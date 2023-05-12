﻿using MySql.Data.MySqlClient;
using OxyPlot;
using OxyPlot.Legends;
using OxyPlot.Series;
using SmartHomeMonitoringApp.Logics;
using SmartHomeMonitoringApp.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace SmartHomeMonitoringApp.Views
{
    /// <summary>
    /// VisualizationControl.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class VisualizationControl : UserControl
    {
        List<string> Divisions = null;

        string FirstSensingDate = string.Empty;

        int TotalDataCount = 0;     // 검색된 데이터 개수

        public VisualizationControl()
        {
            InitializeComponent();
        }

        private void UserControl_Loaded(object sender, RoutedEventArgs e)
        {
            Divisions = new List<string> 
            {
                "SELECT", "LIVING", "DINING", "BED", "BATH"
            };
            CboRoomName.ItemsSource = Divisions;
            CboRoomName.SelectedIndex = 0;  // SELECT가 기본설정
            
            // 검색시작일 날짜 - DB에서 제일 오래된 날짜를 가져와서 뿌림
            using (MySqlConnection conn = new MySqlConnection(Commons.MYSQL_CONNSTRING))
            {
                conn.Open();
                var dtQuery = @"SELECT F.Sensing_Date
                                    FROM(
	                                    SELECT DATE_FORMAT(Sensing_DateTime, '%Y-%m-%d') AS Sensing_Date
	                                    FROM smarthomesensor
                                    ) AS F
                                    GROUP BY F.Sensing_Date
                                    ORDER BY F.Sensing_Date ASC Limit 1;";
                MySqlCommand cmd = new MySqlCommand(dtQuery, conn);
                var result = cmd.ExecuteScalar();
                Debug.WriteLine(result.ToString());
                FirstSensingDate = DtpStart.Text = result.ToString();

                // 검색종료일은 현재일자 할당
                DtpEnd.Text = DateTime.Now.ToString("yyyy-MM-dd");
            }
            
        }

        // 검색버튼 클릭 이벤트 핸들러
        private async void BtnSearch_Click(object sender, RoutedEventArgs e)
        {
            bool IsValid = true;
            string errorMsg = string.Empty;
            DataSet ds = new DataSet();

            // 검색, 저장, 수정, 삭제 전 반드시 검증(Validation)
            if (CboRoomName.SelectedValue.ToString() == "SELECT")
            {
                IsValid = false;
                errorMsg += "방구분을 선택하세요.\n";
            }

            // 시스템 시작된 날짜보다 더 옛날 날짜로 검색하려면
            if (DateTime.Parse(DtpStart.Text) < DateTime.Parse(FirstSensingDate))
            {
                IsValid = false;
                errorMsg += $"검색 시작일은 {FirstSensingDate}부터 가능합니다.\n";
            }

            // 오늘날짜 이후 날짜로 검색하려면
            if (DateTime.Parse(DtpEnd.Text) > DateTime.Now) 
            {
                IsValid = false;
                errorMsg += $"검색 종료일은 오늘까지 가능합니다.\n";
            }

            // 검색시작일이 검색종료일보다 이후면
            if (DateTime.Parse(DtpStart.Text) > DateTime.Parse(DtpEnd.Text))
            {
                IsValid = false;
                errorMsg += $"검색 시작일은 검색종료일보다 늦으면 안됩니다!\"\n";
            }

            if (IsValid == false) 
            {
                await Commons.ShowCustomMessageAsync("검색", errorMsg);
                return;
            }

            // 예외 다 잡았으니 검색 시작 기능 구현
            TotalDataCount = 0;
            try
            {
                using (MySqlConnection conn = new MySqlConnection(Commons.MYSQL_CONNSTRING))
                {
                    conn.Open();
                    var searchQuery = @"SELECT id,
	                                           Home_Id,
	                                           Room_Name,
                                               Sensing_DateTime,
                                               Temp,
                                               Humid
                                          FROM smarthomesensor
                                        WHERE UPPER(Room_Name) = @Room_Name
                                          AND DATE_FORMAT(Sensing_DateTime, '%Y-%m-%d') 
                                        BETWEEN @StartDate AND @EndDate";
                    MySqlCommand cmd = new MySqlCommand(searchQuery, conn);
                    cmd.Parameters.AddWithValue("@Room_Name", CboRoomName.SelectedValue.ToString());
                    cmd.Parameters.AddWithValue("@StartDate", DtpStart.Text);
                    cmd.Parameters.AddWithValue("@EndDate", DtpEnd.Text);
                    MySqlDataAdapter adapter = new MySqlDataAdapter(cmd);
                    
                    adapter.Fill(ds, "smarthomesensor");

                    // MessageBox.Show("TotalData", ds.Tables["smarthomesensor"].Rows.Count.ToString()); // 데이터 개수 확인!
                }
            }
            catch (Exception ex)
            {
                await Commons.ShowCustomMessageAsync("DB검색", $"DB검색 오류 {ex.Message}");
               
            }

            var tmp = new PlotModel { Title = $"{CboRoomName.SelectedValue} ROOM" };
            var legend = new Legend
            {
                LegendBorder = OxyColors.DarkGray,
                LegendBackground = OxyColor.FromArgb(150, 255, 255, 255),
                LegendPosition = LegendPosition.TopRight,
                LegendPlacement = LegendPlacement.Outside,
            };

            tmp.Legends.Add(legend);    // 범례추가

            var tempSeries = new LineSeries
            {
                Title = "Temperature",
                MarkerType = MarkerType.Circle,
                Color = OxyColors.DarkOrange        // 라인색상 온도는 주황색

            };

            var humidSeries = new LineSeries
            {
                Title = "Humidity(%)",
                MarkerType = MarkerType.Square,
                Color = OxyColors.Aqua      // 습도는 물색
            };

            // DB에서 가져온 데이터 차트에 뿌리도록 처리
            if (ds.Tables[0].Rows.Count > 0)
            {
                TotalDataCount = ds.Tables[0].Rows.Count;
                // Create the plot model    // 선택한 방의 이름이 타이틀로 나오도록
                
                var count = 0;

                foreach (DataRow row in ds.Tables[0].Rows)
                {
                    tempSeries.Points.Add(new DataPoint(count++, Convert.ToDouble(row["Temp"])));
                    humidSeries.Points.Add(new DataPoint(count++, Convert.ToDouble(row["Humid"])));
                }
            }

            // Add the series to the plot model
            tmp.Series.Add(tempSeries);
            tmp.Series.Add(humidSeries);

            OpvSmartHome.Model = tmp;

            LblTotalCount.Content = $"검색데이터 {TotalDataCount}개";
        }
    }
}
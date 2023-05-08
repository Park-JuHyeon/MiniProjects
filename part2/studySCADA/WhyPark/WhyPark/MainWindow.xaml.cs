using MahApps.Metro.Controls;
using MySql.Data.MySqlClient;
using System;
using System.Diagnostics;
using System.Windows;
using WhyPark.Logics;

namespace WhyPark
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private async void BtnRequest_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                using (MySqlConnection conn = new MySqlConnection(Commons.myConnString))
                {
                    if (conn.State == System.Data.ConnectionState.Closed) conn.Open();
                    
                    var query = @"INSERT INTO managertbl
                                            (studentID,
                                            studentName,
                                            reason,
                                            startDate,
                                            endDate
                                            
                                            )
                                            VALUES
                                            (@studentID,
                                            @studentName,
                                            @reason,
                                            @startDate,
                                            @endDate
                                           
                                            );";

                    MySqlCommand cmd = new MySqlCommand(query, conn);
                    cmd.Parameters.AddWithValue("@studentID", TxtStudentId.Text);
                    cmd.Parameters.AddWithValue("@studentName", TxtStudentName.Text);
                    cmd.Parameters.AddWithValue("@reason", TxtReason.Text);
                    cmd.Parameters.AddWithValue("@startDate", DPstart.Text);
                    cmd.Parameters.AddWithValue("@endDate", DPend.Text);
                    cmd.ExecuteNonQuery();
                    Debug.WriteLine(query);
                    await Commons.ShowMessageAsync("저장성공", "존나축하");


                }
            }
            catch (Exception ex)
            {
                await Commons.ShowMessageAsync("오류", $"에러 {ex.Message}");
            }
        }

    }
}

using Google.Protobuf.WellKnownTypes;
using MahApps.Metro.Controls;
using MySql.Data.MySqlClient;
using MySqlX.XDevAPI.Relational;
using System;
using System.Collections.Generic;
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
                    //cmd.Parameters.AddWithValue("@startDate", DPstart.ToString("yyyy-MM-dd"));
                    //cmd.Parameters.AddWithValue("@endDate", DPend.ToString("yyyy-MM-dd"));
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

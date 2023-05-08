using MahApps.Metro.Controls.Dialogs;
using MahApps.Metro.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace WhyPark.Logics
{
    public class Commons
    {
        // MySQL용
        public static readonly string myConnString = "Server=210.119.12.57;" +
                                                     "Port=3306;" +
                                                     "Database=campusdb;" +
                                                     "Uid=root;" +
                                                     "Pwd=12345;";

        // 메트로 다이얼로그창을 위한 메서드
        public static async Task<MessageDialogResult> ShowMessageAsync(string title, string message,
            MessageDialogStyle style = MessageDialogStyle.Affirmative)
        {
            return await ((MetroWindow)Application.Current.MainWindow).ShowMessageAsync(title, message, style, null);
        }

    }
}

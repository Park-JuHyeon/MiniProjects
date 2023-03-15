# 팀 프로젝트 로그인 화면 
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    conn = None
    curIdx = 0  # 현재 데이터 PK

    def __init__(self):
        super().__init__()
        uic.loadUi('./group_project/login.ui', self) 
        self.setWindowIcon(QIcon('./group_project/login.png'))
        self.setWindowTitle('로그인')

        # self.initDB()  # DB 초기화

        # self.btnID.clicked.connect(self.btnIDClikced)
        # self.btnPW.clicked.connect(self.btnPWClikced)
        # self.btnlogin.clicked.connect(self.btnloginClikced)

    # def btnIDClikced(self):





    # def btnPWClikced(self):



    # def btnloginClikced(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())






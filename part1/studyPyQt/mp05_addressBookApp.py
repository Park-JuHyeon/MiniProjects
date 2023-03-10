# 주소록 GUI 프로그램 - My SQL 연동
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    conn = None

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/addressBook.ui', self) 
        self.setWindowIcon(QIcon('./studyPyQt/addressbook2.png'))

        self.initDB()  # DB 초기화

    def initDB(self):
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                                    db = 'miniproject', charset = 'utf8')
        cur = self.conn.cursor()
        query = '''SELECT Idx
                     , FullName
                     , PhoneNum
                     , Email
                     , Address
                 FROM addressbook'''   # 멀티라인 문자열이 편함!
        cur.execute(query)
        rows = cur.fetchall()

        # print(rows)
        self.makeTable(self, rows)
        self.conn.close()   # 프로그램 종료할 때

    def makeTable(self, rows):
        self.tblAddress.setColumnCount(5)  # 0. 열갯수
        self.tblAddress.setRowCount(len(rows)) # 0. 행갯수
        
        for i , row in enumerate(rows):
            # row[0] ~ row[4]
            idx = row[0]
            fullName = row[1]
            phoneNum = row[2]
            email = row[3]
            address = row[4]

            self.tblAddress.setItem(i, 0, QTableWidgetItem(idx))
            self.tblAddress.setItem(i, 1, QTableWidgetItem(fullName))
            self.tblAddress.setItem(i, 2, QTableWidgetItem(phoneNum))
            self.tblAddress.setItem(i, 3, QTableWidgetItem(email))
            self.tblAddress.setItem(i, 4, QTableWidgetItem(address))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())




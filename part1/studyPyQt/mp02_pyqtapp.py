# Qt Designer 디자인 사용
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    count = 0  # 클랙횟수 카운트 변수

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/mainApp.ui', self)  # 복잡하게 기능 다 타이핑하지말고 만들어서 로드해라!!
        
        # Qt Designer에서 구성한 위젯 시그널 만듬
        self.btnOK.clicked.connect(self.btnOKClicked)
        self.btnpop.clicked.connect(self.btnpopClicked)

    def btnpopClicked(self):
        QMessageBox.about(self, 'popup', '까꿍!')  # about(self, 이름, 내용)

    def btnOKClicked(self):  # 슬롯함수
        self.count += 1
        self.lblMessage.clear()
        self.lblMessage.setText(f'메시지: OK!! + {self.count}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())

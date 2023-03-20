import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  #  Qt.white ...
import qrcode

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPython/qrcodeApp.ui', self) 
        self.setWindowTitle('QrCode 생성앱 v0.1')
        self.setWindowIcon(QIcon('./studyPython/QRcode.png'))

        self.btnQrGen.clicked.connect(self.makeQRcode)
        self.txtQrData.returnPressed.connect(self.makeQRcode)

    def makeQRcode(self):
        
        data = '안녕'
        qr_img = qrcode.make(data)  # pixmap() 함수생성
        qr_img.save('./studyPython/Name.png')

        img = QPixmap('./studyPython/Name.png')
        self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(200))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())


def makeQRcode(self):
        
        data = self.txtName.text()
        qr_img = qrcode.make(data)  # pixmap() 함수생성
        qr_img.save('./Campus/Name.png')

        img = QPixmap('./Campus/Name.png')
        self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(200))


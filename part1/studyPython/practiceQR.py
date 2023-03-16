import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  #  Qt.white ...
import qrcode

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('C:\Source\Campus\project/studentCard.ui', self) 
        self.setWindowTitle('QrCode 생성앱 v0.1')
        self.setWindowIcon(QIcon('./studyPython/QRcode.png'))

        img = qrcode.make('안녕안녕')
        img.save('C:/Source/hello.png')
        print(type(img))
        print(img.size)

        #self.txtQrData.returnPressed.connect(self.btnQrGenClicked)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())



# Qt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import *
from urllib.request import urlopen
import webbrowser # 웹브라우저 모듈

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverAPIMovie.ui', self) 
        self.setWindowIcon(QIcon('./studyPyQt/newspaper.png'))

        # 검색 버튼 클릭시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요!')
            return
        else:
            api = NaverApi()  # NaverAPi 클래스 객체 생성
            node = 'movie' # movie로 변경하면 영화검색
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            # print(result) 
            # 테이블위젯 출력 기능
            items = result['items']  # json전체 결과 중 items 아래 배열만 추출
            self.makeTable(items)   # 테이블위젯에 데이터들을 할당하는 함수
    
    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # column = self.tblResult.currentIndex().column()
        # print(row, column)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text()  # url 링크컬럼 변경
        webbrowser.open(url)  # 네이버 영화 웹사이트 오픈
        
    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과 변경
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # 단일선택
        self.tblResult.setColumnCount(7)  # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items))   # items가 100개 이므로 100개의 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60) # 개봉년도
        self.tblResult.setColumnWidth(4, 50) # 평점
        # 컬럼 데이터를 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, post in enumerate(items):   # 0, 뉴스 ...
            title = self.replaceHtmlTag(post['title'])
            pubDate = post['pubDate']
            director = post['director']
            actor = post['actor']
            userRating = post['userRating']
            link = post['link']
            # image = QImage(requests.get(post['image'], stream = True))
            # imageData = urlopen(post['image']).read()
            # image = QPixmap()

            # image.loadFromData(imageData)
            # imgLabel = QLabel()
            # imgLabel.setPixmap(image)
            # imgLabel.setGeometry(0,0,60,100) 
            # imgLabel.resize(60, 100)

            # setItem(행, 열, 넣을데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link)) 
            self.tblResult.setCellWidget(i, 6, imgLabel)   
    
    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<')  
        result = result.replace('&gt', '>')   
        result = result.replace('<b>', '')  
        result = result.replace('</b>', '')  
        result = result.replace('&apos;', "'")  
        result = result.replace('&quot;', '"')   
        # 변환안된 특수문자가 나타날때마다 추가하면 됨

        return result
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp() 
    ex.show()
    sys.exit(app.exec_())

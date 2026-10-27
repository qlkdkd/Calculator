# ui.py

from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QVBoxLayout, QMessageBox, \
    QPlainTextEdit, QHBoxLayout, QLabel # QLabel 추가

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        # 날짜 위젯
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)

        # 텍스트 에디트 위젯 추가(읽기만 가능)
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        # 버튼1 (메시지 생성) 구성
        self.btn1 = QPushButton('Message', self) # 버튼 추가

        # 버튼2 (메시지 전체 삭제) 구성
        self.btn2 = QPushButton('Clear', self)

        # 레이아웃 구성
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        #vbox.addStretch(1)
        vbox.addWidget(self.lbl1)

        self.setLayout(vbox)

        # 창 구성
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText("Button clicked")

    def clearMessage(self):
        self.te1.clear()
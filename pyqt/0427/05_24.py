import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Worker(QThread):  #QThread를 상속받아 Worker 클래스를 정의
    def run(self):
        while True:
            print('Hello')
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
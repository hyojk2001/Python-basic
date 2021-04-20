import sys 
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
btn = QPushButton('hello')
btn.show()
app.exec_()
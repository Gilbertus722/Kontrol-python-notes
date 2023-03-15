from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QmainWindow, QMessageBox
from PyQt5.QtCore import Qt, QTimer
import sys
import datetime

def aplic():
    app = QApplication(sys.argv)
    okno = Window()

    okno.show()
    sys.exit(app.exec_())

if __name__ == '_main_':
    aplic

class Window(QmainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("progams")
        self.setGeometry(400,400,600.300)
    

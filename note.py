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
        self.text_data = QtWidgets.QLabel(self)
        self.text_data.setText("Выберите дату")
        self.text_data.adjustSize()
        self.text_data.move(10,52)

        self.time=QtWidgets.QTimeEdit(self)
        self.time.move(100.100)
        self.time.adjustSize()

        self.time=QtWidgets.QTimeEdit(self)
        self.time.move(110,100)
        self.time.adjustSize()

        self.sobati = QtWidgets.QLineEdit(self)
        self.sobati.setGeometry(100,150,160,30)
        self.sobati.adjustSixe()
        self.sobati.setPlaceholderText('Введите событие')

        self.knopka = QtWidgets.QPushButton(self)
        self.knopka.move(210,80)
        self.knopka.setText('Подтвердить')
        self.knopkaadjustSize()
        
        

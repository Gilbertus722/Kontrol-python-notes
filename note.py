
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
        self.knopka.clicked.connect(self.knopka_gotovo)

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

    def knopka_gotovo(self):
        data_txt=str(self.data.text)
        time_txt=str(self.time.text())
        sobati_text=str(self.sobati.text)
        print("Дата: "+data_text)
        print("Время: "+time_text)
        print("Событие: "+sobati_txt)
        File_A = open('dataTime.txt','a+')
        DataTime_txt = (data_txt + " ' "+ time_txt +" ' "+ sobati_text)
        Data_txt = (data_txt + " ' time ' "+ sobati_text)
        File_A.write(DataTime_txt+ '\n')
        File_A.write(Data_txt + '\n')
        File_A.close()

    def proverka(self):

        date_pk = datetime.date.today()
        time_pk = datetime.datetime.now().time()
        date_pk = str(date_pk)
        time_pk = str(time_pk)
        one = date_pk[:4:]
        two = date_pk[8::]
        date_pk = date_pk[4:8:]
        date_pk (two + date_pk +one)
        date_pk = date_pk.replace('-','.')

        time_pk = time_pk[:5:]

        dateTime_pk = (date_pk + " ' " + time_pk )
        print(dateTime_pk+ " = Текущее дата и время")

        date_pk = (date_pk + " ' time")

File_R = open("dateTime.txt", "r")
lines = File_R.readlines()
File_R.close()
lines = [line.rstrip() for line in lines]

for line in lines:
    if date_pk in line:

        index_date = lines.index(line)
        del lines[index_date]

        text = line[19::]

        self.error = QtWidgets.QMessageBox(self)
        self.error.setWindowTitle("Напоминаю")
        self.error.setText(text)
        self.error.setIcon(QtWidgets.QMessageBox.Warning)
        self.error.setStandardButtons(self.error.Ok|self.error.Cancel)
        self.error.exec_()

    if dateTime_pk in line:

        index_dateTime = lines.index(line)
        del lines[index_dateTime]

        text = line[20::]

        self.error = QtWidgets.QMessageBox(self)
        self.error.setWindowTitle("Напоминаю")
        self.error.setText(text)
        self.error.setIcon(QtWidgets.QMessageBox.Warning)
        self.error.setStandardButtons(self.error.Ok|self.error.Cancel)
        self.error.exec_()

File_R - open("dateTime.txt", "w")
for i in lines:
    File_R.write(i + '\n')
File_R.close()






        

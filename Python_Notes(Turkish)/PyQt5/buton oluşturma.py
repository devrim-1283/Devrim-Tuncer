import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def pencere():

    app = QtWidgets.QApplication(sys.argv) # klasik

    witget = QtWidgets.QWidget()  # klasik

    witget.setWindowTitle("Buton Oluşturma")

    etiket1 = QtWidgets.QLabel(witget)
    etiket1.setText("Selam")
    etiket1.move(100,100)

    buton = QtWidgets.QPushButton(witget)
    buton.setText("Buton")              # buton oluşturma
    buton.move(200,200)


    witget.show()

    sys.exit(app.exec_())

pencere()
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Radio Button")
        self.raido_string = QtWidgets.QLabel("Hangi Dili Seviyorsun ?")
        self.python = QtWidgets.QRadioButton("Python")
        self.java = QtWidgets.QRadioButton("Java")
        self.php = QtWidgets.QRadioButton("PHP")
        self.yazı = QtWidgets.QLabel(self)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.raido_string)
        vbox.addWidget(self.python)
        vbox.addWidget(self.java)
        vbox.addWidget(self.php)
        vbox.addWidget(self.yazı)

        self.python.toggled.connect(self.checked)
        self.java.toggled.connect(self.checked)
        self.php.toggled.connect(self.checked)

        self.setLayout(vbox)
        self.show()

    def checked(self):
        if self.python.isChecked():
            self.yazı.setText("Python")
        elif self.java.isChecked():
            self.yazı.setText("Java")
        else:
            self.yazı.setText("PHP")


app = QtWidgets.QApplication(sys.argv)
window = window()
sys.exit(app.exec_())
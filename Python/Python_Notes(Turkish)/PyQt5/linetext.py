import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("LineText")
        self.yazı = QtWidgets.QTextEdit(self)

        vlay = QtWidgets.QVBoxLayout()
        vlay.addWidget(self.yazı)


        self.setLayout(vlay)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = windows()
sys.exit(app.exec_())
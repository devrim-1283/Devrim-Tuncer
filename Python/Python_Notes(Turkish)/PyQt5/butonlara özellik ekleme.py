import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.yazı = QtWidgets.QLabel("0")
        self.buton = QtWidgets.QPushButton("Arttır")
        self.buton2 = QtWidgets.QPushButton("Azalt")
        self.sayı = 0
    # classla oluşturduğumuz zaman layout yapmazsak görünmez eklediklerimiz

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.buton2)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.buton.clicked.connect(self.click1)
        self.buton2.clicked.connect(self.click2)


        self.setLayout(h_box)
        self.show()

    def click1(self):
        self.sayı+=1
        self.yazı.setText(str(self.sayı))

    def click2(self):
        self.sayı-=1
        self.yazı.setText(str(self.sayı))



app = QtWidgets.QApplication(sys.argv)
window = window()
sys.exit(app.exec_())

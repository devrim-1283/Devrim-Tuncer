import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.main_1()
    def main_1(self):
        self.kullanıcı_adı = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) # parolayı gizleme

        self.new_label = QtWidgets.QLabel("Kullanıcı Adı: ")
        self.new_label2 = QtWidgets.QLabel("Şifre: ")

        self.login = QtWidgets.QPushButton("Giriş")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.new_label)
        h_box.addWidget(self.kullanıcı_adı)
        h_box.addStretch()


        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.new_label2)
        h2_box.addWidget(self.password)
        h2_box.addStretch()

        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addStretch()
        h3_box.addWidget(self.login)
        h3_box.addStretch()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addStretch()

        self.setLayout(v_box)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = windows()
sys.exit(app.exec_())

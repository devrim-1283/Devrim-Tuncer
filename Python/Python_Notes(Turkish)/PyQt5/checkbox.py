import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Checkbox")
        self.checkbox = QtWidgets.QCheckBox("""Esmayı seviyor musun ?""")
        self.button = QtWidgets.QPushButton("Kontrol Et")
        self.yazı = QtWidgets.QLabel(self)


        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(self.checkbox)
        v_layout.addWidget(self.yazı)
        v_layout.addWidget(self.button)

        #self.checkbox.stateChanged.connect(lambda: self.button_clicked(self.checkbox.isChecked(),self.yazı)) # bu chackboxun durumu değiştiği an çalışır
        self.button.clicked.connect(lambda: self.button_clicked(self.checkbox.isChecked(),self.yazı)) # fonskiyon içine fonskyion objesi gönderme


        self.setLayout(v_layout)
        self.show()
    def button_clicked(self,check,yazı):
        if check:
            self.yazı.setText("Esma'yı seviyorsun...")
        else:
            self.yazı.setText("""Emin misin ? .....
            Saçmalama istersen.........
            Hemen tıklaaaaaaaaaaaaa""")

app = QtWidgets.QApplication(sys.argv)
window = window()
sys.exit(app.exec_())
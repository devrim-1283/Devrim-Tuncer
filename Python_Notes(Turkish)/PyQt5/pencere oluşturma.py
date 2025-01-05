import sys  # Programın terminalden çalışması için gerekli
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv) # klasik yazman gerek terminalde çalışması için

    windows = QtWidgets.QWidget()   # pencere oluşturma

    windows.setWindowTitle("Ders 1 Pencere Oluşturma")  # pencereye başlık verme

    windows.show()   # pencereyi gösterme

    sys.exit(app.exec_())  # biz çarpı tuşuna basmadığaımız sürece uygulama çalışacak
window()



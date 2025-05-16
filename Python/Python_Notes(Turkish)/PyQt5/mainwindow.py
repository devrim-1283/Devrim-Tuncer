import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QAction,QMainWindow


class menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu('Dosya')
        düzenle = menubar.addMenu("Düzenle")


        dosya_ac = QAction( 'Dosya Aç', self)
        dosya_ac.setShortcut('Ctrl+O')

        dosya_kaydet = QAction( 'Dosya Kaydet', self)
        dosya_kaydet.setShortcut('Ctrl+S')

        cıkıs = QAction("Çıkıs", self)
        cıkıs.setShortcut('Ctrl+Q')

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cıkıs)

        ara_bul = QAction( 'Ara Bul', self)
        ara = düzenle.addMenu('Ara')

        cıkıs.triggered.connect(self.dosyaClicked)
        dosya.triggered.connect(self.dosya)
        ara.addAction(ara_bul)
        self.show()
    def dosyaClicked(self):
        QApplication.quit()
    def dosya(self,action):
        if action.text().lower()=="dosya aç":
            print("dosya açıldı")
        elif action.text().lower()=="dosya kaydet":
            print("dosya kaydet")

app = QApplication(sys.argv)
window = menu()
window.setWindowTitle('Menü')
sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets,QtGui

def pencere():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("Pencereye Yazı ve Resim ekleme")

    window.setGeometry(100,100,1000,500) # ilk iki parametre uygulamanın hangi konumda başlatılacağını diğer iki parametre ise boyutunu ifade eder

    new_label = QtWidgets.QLabel(window)
    new_label.setText("Devrim Tunçer ")                   # Yazı ekleme
    new_label.move(200,30)

    new_picture = QtWidgets.QLabel(window)
    new_picture.setPixmap(QtGui.QPixmap("WhatsApp Image 2024-11-30 at 16.15.27.jpeg"))    # Resim ekleme
    new_picture.move(150,100)

    # bu yöntemler akıllıca ve kullanışlı değil biz bunları layoutlar ile yapıcaz şimdilik görmek içine

    window.show()

    sys.exit(app.exec_())

pencere()
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def window():

    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")   # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")


    h_layout = QtWidgets.QHBoxLayout()
    h_layout.addWidget(buton1)
    h_layout.addWidget(buton2)

    windows.setLayout(h_layout)
    windows.setGeometry(100,100,1000,1000)

    windows.show()
    sys.exit(app.exec_())

def window1():

    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")   # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")


    h_layout = QtWidgets.QHBoxLayout()
    h_layout.addWidget(buton1)
    h_layout.addWidget(buton2)
    h_layout.addStretch()

    windows.setLayout(h_layout)
    windows.setGeometry(100,100,1000,1000)

    windows.show()
    sys.exit(app.exec_())

def window2():

    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")   # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")


    h_layout = QtWidgets.QHBoxLayout()

    h_layout.addStretch()
    h_layout.addWidget(buton1)
    h_layout.addWidget(buton2)


    windows.setLayout(h_layout)
    windows.setGeometry(100,100,1000,1000)

    windows.show()
    sys.exit(app.exec_())


def window3():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    h_layout = QtWidgets.QHBoxLayout()


    h_layout.addWidget(buton1)
    h_layout.addStretch()
    h_layout.addWidget(buton2)

    windows.setLayout(h_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())

def window4():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()


    v_layout.addWidget(buton1)
    v_layout.addWidget(buton2)

    windows.setLayout(v_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())


def window5():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()


    v_layout.addWidget(buton1)
    v_layout.addWidget(buton2)
    v_layout.addStretch()

    windows.setLayout(v_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())

def window6():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()


    v_layout.addWidget(buton1)
    v_layout.addStretch()
    v_layout.addWidget(buton2)


    windows.setLayout(v_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())


def window7():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()


    v_layout.addStretch()
    v_layout.addWidget(buton1)
    v_layout.addWidget(buton2)

    windows.setLayout(v_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())

def window8():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()

    v_layout.addWidget(buton1)
    v_layout.addWidget(buton2)

    h_layout = QtWidgets.QHBoxLayout()

    h_layout.addWidget(buton1)
    h_layout.addWidget(buton2)

    v_layout.addLayout(h_layout)
    windows.setLayout(v_layout)
    windows.setGeometry(100, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())

def window9():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    windows.setWindowTitle("Layout")  # iki türlü layout vardır vertical ve horizontal biri dikey diğeri yatay layout

    buton1 = QtWidgets.QPushButton("Button 1")
    buton2 = QtWidgets.QPushButton("Button 2")

    v_layout = QtWidgets.QVBoxLayout()
    v_layout.addStretch()
    v_layout.addWidget(buton1)
    v_layout.addWidget(buton2)


    h_layout = QtWidgets.QHBoxLayout()
    h_layout.addStretch()
    h_layout.addWidget(buton1)

    h_layout.addWidget(buton2)



    v_layout.addLayout(h_layout)

    windows.setLayout(v_layout)


    windows.setGeometry(10, 100, 1000, 1000)

    windows.show()
    sys.exit(app.exec_())
# Horizontal Layout
#window()
#window1()
#window2()
#window3()

# Vertical Layout
#window4()
#window5()
#window6()
#window7()

# Veritical and Horizontal
#window8()
window9()

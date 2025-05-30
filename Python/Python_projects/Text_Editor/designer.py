from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        v_box = QtWidgets.QVBoxLayout(self.centralwidget)
        v_box.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını sıfırla
        v_box.setSpacing(0)  # Widget'lar arası boşluğu sıfırla
        v_box.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTheme = QtWidgets.QMenu(self.menuSettings)
        self.menuTheme.setObjectName("menuTheme")
        self.menuPage = QtWidgets.QMenu(self.menubar)
        self.menuPage.setObjectName("menuPage")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Page = QtWidgets.QAction(MainWindow)
        self.actionNew_Page.setObjectName("actionNew_Page")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionDark_Theme = QtWidgets.QAction(MainWindow)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionDefault_Theme = QtWidgets.QAction(MainWindow)
        self.actionDefault_Theme.setObjectName("actionDefault_Theme")
        self.actionClear_2 = QtWidgets.QAction(MainWindow)
        self.actionClear_2.setObjectName("actionClear_2")
        self.actionDeveloped_by_Devrim_Tun_er = QtWidgets.QAction(MainWindow)
        self.actionDeveloped_by_Devrim_Tun_er.setObjectName("actionDeveloped_by_Devrim_Tun_er")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.menuFile.addAction(self.actionNew_Page)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionOpen)
        self.menuTheme.addAction(self.actionDark_Theme)
        self.menuTheme.addAction(self.actionDefault_Theme)
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuPage.addAction(self.actionClear_2)
        self.menuAbout.addAction(self.actionDeveloped_by_Devrim_Tun_er)
        self.menuAbout.addAction(self.actionGithub)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuPage.setTitle(_translate("MainWindow", "Page"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_Page.setText(_translate("MainWindow", "New Page"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionDark_Theme.setText(_translate("MainWindow", "Dark Theme"))
        self.actionDefault_Theme.setText(_translate("MainWindow", "Default Theme"))
        self.actionClear_2.setText(_translate("MainWindow", "Clear"))
        self.actionDeveloped_by_Devrim_Tun_er.setText(_translate("MainWindow", "Developed by Devrim Tunçer"))
        self.actionGithub.setText(_translate("MainWindow", "Linkedin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

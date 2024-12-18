from designer import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import os
import webbrowser

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.folder()
        self.init_ui()
    def folder(self):
        username = os.getenv("USERNAME") or os.getenv("USER")
        os.chdir(f"/home/{username}/Documents")
        try:
            os.mkdir("text_editor")
            os.chdir("text_editor")
        except:
            os.chdir("text_editor")
    def init_ui(self):
        self.ui.actionNew_Page.triggered.connect(self.new_page)
        self.ui.actionSave.triggered.connect(self.save_page)
        self.ui.actionOpen.triggered.connect(self.open_page)
        self.ui.actionSave_as.triggered.connect(self.save_as_page)

        self.ui.actionDark_Theme.triggered.connect(self.dark_theme)
        self.ui.actionDefault_Theme.triggered.connect(self.default_theme)

        self.ui.actionClear_2.triggered.connect(self.clear_page)

        self.ui.actionDeveloped_by_Devrim_Tun_er.triggered.connect(self.github)
        self.ui.actionGithub.triggered.connect(self.linkedin)

        self.show()
    def clear_page(self):
        self.ui.textEdit.clear()
    def new_page(self):
        self.ui.textEdit.clear()
        self.setWindowTitle("New Page - Text Editor")
    def save_page(self):
        first_line = self.ui.textEdit.toPlainText().splitlines()[0] if self.ui.textEdit.toPlainText().splitlines() else 'Untitled.txt'
        with open(f"{first_line}.txt","w") as file:
            file.write(str(self.ui.textEdit.toPlainText()))
    def open_page(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.ui.textEdit.setText(file.read())
        self.setWindowTitle(str(file_name[0])+" - Text Editor")
    def save_as_page(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        with open(file_name[0],"w") as file:
            file.write(str(self.ui.textEdit.toPlainText()))
    def dark_theme(self):
        dark_stylesheet = """
              QMainWindow {
                  background-color: #121212;
                  color: #FFFFFF;
              }
              QTextEdit {
                  background-color: #1E1E1E;
                  color: #FFFFFF;
              }
              QMenuBar {
                  background-color: #121212;
                  color: #FFFFFF;
              }
              QMenu {
                  background-color: #121212;
                  color: #FFFFFF;
              }
              QToolBar {
                  background-color: #1E1E1E;
              }
          """
        self.setStyleSheet(dark_stylesheet)

    def default_theme(self):
        default_stylesheet = """
            QMainWindow {
                background-color: #FFFFFF;
                color: #000000;
            }
            QTextEdit {
                background-color: #FFFFFF;
                color: #000000;
            }
            QMenuBar {
                background-color: #FFFFFF;
                color: #000000;
            }
            QMenu {
                background-color: #FFFFFF;
                color: #000000;
            }
            QToolBar {
                background-color: #E0E0E0;
            }
            QPushButton {
                background-color: #E0E0E0;
                color: #000000;
            }
        """
        self.setStyleSheet(default_stylesheet)
    def github(self):
        webbrowser.open("https://github.com/devrim-1283")
    def linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/devrim-tun%C3%A7er-218a55320/")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = mainWindow()
    sys.exit(app.exec_())


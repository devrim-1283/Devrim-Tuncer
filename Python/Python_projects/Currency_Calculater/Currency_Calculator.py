from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
import requests
import webbrowser
import sys
import os
import datetime
import sqlite3
import shutil

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.exec_file = os.path.expanduser("~/.local/share/Currency_Calculator/")
        self.desktop()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database_1()
        self.config()
        self.connection()
        self.table_widget()
        self.theme_default()
        self.__new_init__(self)
    def desktop(self):
        home_dir = os.path.expanduser("~")
        target_dir = os.path.expanduser("~/.local/share/Currency_Calculator")
        found_path = None
        if not os.path.exists(target_dir):
            for root, dirs, files in os.walk(home_dir):
                if "Currency_Calculator" in dirs:  
                    found_path = os.path.join(root,"Currency_Calculator")  
                    break 
            shutil.copytree(found_path,target_dir)
            target_file = os.path.expanduser("~/.local/share/applications/currency_calculator.desktop")
            exec_bash = f'Exec=bash -c "cd {self.exec_file} && ./Currency_Calculator"'
            icon_file = os.path.expanduser("~/.local/share/Currency_Calculator/icon.png")
            if not os.path.exists(target_file):
                string_desktop=f"""
[Desktop Entry]
Name=Currency Calculator
{exec_bash}
Icon={icon_file}
Type=Application
Categories=Utility;Finance
Terminal=false
    """ 
                with open(target_file,"w") as file:
                    file.write(string_desktop)
                os.chmod(target_file, 0o755)
                os.chmod(self.exec_file,0o755)
    def database_1(self):
        database = sqlite3.connect(f"{self.exec_file}currency.db")
        cursore = database.cursor()
        cursore.execute("CREATE TABLE IF NOT EXISTS history (number_1 INTEGER,amount TEXT, from_1 TEXT, to_1 TEXT, total TEXT, date_1 year_1 TEXT, hour_1 TEXT)")
        database.commit()
        database.close()
    def config(self):
        if os.path.isfile(f"{self.exec_file}.config"):
            with open(f"{self.exec_file}.config", "r") as config:
                content = config.read().split(",")
                self.api = content[0]
                self.theme = content[1]
                self.number_1 = int(content[2])

        else:
            self.api = "https://data.fixer.io/api/latest?access_key=e78bd0e7a643c9a26e0faa75d0dd0c39"
            self.theme = "Default"
            self.number_1 = 1
            with open(f"{self.exec_file}.config", "w") as config:
                config.write(self.api+",")
                config.write(self.theme+",")
                config.write(str(self.number_1)+",")

    def connection(self):
        with open(f"{self.exec_file}.config", "r") as config:
            self.api = config.read().split(",")[0]
        try:
            html = requests.get(self.api)
            self.content = html.json()
            if self.content["success"]:
                self.ui.label_7.setText("Successfully Connected to API")
            else:
                self.ui.label_7.setText("Failed to Connect to API")
            self.ui.lineEdit_2.setText(self.api)
        except:
            self.ui.label_7.setText("Failed to Connect to API")
    def conventer(self,a, b, c):
        currency_a = None
        currency_b = None
        for i, j in self.content["rates"].items():
            if i == a:
                currency_a = j
            if i == b:
                currency_b = j
        calculate = currency_b / currency_a
        return str(c * calculate)[0:8]

    def __new_init__(self, parent):
        self.total = None
        self.amount = None
        self.ui.textEdit.setText("""
        Welcome to the Currency Converter App

Developed by Devrim Tunçer



App Features

- On the right side, you can:

  - Convert your desired currency to any other currency  

  - Copy the conversion results  

  - Review your past conversion transactions  

  - Quickly perform swaps  

  - Update the API  



Get Your API Key

- At the top, visit https://fixer.io to obtain your API key.  

- Enter and save the key in the designated API section.



Currency Information

- On the left side, you will see the exchange rates of your selected currency against 46 different currencies.  

- When you update the API, the exchange rates will be refreshed.



Additional Features

- Use the menu buttons to:

  - Change the theme  

  - Access links to Devrim Tunçer's LinkedIn account  

  - Visit the GitHub repository for the project  
        """)
        self.ui.actionDark_Theme.triggered.connect(self.dark)
        self.ui.actionDefault_Theme.triggered.connect(self.default)
        self.ui.actionGithub.triggered.connect(self.github)
        self.ui.actionDevrim_Tun_er.triggered.connect(self.linkedin)
        self.ui.pushButton_7.clicked.connect(self.clear_api)
        self.ui.pushButton_6.clicked.connect(self.api_load)
        self.ui.pushButton_5.clicked.connect(self.fixer)
        self.ui.pushButton_9.clicked.connect(self.clear_notes)
        self.ui.pushButton_8.clicked.connect(self.calculate)
        self.ui.pushButton.clicked.connect(self.download)
        self.ui.pushButton_2.clicked.connect(self.copy_total)
        self.ui.pushButton_3.clicked.connect(self.swap)
        self.ui.pushButton_4.clicked.connect(self.update_api)
        self.ui.comboBox_5.currentIndexChanged.connect(self.table_widget)
        self.show()
    def calculate(self):
        if self.ui.label_7.text() == "Successfully Connected to API" or self.ui.label_7.text() == "UPDATE API":
            from_1 = self.ui.comboBox_4.currentText()
            to_1 = self.ui.comboBox_6.currentText()
            try:
                self.amount = float(self.ui.lineEdit.text())
                self.total = self.conventer(from_1, to_1,self.amount)
                self.ui.label_4.setText(self.total)
                self.number_1+=1
                with open(f"{self.exec_file}.config", "r+") as config:
                    content = config.read().split(",")
                    content[2] = str(self.number_1)
                    config.seek(0)
                    for i in content:
                        config.write(i+",")
            except:
                self.ui.label_4.setText("Error VALUE")
            if self.ui.label_4!="Error VALUE":
                database = sqlite3.connect(f"{self.exec_file}currency.db")
                cursore = database.cursor()
                day_month_year = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year)
                hour_minute_second = str(datetime.datetime.now().hour) + "/" + str(datetime.datetime.now().minute)+ "/" + str(datetime.datetime.now().second)
                cursore.execute("insert into history values(?,?,?,?,?,?,?)",(self.number_1,self.amount,from_1,to_1,self.total,day_month_year,hour_minute_second))
                database.commit()
                cursore.execute('SELECT * FROM history ORDER BY number_1 DESC LIMIT 25;')
                list_history = cursore.fetchall()
                database.close()
                row = 0
                for i in list_history:
                    self.ui.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(i[1]))
                    self.ui.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(i[2]))
                    self.ui.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(i[3]))
                    self.ui.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(i[4]))
                    self.ui.tableWidget_2.setItem(row, 4,QtWidgets.QTableWidgetItem(i[5]))
                    self.ui.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(i[6]))
                    row+=1
        else:
            self.ui.label_4.setText("Error API")
    def table_widget(self):
        currency_dict = {
            0: "USD",
            1: "EUR",
            2: "TRY",
            3: "JPY",
            4: "GBP",
            5: "AUD",
            6: "CHF",
            7: "CAD",
            8: "CNY",
            9: "HKD",
            10: "NZD",
            11: "SEK",
            12: "KRW",
            13: "SGD",
            14: "MXN",
            15: "INR",
            16: "RUB",
            17: "ZAR",
            18: "BRL",
            19: "TWD",
            20: "DKK",
            21: "PLN",
            22: "THB",
            23: "IDR",
            24: "HUF",
            25: "CZK",
            26: "ILS",
            27: "CLP",
            28: "PHP",
            29: "AED",
            30: "SAR",
            31: "MYR",
            32: "ARS",
            33: "COP",
            34: "PEN",
            35: "VND",
            36: "NGN",
            37: "EGP",
            38: "PKR",
            39: "KWD",
            40: "BDT",
            41: "QAR",
            42: "OMR",
            43: "MAD",
            44: "RON",
            45: "BGN"
        }
        from_1 = self.ui.comboBox_5.currentText()
        for i in range(0,self.ui.tableWidget.rowCount()):
            to_1 = currency_dict[i]
            total = self.conventer(from_1, to_1,1)
            self.ui.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(total))
    def swap(self):
        from_1_combobox = self.ui.comboBox_4.currentText()
        to_1_combobox = self.ui.comboBox_6.currentText()
        index_from = self.ui.comboBox_6.findText(from_1_combobox)
        index_to = self.ui.comboBox_4.findText(to_1_combobox)
        if index_from !=-1 and index_to!=-1:
            self.ui.comboBox_6.setCurrentIndex(index_from)
            self.ui.comboBox_4.setCurrentIndex(index_to)
    def update_api(self):
        self.connection()
        if self.ui.label_7.text()=="Successfully Connected to API":
            self.ui.label_7.setText("UPDATE API")
            self.table_widget()
    def copy_total(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.total)

    def download(self):
        username = os.getenv("USERNAME") or os.getenv("USER")
        with open(f"/home/{username}/Downloads/history_page.txt","w") as config:
            for i in range(self.ui.tableWidget_2.rowCount()):
                rows = ""
                for j in range(self.ui.tableWidget_2.columnCount()):
                    rows =rows + str(self.ui.tableWidget_2.item(i,j).text())+","
                config.write(rows+"\n")
    def api_load(self):
        self.api = self.ui.lineEdit_2.text()
        with open(".config", "w") as config:
            config.write(self.api+",")
            config.write(self.theme+",")
            config.write(str(self.number_1)+",")
        self.close()
    def clear_notes(self):
        self.ui.textEdit.clear()
    def clear_api(self):
        self.ui.lineEdit_2.clear()
    def fixer(self):
        url ="https://fixer.io/"
        webbrowser.open(url)
    def github(self):
        url = "https://github.com/devrim-1283"
        webbrowser.open(url)
    def linkedin(self):
        url = "https://www.linkedin.com/in/devrim-tun%C3%A7er-218a55320/"
        webbrowser.open(url)
    def dark(self):
        dark_stylesheet = ("""
        QWidget {
            background-color: #121212;
            color: #FFFFFF;
        }
        QPushButton {
            background-color: #333333;
            color: #FFFFFF;
            border: 1px solid #444;
        }
        QPushButton:hover {
            background-color: #444;
        }
        QLabel {
            color: #FFFFFF;
        }
        QLineEdit {
            background-color: #1E1E1E;
            color: #FFFFFF;
            padding: 5px;
        }
        QTextEdit {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        QTableWidget {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        QTableWidget QHeaderView::section {
            background-color: #222222;
            padding: 4px;
        }
        QComboBox {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        QComboBox QAbstractItemView {
            background-color: #252525;
            color: #FFFFFF;
        }
        QMenuBar {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        QMenu {
            background-color: #1E1E1E;
        }
        QStatusBar {
            background-color: #121212;
            color: #FFFFFF;
        }
    """)
        self.setStyleSheet(dark_stylesheet)
        with open(f"{self.exec_file}.config","r+") as config:
            content = config.read().split(",")
            content[1] = "Dark"
            config.seek(0)
            for i in content:
                config.write(i+",")
    def default(self):
        default_stylesheet = """
        QWidget {
            background-color: #FFFFFF;
            color: #000000;
        }
        QPushButton {
            background-color: #F0F0F0;
            color: #000000;
            padding: 5px;
            border: 1px solid #CCCCCC;
        }
        QPushButton:hover {
            background-color: #E0E0E0;
        }
        QLabel {
            color: #000000;
        }
        QLineEdit {
            background-color: #FFFFFF;
            color: #000000;
            padding: 5px;
        }
        QTextEdit {
            background-color: #FFFFFF;
            color: #000000;
        }
        QTableWidget {
            background-color: #FFFFFF;
            color: #000000;
        }
        QTableWidget QHeaderView::section {
            background-color: #E0E0E0;
            padding: 4px;
        }
        QComboBox {
            background-color: #FFFFFF;
            color: #000000;
        }
        QComboBox QAbstractItemView {
            background-color: #FFFFFF;
            color: #000000;
        }
        QMenuBar {
            background-color: #F0F0F0;
            color: #000000;
        }
        QMenu {
            background-color: #FFFFFF;
        }
        QStatusBar {
            background-color: #F0F0F0;
            color: #000000;
        }
    """
        self.setStyleSheet(default_stylesheet)
        with open(f"{self.exec_file}.config","r+") as config:
            content = config.read().split(",")
            content[1] = "Default"
            config.seek(0)
            for i in content:
                config.write(i+",")
    def theme_default(self):
        with open(f"{self.exec_file}.config","r+") as config:
            content = config.read().split(",")
            if content[1] == "Default":
                self.default()
            if content[1] == "Dark":
                self.dark()




app = QtWidgets.QApplication(sys.argv)
window = main_window()
sys.exit(app.exec_())
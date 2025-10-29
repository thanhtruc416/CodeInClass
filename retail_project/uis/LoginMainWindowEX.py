from PyQt6.QtWidgets import QMessageBox, QMainWindow
from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.uis import EmployeeMainWindowEx
from retail_project.uis.EmployeeMainWindowEx import EmployeeMainWindow

from retail_project.uis.LoginMainWindow import Ui_MainWindow


class LoginMainWindowEX(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)  # Sửa click -> clicked

    def process_login(self):
        email = self.lineEditEmail.text()
        password = self.lineEditPassword.text()

        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email, password)

        msg = QMessageBox()
        if em is None:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed, please try again")
            msg.setWindowTitle("Login Failed")
            msg.exec()
        else:
            self.gui_emp=EmployeeMainWindow()
            self.gui_emp.setupUi(QMainWindow())
            self.gui_emp.showWindow()
            self.MainWindow.close()


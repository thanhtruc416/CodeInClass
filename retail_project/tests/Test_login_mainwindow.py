from PyQt6.QtWidgets import QApplication, QMainWindow

from retail_project.uis.LoginMainWindowEX import LoginMainWindowEX

app=QApplication([])
login_ui=LoginMainWindowEX()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()
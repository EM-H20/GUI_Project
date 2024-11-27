import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\coding_File\\vscode\\GUI_Project\\HolyView.ui")[0]

#=========================================   class 부분  =========================================
class WindowClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#======================================   Signal & Setting 부분   =================================
        self.show_button.clicked.connect(self.button_show)

#========================================   slot 실행부분    ========================================
    def button_show(self):
        print("show")

#========================================   app 실행부분    ========================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = WindowClass()
    mainWindow.show()
    sys.exit(app.exec_())

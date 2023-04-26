from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from NFA_to_DFA import HomeScreen


class User_Manual(QMainWindow):
    def __init__(self):
        super(User_Manual,self).__init__()
        uic.loadUi("User_Manual.ui",self)
        self.show()        



app=QApplication(sys.argv)
home= HomeScreen()
User_Manual_Window=User_Manual()
app.exec_()


##app = QApplication(sys.argv)
##home = HomeScreen()
##home.show()
##app.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5 import uic


class User_Manual(QMainWindow):
    def __init__(self):
        super(User_Manual,self).__init__()
        uic.loadUi("User_Manual.ui",self)
        self.show()        




from PyQt5.QtWidgets import *
from PyQt5 import uic


class User_Manual(QMainWindow):

    def __init__(self) -> None:
        """
        function to show the User instructions on entering the NFA_to_DFA page
        """
        super(User_Manual, self).__init__()
        uic.loadUi("../UI/User_Manual.ui", self)
        self.show()

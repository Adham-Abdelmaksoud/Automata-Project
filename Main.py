from User_Manual import User_Manual
from NFA_to_DFA import HomeScreen
from PyQt5.QtWidgets import *
import sys

def main():
    app=QApplication(sys.argv)
    home= HomeScreen()
    User_Manual_Window=User_Manual()
    app.exec_()

if __name__ == "__main__":
    main()
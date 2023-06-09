from util import *
from NFA_to_DFA import NFAtoDFA
from CFG_to_PDA import CFGtoPDA
from User_Manual import User_Manual


class Home(QMainWindow):
    def __init__(self) -> None:
        """
        init the main window for the gui

        """
        super(Home, self).__init__()
        uic.loadUi('../UI/Home.ui', self)
        # searching for the buttons by ID and referencing them
        self.btn1 = self.findChild(QPushButton, 'NFA_to_DFA_btn')
        self.btn2 = self.findChild(QPushButton, 'CFG_to_PDA_btn')

        # assign event listeners when the button is clicked to excute a function
        self.btn1.clicked.connect(self.gotoNFAtoDFA)
        self.btn2.clicked.connect(self.gotoCFGtoPDA)

    def gotoNFAtoDFA(self) -> None:
        """when button1 is clicked change the Home window to the NFA_to_DFA window
        """
        sceneStack_Manuals.setCurrentIndex(0)
        sceneStack_Manuals.show()
        sceneStack.resize(1029, 973)
        sceneStack.setCurrentIndex(1)

    def gotoCFGtoPDA(self) -> None:
        """when button2 is clicked change the Home window to the CFG_to_PDA window
        """
        sceneStack.resize(1100, 650)
        sceneStack.setCurrentIndex(2)


def main():
    home = Home()
    nfatodfa = NFAtoDFA()
    cfgtopda = CFGtoPDA()
    NFAusermanual = User_Manual()

    sceneStack.addWidget(home)
    sceneStack.addWidget(nfatodfa)
    sceneStack.addWidget(cfgtopda)

    sceneStack.setMinimumWidth(875)
    sceneStack.setMinimumHeight(540)
    sceneStack.resize(875, 540)
    sceneStack.show()

    sceneStack_Manuals.addWidget(NFAusermanual)
    sceneStack_Manuals.resize(860, 800)
    sceneStack_Manuals.setFixedWidth(860)
    sceneStack_Manuals.setFixedHeight(800)

    app.exec_()


if __name__ == '__main__':
    main()

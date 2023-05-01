from util import *
from NFA_to_DFA import NFAtoDFA
from CFG_to_PDA import CFGtoPDA

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('UI/Home.ui', self)

        self.btn1 = self.findChild(QPushButton, 'NFA_to_DFA_btn')
        self.btn2 = self.findChild(QPushButton, 'CFG_to_PDA_btn')

        self.btn1.clicked.connect(self.gotoNFAtoDFA)
        self.btn2.clicked.connect(self.gotoCFGtoPDA)

    def gotoNFAtoDFA(self):
        sceneStack.setFixedWidth(1100)
        sceneStack.setFixedHeight(800)
        sceneStack.setCurrentIndex(1)

    def gotoCFGtoPDA(self):
        sceneStack.setFixedWidth(1100)
        sceneStack.setFixedHeight(650)
        sceneStack.setCurrentIndex(2)

def main():
    home = Home()
    nfatodfa = NFAtoDFA()
    cfgtopda = CFGtoPDA()

    sceneStack.addWidget(home)
    sceneStack.addWidget(nfatodfa)
    sceneStack.addWidget(cfgtopda)

    sceneStack.setFixedWidth(875)
    sceneStack.setFixedHeight(540)
    sceneStack.show()

    app.exec_()

if __name__ == '__main__':
    main()
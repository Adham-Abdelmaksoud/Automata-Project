from util import *

class CFGtoPDA(QMainWindow):
    def __init__(self):
        super(CFGtoPDA, self).__init__()
        uic.loadUi('../UI/CFG_to_PDA.ui', self)

        self.PDA_Widget = self.findChild(QWidget, 'PDA_Widget')
        self.back_btn = self.findChild(QPushButton, 'back_btn')

        self.PDA_viz = gv.Digraph()
        self.PDA_lbl = QLabel(self)

        self.PDA_viz.node('', shape='none')
        self.PDA_layout = QVBoxLayout(self.PDA_Widget)

        self.convertBtn.clicked.connect(self.convert)
        self.back_btn.clicked.connect(self.goback)


    def goback(self):
        sceneStack.resize(875, 540)
        sceneStack.setCurrentIndex(0)
        sceneStack_Manuals.close()
    

    def plot(self, imgName, graph_viz, layout, label):
        self.layout = layout
        self.layout.addWidget(label, alignment=Qt.AlignCenter)
        graph_viz.format = 'png'
        graph_viz.render(imgName, view = False)
        aspectResize(imgName+'.png', self.PDA_Widget.width(), self.PDA_Widget.height())
        pixmap = QPixmap(imgName+'.png')
        label.setPixmap(pixmap)


    def convert(self):
        pass
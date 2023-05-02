from util import *

class CFGtoPDA(QMainWindow):
    def __init__(self):
        super(CFGtoPDA, self).__init__()
        uic.loadUi('../UI/CFG_to_PDA.ui', self)

        self.startSymbol_txt = self.findChild(QLineEdit, 'startSymbol_txt')
        self.terminalSymbols_txt = self.findChild(QLineEdit, 'terminalSymbols_txt')
        self.CFG_txt = self.findChild(QTextEdit, 'CFG_txt')
        self.PDA_output = self.findChild(QTextEdit, 'PDA_output')
        self.convert_btn = self.findChild(QPushButton, 'convert_btn')
        self.back_btn = self.findChild(QPushButton, 'back_btn')

        self.PDA_viz = gv.Digraph()
        self.PDA_lbl = QLabel(self)
        self.PDA_layout = QVBoxLayout(self.PDA_Widget)

        self.convert_btn.clicked.connect(self.convert)
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

    def getStateNum(self, rule):
        stateStr = rule[3]
        for i in range(3, len(rule)):
            if rule[i] == ',':
                break
            else:
                stateStr += rule[i]
        return int(stateStr)

    def convert(self):
        self.startSymbol = self.startSymbol_txt.text()
        self.terminalSymbols = self.terminalSymbols_txt.text().split(',')
        self.CFGrules = self.CFG_txt.toPlainText().split('\n')

        self.PDA_viz = gv.Digraph()

        transitions = []
        transitions.append(
            'δ(q1, ε, ε) = {(q2, $)}'
        )
        transitions.append(
            f'δ(q2, ε, ε) = {{(q3, {self.startSymbol})}}'
        )

        stateCounter = 3

        for terminal in self.terminalSymbols:
            transitions.append(
                f'δ(q3, {terminal}, {terminal}) = {{(q3, ε)}}'
            )

        for rule in self.CFGrules:
            if rule == '':
                continue
            rule = rule.replace(' ', '')
            start, allProduced = rule.split('->')
            for produced in allProduced.split('|'):
                if produced == 'eps':
                    produced = 'ε'
                isFirstChar = True
                charCounter = 0
                for char in produced[::-1]:
                    charCounter += 1
                    if charCounter == len(produced):
                        transitions.append(
                            f'δ(q{stateCounter}, ε, ε) = {{(q3, {char})}}'
                        )
                        break
                    if(isFirstChar):
                        transitions.append(
                            f'δ(q3, ε, {start}) = {{(q{stateCounter+1}, {char})}}'
                        )
                        isFirstChar = False
                    else:
                        transitions.append(
                            f'δ(q{stateCounter}, ε, ε) = {{(q{stateCounter+1}, {char})}}'
                        )
                    stateCounter += 1

        transitions.append(
            f'δ(q3, ε, $) = {{(q{stateCounter+1}, ε)}}'
        )

        transitions.sort(key=self.getStateNum)
        transitions = "\n".join(transitions)
        self.PDA_output.setPlainText(transitions)
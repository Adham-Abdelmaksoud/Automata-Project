from util import *

class CFGtoPDA(QMainWindow):
    def __init__(self):
        super(CFGtoPDA, self).__init__()
        uic.loadUi('../UI/CFG_to_PDA.ui', self)

        self.PDA_Widget = self.findChild(QWidget, 'PDA_Widget')
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

        transitions = []
        transitions.append(
            'δ(q1, ε, ε) = {(q2, $)}'
        )
        self.PDA_viz.node('',shape='none')
        self.PDA_viz.node('q1',shape='circle')
        self.PDA_viz.edge('','q1',constraint='false')
        self.PDA_viz.node('q2',shape='circle')
        self.PDA_viz.edge('q1', 'q2',label='ε,ε->$',constraint='false')

        transitions.append(
            f'δ(q2, ε, ε) = {{(q3, {self.startSymbol})}}'
        )
        self.PDA_viz.node('q3', shape='circle')
        self.PDA_viz.edge('q2', 'q3', label=f'ε,ε->{self.startSymbol}',constraint='false')

        stateCounter = 3

        for terminal in self.terminalSymbols:
            transitions.append(
                f'δ(q3, {terminal}, {terminal}) = {{(q3, ε)}}'
            )
            self.PDA_viz.edge('q3','q3',label=f'{terminal},{terminal}->ε',constraint='false')

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
                        self.PDA_viz.node(f'q{stateCounter}',shape='circle')
                        self.PDA_viz.edge(f'q{stateCounter}', 'q3', label=f'ε,ε->{char}',constraint='false')

                        break
                    if(isFirstChar):
                        transitions.append(
                            f'δ(q3, ε, {start}) = {{(q{stateCounter+1}, {char})}}'
                        )
                        self.PDA_viz.node(f'q{stateCounter+1}', shape='circle')
                        self.PDA_viz.edge(f'q3', f'q{stateCounter+1}', label=f'ε,{start}->{char}',constraint='false')
                        isFirstChar = False
                    else:
                        transitions.append(
                            f'δ(q{stateCounter}, ε, ε) = {{(q{stateCounter+1}, {char})}}'
                        )
                        self.PDA_viz.node(f'q{stateCounter+1}', shape='circle')
                        self.PDA_viz.edge(f'q{stateCounter}', f'q{stateCounter+1}', label=f'ε,ε->{char}',constraint='false')

                    stateCounter += 1

        transitions.append(
            f'δ(q3, ε, $) = {{(q{stateCounter+1}, ε)}}'
        )
        self.PDA_viz.node(f'q{stateCounter+1}', shape='doublecircle')
        self.PDA_viz.edge(f'q3', f'q{stateCounter + 1}', label='ε,$->ε',constraint='false')



        # GRAPH
        # | | |
        # v v v
        self.PDA_viz = gv.Digraph()
        self.PDA_viz.node('', shape='none')

        self.PDA_viz.node('q1', shape='circle')
        self.PDA_viz.node('q2', shape='circle')
        self.PDA_viz.node('q3', shape='circle')
        self.PDA_viz.edge('', 'q1')
        self.PDA_viz.edge('q1', 'q2', label='ε/ε/$')
        self.PDA_viz.edge('q2', 'q3', label='ε/ε/'+self.startSymbol)

        stateCounter = 3

        for terminal in self.terminalSymbols:
            self.PDA_viz.edge('q3', 'q3', label=f'{terminal}/{terminal}/ε')

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
                        self.PDA_viz.edge(
                            f'q{stateCounter}',
                            'q3',
                            label=f'ε/ε/{char}'
                        )
                        break
                    self.PDA_viz.node(f'q{stateCounter+1}', shape='circle')
                    if(isFirstChar):
                        self.PDA_viz.edge(
                            'q3',
                            f'q{stateCounter+1}',
                            label=f'ε/{start}/{char}'
                        )
                        isFirstChar = False
                    else:
                        self.PDA_viz.edge(
                            f'q{stateCounter}',
                            f'q{stateCounter+1}',
                            label=f'ε/ε/{char}'
                        )
                    stateCounter += 1

        self.PDA_viz.node(f'q{stateCounter+1}', shape='doublecircle')
        self.PDA_viz.edge('q3', f'q{stateCounter+1}', label='ε/$/ε')

        self.plot('PDA', self.PDA_viz, self.PDA_layout, self.PDA_lbl)
        # ^ ^ ^
        # | | |
        # GRAPH

        

        transitions.sort(key=self.getStateNum)
        transitions = "\n".join(transitions)
        self.PDA_output.setPlainText(transitions)
        self.PDA_viz.format = 'pdf'
        self.PDA_viz.render('CFG', view=True)
        # u=self.PDA_viz.unflatten(stagger=10)
        # u.render('CFG', view=True)

import networkx as nx

from util import *

class NFAtoDFA(QMainWindow):
    def __init__(self):
        super(NFAtoDFA, self).__init__()
        uic.loadUi('../UI/edited_NFA_to_DFA.ui', self)
        self.show()
        self.lastRand = 0

        self.NFA_Widget = self.findChild(QWidget, 'NFA_Widget')
        self.DFA_Widget = self.findChild(QWidget, 'DFA_Widget')
        self.fromNodeTxt = self.findChild(QLineEdit, 'fromNodeTxt')
        self.toNodeTxt = self.findChild(QLineEdit, 'toNodeTxt')
        self.edgeLabelTxt = self.findChild(QLineEdit, 'edgeLabelTxt')
        self.convertBtn = self.findChild(QPushButton, 'convertBtn')
        self.backbtn = self.findChild(QPushButton,'backbtn')
        self.addEdgeBtn = self.findChild(QPushButton, 'addEdgeBtn')
        self.generateBtn = self.findChild(QPushButton, 'generateGraphBtn')
        self.clearBtn = self.findChild(QPushButton, 'clearGraphBtn')
        self.fromIsInitial = self.findChild(QCheckBox, 'initial1')
        self.toIsInitial = self.findChild(QCheckBox, 'initial2')
        self.fromIsFinal = self.findChild(QCheckBox, 'final1')
        self.toIsFinal = self.findChild(QCheckBox, 'final2')
        self.error_empty_fields = self.findChild(QLabel,'error_empty_fields')
        self.star_from_node = self.findChild(QLabel, 'star_from_node')
        self.star_to_node = self.findChild(QLabel, 'star_to_node')
        self.star_transition_edge = self.findChild(QLabel, 'star_transition_edge')

        self.NFA = nx.DiGraph()
        self.DFA = nx.DiGraph()
        self.NFA_viz = gv.Digraph()
        self.DFA_viz = gv.Digraph()
        self.NFA_lbl = QLabel(self)
        self.DFA_lbl = QLabel(self)

        self.NFA_viz.node('', shape='none')
        self.NFA_layout = QVBoxLayout(self.NFA_Widget)
        self.DFA_layout = QVBoxLayout(self.DFA_Widget)

        self.addEdgeBtn.clicked.connect(self.addEdge)
        self.convertBtn.clicked.connect(self.convert)
        self.generateBtn.clicked.connect(self.generateGraph)
        self.clearBtn.clicked.connect(self.clear)
        self.backbtn.clicked.connect(self.goback)

    def goback(self):
        sceneStack.resize(875, 540)
        sceneStack.setCurrentIndex(0)
        sceneStack_Manuals.close()

    def generateGraph(self):
        self.NFA_viz = gv.Digraph()
        self.NFA_viz.node('', shape='none')

        graph1 = nx.DiGraph()
        graph1.add_edge('q0','q0', label='0')
        graph1.add_edge('q0','q1', label='0,1')
        graph1.add_edge('q1','q0', label='1')
        graph1.add_edge('q1','q1', label='1')
        for node in graph1.nodes:
            graph1.nodes[node]['initial'] = False
            graph1.nodes[node]['final'] = False
        graph1.nodes['q0']['initial'] = True
        graph1.nodes['q1']['final'] = True

        graph2 = nx.DiGraph()
        graph2.add_edge('q0','q0', label='0')
        graph2.add_edge('q0','q1', label='1')
        graph2.add_edge('q1','q1', label='0,1')
        graph2.add_edge('q1','q2', label='0')
        graph2.add_edge('q2','q1', label='1')
        graph2.add_edge('q2','q2', label='0,1')
        for node in graph2.nodes:
            graph2.nodes[node]['initial'] = False
            graph2.nodes[node]['final'] = False
        graph2.nodes['q0']['initial'] = True
        graph2.nodes['q2']['final'] = True

        graph3 = nx.DiGraph()
        graph3.add_edge('1','2', label='eps')
        graph3.add_edge('1','4', label='eps')
        graph3.add_edge('2','3', label='a')
        graph3.add_edge('3','2', label='eps')
        graph3.add_edge('3','4', label='eps')
        graph3.add_edge('4','5', label='eps')
        graph3.add_edge('4','6', label='eps')
        graph3.add_edge('5','7', label='a')
        graph3.add_edge('6','8', label='b')
        graph3.add_edge('7','9', label='eps')
        graph3.add_edge('8','9', label='eps')
        for node in graph3.nodes:
            graph3.nodes[node]['initial'] = False
            graph3.nodes[node]['final'] = False
        graph3.nodes['1']['initial'] = True
        graph3.nodes['9']['final'] = True

        graph4 = nx.DiGraph()
        graph4.add_edge('1','2', label='eps')
        graph4.add_edge('1','3', label='eps')
        graph4.add_edge('1','4', label='eps')
        graph4.add_edge('2','5', label='a')
        graph4.add_edge('3','6', label='b')
        graph4.add_edge('4','7', label='a')
        graph4.add_edge('7','8', label='b')
        graph4.add_edge('5','9', label='eps')
        graph4.add_edge('6','9', label='eps')
        graph4.add_edge('8','9', label='eps')
        for node in graph4.nodes:
            graph4.nodes[node]['initial'] = False
            graph4.nodes[node]['final'] = False
        graph4.nodes['1']['initial'] = True
        graph4.nodes['9']['final'] = True

        graph5 = nx.DiGraph()
        graph5.add_edge('q0','q1', label='1')
        graph5.add_edge('q0','q2', label='eps')
        graph5.add_edge('q1','q0', label='0')
        graph5.add_edge('q1','q2', label='0,1')
        for node in graph5.nodes:
            graph5.nodes[node]['initial'] = False
            graph5.nodes[node]['final'] = False
        graph5.nodes['q0']['initial'] = True
        graph5.nodes['q0']['final'] = True

        graph6 = nx.DiGraph()
        graph6.add_edge('q0','q1', label='eps')
        graph6.add_edge('q0','q2', label='eps')
        graph6.add_edge('q1','q0', label='eps')
        graph6.add_edge('q2','q6', label='eps')
        graph6.add_edge('q2','q4', label='eps')
        graph6.add_edge('q6','q7', label='b')
        graph6.add_edge('q4','q5', label='a')
        graph6.add_edge('q5','q3', label='eps')
        graph6.add_edge('q7','q3', label='eps')
        graph6.add_edge('q3','q1', label='eps')
        for node in graph6.nodes:
            graph6.nodes[node]['initial'] = False
            graph6.nodes[node]['final'] = False
        graph6.nodes['q0']['initial'] = True
        graph6.nodes['q1']['final'] = True


        graphs = [graph1, graph2, graph3, graph4, graph5, graph6]
        rand = int(random()*len(graphs))
        while rand == self.lastRand:
            rand = int(random()*len(graphs))
        self.lastRand = rand
        self.NFA = graphs[rand]

        self.fromNXtoGV(self.NFA, self.NFA_viz)
        self.plot('NFA', self.NFA_viz, self.NFA_layout, self.NFA_lbl)

    def clear(self):
        self.NFA = nx.DiGraph()
        self.NFA_viz = gv.Digraph()
        self.NFA_viz.node('', shape='none')
        self.plot('NFA', self.NFA_viz, self.NFA_layout, self.NFA_lbl)
        self.clearStarFields()
        
        ## Engy: I made the clear button clears both graphs ## 
        self.DFA = nx.DiGraph()
        self.DFA_viz = gv.Digraph()
        self.DFA_viz.node('', shape='none')
        self.plot('DFA', self.DFA_viz, self.DFA_layout, self.DFA_lbl)
        ## ##

    def plot(self, imgName, graph_viz, layout, label):
        self.layout = layout
        self.layout.addWidget(label, alignment=Qt.AlignCenter)
        graph_viz.format = 'png'
        graph_viz.render(imgName, view=False)
        aspectResize(imgName+'.png', self.NFA_Widget.width(),
                     self.NFA_Widget.height())
        pixmap = QPixmap(imgName+'.png')
        label.setPixmap(pixmap)

    def fromNXtoGV(self, graph, graph_viz):
        labels = nx.get_edge_attributes(graph, 'label')
        isInitialSet = False
        for edge in graph.edges:
            if (graph.nodes[edge[0]]['final']):
                graph_viz.node(edge[0], shape='doublecircle')
            else:
                graph_viz.node(edge[0], shape='circle')
            if (graph.nodes[edge[1]]['final']):
                graph_viz.node(edge[1], shape='doublecircle')
            else:
                graph_viz.node(edge[1], shape='circle')

            if (not isInitialSet and graph.nodes[edge[0]]['initial']):
                isInitialSet = True
                graph_viz.edge('', edge[0])
            if (not isInitialSet and graph.nodes[edge[1]]['initial']):
                isInitialSet = True
                graph_viz.edge('', edge[1])
            if labels[edge]=='eps':
                graph_viz.edge(edge[0], edge[1], label='ε')
            else:
                graph_viz.edge(edge[0], edge[1], label=labels[edge])

    def addEdge(self):
        emptyField = False
        fromNode = self.fromNodeTxt.text()
        toNode = self.toNodeTxt.text()
        edgeLbl = self.edgeLabelTxt.text()



        if fromNode=='':
            emptyField=True
            self.star_from_node.setText('*')
        else:
            self.star_from_node.setText('')

        if toNode=='':
            emptyField = True
            self.star_to_node.setText('*')
        else:
            self.star_to_node.setText('')

        if edgeLbl=='':
            emptyField = True
            self.star_transition_edge.setText('*')
        else:
            self.star_transition_edge.setText('')

        if emptyField:
            self.error_empty_fields.setText('Please Fill Empty Fields')
            return


        if self.toIsInitial.isChecked() and self.fromIsInitial.isChecked():
            self.errorMessage('Error', 'NFA can have only one initial state')
            self.clearStarFields()
            return

        if self.fromIsInitial.isChecked():
            if fromNode in nx.nodes(self.NFA):
                if self.NFA.nodes[fromNode]['initial']:
                    pass
                else:
                    for node in nx.nodes(self.NFA):
                        if self.NFA.nodes[node]['initial']:
                            self.errorMessage('Error', 'NFA can have only one initial state')
                            self.clearStarFields()
                            return
            else:
                for node in nx.nodes(self.NFA):
                    if self.NFA.nodes[node]['initial']:
                        self.errorMessage('Error', 'NFA can have only one initial state')
                        self.clearStarFields()
                        return


        if self.toIsInitial.isChecked():
            if toNode in nx.nodes(self.NFA):
                if self.NFA.nodes[toNode]['initial']:
                    pass
                else:
                    for node in nx.nodes(self.NFA):
                        if self.NFA.nodes[node]['initial']:
                            self.errorMessage('Error', 'NFA can have only one initial state')
                            self.clearStarFields()
                            return
            else:
                for node in nx.nodes(self.NFA):
                    if self.NFA.nodes[node]['initial']:
                        self.errorMessage('Error', 'NFA can have only one initial state')
                        self.clearStarFields()
                        return



        if (fromNode != '' and toNode != ''):
            self.NFA.add_edge(fromNode, toNode, label=edgeLbl)
            self.clearStarFields()


        if (self.fromIsFinal.isChecked()):
            self.NFA.nodes[fromNode]['final'] = True

        else:
            self.NFA.nodes[fromNode]['final'] = False

        if (self.fromIsInitial.isChecked()):
            self.NFA.nodes[fromNode]['initial'] = True

        else:
            self.NFA.nodes[fromNode]['initial'] = False

        if (self.toIsFinal.isChecked()):
            self.NFA.nodes[toNode]['final'] = True

        else:
            self.NFA.nodes[toNode]['final'] = False

        if (self.toIsInitial.isChecked()):
            self.NFA.nodes[toNode]['initial'] = True

        else:
            self.NFA.nodes[toNode]['initial'] = False

        self.NFA_viz = gv.Digraph()
        self.NFA_viz.node('', shape='none')
        self.fromNXtoGV(self.NFA, self.NFA_viz)
        self.plot('NFA', self.NFA_viz, self.NFA_layout, self.NFA_lbl)
        self.fromNodeTxt.setText('')
        self.toNodeTxt.setText('')
        self.edgeLabelTxt.setText('')

    def markInitialAndFinal(self, initial):
        for nodeStr in self.DFA.nodes:
            # mark initial nodes
            if nodeStr == initial:
                self.DFA.nodes[nodeStr]['initial'] = True
            else:
                self.DFA.nodes[nodeStr]['initial'] = False
            nodeList = nodeStr.split(',')

            # mark final nodes
            self.DFA.nodes[nodeStr]['final'] = False
            if nodeStr == 'rej':
                continue
            for node in nodeList:
                if self.NFA.nodes[node]['final']:
                    self.DFA.nodes[nodeStr]['final'] = True
                    break

    def addEpsilonTransitions(self, nodeList, visited):
        nodeSet = set(nodeList)
        for node in nodeList:
            if node not in visited:
                visited.append(node)
                epsDstNodes = self.NFA.nodes[node]['eps']
                if len(epsDstNodes) != 0:
                    nodeSet = nodeSet.union(epsDstNodes)
                    nodeSet = self.addEpsilonTransitions(list(nodeSet), visited)
        return nodeSet

    def getNextNodeSet(self, nodeList, alpha, isEpsilonNFA):
        nextNodeSet = set()
        for node in nodeList:
            nextNodeSet = nextNodeSet.union(self.NFA.nodes[node][alpha])
        if isEpsilonNFA:
            visited = []
            nextNodeSet = self.addEpsilonTransitions(list(nextNodeSet), visited)
        return nextNodeSet

    def addTransitionTuple(self, alphabet, nodeList, visited, nodePattern):
        if nodeList[0] == 'rej':
            return
        for alpha in alphabet:
            # form the next node set
            if alpha == 'eps':
                continue
            nextNodeSet = self.getNextNodeSet(
                nodeList, alpha, 'eps' in alphabet)

            # form the next node list
            nextNodeList = []
            for node in nodePattern:
                if node in nextNodeSet:
                    nextNodeList.append(node)
            if len(nextNodeList) == 0:
                nextNodeList = ['rej']
            nextNodeStr = ",".join(nextNodeList)
            nodeStr = ",".join(nodeList)

            # add nodes to DFA
            self.DFA.add_nodes_from([nodeStr, nextNodeStr])
            if nextNodeStr in self.DFA.nodes[nodeStr].keys():
                self.DFA.nodes[nodeStr][nextNodeStr].add(alpha)
            else:
                self.DFA.nodes[nodeStr][nextNodeStr] = {alpha}

            # check if a node is visited
            if nextNodeList not in visited:
                visited.append(nextNodeList)
                self.addTransitionTuple(
                    alphabet, nextNodeList, visited, nodePattern)

    def optimizeDFA(self, alphabet, nodePattern):
        transitions = dict()
        edge_labels = nx.get_edge_attributes(self.DFA, 'label')

        # initialize the DFA transition table
        for node in self.DFA.nodes:
            transitions[node] = dict()

        # fill the DFA transition table
        for edge in self.DFA.edges:
            lbl_vals = edge_labels[edge].split(',')
            for lbl in lbl_vals:
                transitions[edge[0]][lbl] = edge[1]

        newClusters = [[], []]
        oldClusters = []
        # initialize the initial cluster
        for node in self.DFA.nodes:
            if self.DFA.nodes[node]['final']:
                newClusters[1].append(node)
            else:
                newClusters[0].append(node)
        remove = -1
        for i in range(2):
            if(len(newClusters[i]) == 0):
                remove = i
        if remove != -1:
            newClusters.pop(remove)

        # perform divisive clustering
        while(len(oldClusters)!=len(newClusters)):
            oldClusters = newClusters
            newClusters = []
            # for each cluster
            for oldCluster in oldClusters:
                # put a single node in the cluster
                if len(oldCluster) == 1:
                    newClusters.append(oldCluster)
                    continue
                newClusters.append([oldCluster[0]])
                
                # for each element in the cluster
                for element in oldCluster:
                    inCluster = False
                    # search for a new cluster to add the element
                    for i in range(len(newClusters)):
                        if newClusters[i][0] not in oldCluster:
                            continue
                        # if the element is already clustered
                        if element == newClusters[i][0]:
                            inCluster = True
                            break
                        # if the element has same transitions as any element in the new cluster
                        areSimilar = True
                        for alpha in alphabet:
                            dst1 = transitions[element][alpha]
                            dst2 = transitions[newClusters[i][0]][alpha]
                            for cluster in oldClusters:
                                if dst1 in cluster and dst2 not in cluster:
                                    areSimilar = False
                                    break
                            if not areSimilar:
                                break
                        # add the element in the suitable cluster
                        if areSimilar:
                            newClusters[i].append(element)
                            inCluster = True
                            break
                    # if no cluster is found for the element, create a new cluster
                    if not inCluster:
                        newClusters.append([element])
            
        self.DFA_optimized = nx.DiGraph()
        newNodes = []
        newTransitions = dict()

        for i in range(len(newClusters)):
            nodeSet = set()
            newTransitions[i] = dict()
            isInitial = False
            isFinal = False

            # create new transition table
            for element in newClusters[i]:
                for alpha in alphabet:
                    for j in range(len(newClusters)):
                        if transitions[element][alpha] in newClusters[j]:
                            if j in newTransitions[i].keys():
                                newTransitions[i][j].add(alpha)
                            else:
                                newTransitions[i][j] = {alpha}

                # mark initial and final nodes
                if self.DFA.nodes[element]['initial']:
                    isInitial = True
                if self.DFA.nodes[element]['final']:
                    isFinal = True

                brokenElement = element.split(',')
                for b in brokenElement:
                    nodeSet.add(b)

            # add all new nodes
            nodeList = []
            if 'rej' in nodeSet:
                nodeList = ['rej']
            else:
                for node in nodePattern:
                    if node in nodeSet:
                        nodeList.append(node)
            nodeStr = ",".join(nodeList)
            newNodes.append(nodeStr)
            self.DFA_optimized.add_node(nodeStr)
            
            # set initial and final nodes
            if isInitial:
                self.DFA_optimized.nodes[nodeStr]['initial'] = True
            else:
                self.DFA_optimized.nodes[nodeStr]['initial'] = False
            if isFinal:
                self.DFA_optimized.nodes[nodeStr]['final'] = True
            else:
                self.DFA_optimized.nodes[nodeStr]['final'] = False

        # add optimized DFA edges
        for i in newTransitions:
            for j in newTransitions[i]:
                self.DFA_optimized.add_edge(newNodes[i], newNodes[j], label=",".join(list(newTransitions[i][j])))

        self.DFA = self.DFA_optimized  

    def convert(self):
        initialFlag=False
        finalFlag=False
        if len(nx.nodes(self.NFA))==0:
            self.errorMessage('Error','Please enter your NFA')
            return

        for node in nx.nodes(self.NFA):
            if self.NFA.nodes[node]['initial']:
                initialFlag=True
            if self.NFA.nodes[node]['final']:
                finalFlag=True

        if not initialFlag:
            self.errorMessage('Error','NFA must have at least one initial state')
            return
        if not finalFlag:
            self.errorMessage('Error','NFA must have at least one final state')
            return


        edge_labels = nx.get_edge_attributes(self.NFA, 'label')

        # get the alphabet used by the NFA
        alphabet = set()
        for lbl in list(edge_labels.values()):
            lbl_vals = lbl.split(',')
            for val in lbl_vals:
                alphabet.add(val)
        alphabet = list(alphabet)

        # initialize output set of each transition and make the node formation pattern
        nodePattern = []
        for node in self.NFA.nodes:
            nodePattern.append(node)
            for alph in alphabet:
                self.NFA.nodes[node][alph] = set()

        # form an NFA transition table
        initialNode = None
        for edge in self.NFA.edges:
            if self.NFA.nodes[edge[0]]['initial']:
                initialNode = edge[0]
            lbl_vals = edge_labels[edge].split(',')
            for lbl in lbl_vals:
                self.NFA.nodes[edge[0]][lbl].add(edge[1])

        # for the initial node list
        initialNodeSet = {initialNode}
        if 'eps' in alphabet:
            visited = []
            initialNodeSet = self.addEpsilonTransitions(list(initialNodeSet), visited)
        initialNodeList = []
        for node in nodePattern:
            if node in initialNodeSet:
                initialNodeList.append(node)
        initialNodeStr = ",".join(initialNodeList)

        # initialize DFA
        self.DFA = nx.DiGraph()
        self.DFA_viz = gv.Digraph()
        self.DFA_viz.node('', shape='none')

        # traversing initializations
        visited = []
        self.DFA.add_node(initialNodeStr)

        # form the DFA transition table
        self.addTransitionTuple(alphabet, initialNodeList, visited, nodePattern)

        # mark initial and final nodes
        self.markInitialAndFinal(initialNodeStr)

        # add the DFA edges
        if 'eps' in alphabet:
            alphabet.remove('eps')
        for fromNode in self.DFA.nodes:
            if fromNode == 'rej':
                self.DFA.add_edge('rej', 'rej', label=",".join(alphabet))
            else:
                for toNode in self.DFA.nodes[fromNode]:
                    if toNode != 'initial' and toNode != 'final':
                        self.DFA.add_edge(fromNode, toNode, label=",".join(
                            list(self.DFA.nodes[fromNode][toNode])))

        # display the DFA
        self.optimizeDFA(alphabet, nodePattern)
        self.fromNXtoGV(self.DFA, self.DFA_viz)
        self.plot('DFA', self.DFA_viz, self.DFA_layout, self.DFA_lbl)

    def errorMessage(self,title,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def clearStarFields(self):
        self.star_from_node.setText('')
        self.star_to_node.setText('')
        self.star_transition_edge.setText('')
        self.error_empty_fields.setText('')



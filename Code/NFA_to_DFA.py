import networkx as nx
from graphgenerator import generateRandom_graph
from util import *


class NFAtoDFA(QMainWindow):
    def __init__(self):
        """initialize the Qt window to show the GUI for the NFA to DFA 
        """
        super(NFAtoDFA, self).__init__()
        # fetch and load ui file
        uic.loadUi('../UI/edited_NFA_to_DFA.ui', self)
        self.show()
        # index of the last random generated graph
        self.lastRand = 0
        # find childreen by ID and assign a reference in order to use them in the python file
        self.NFA_Widget = self.findChild(QWidget, 'NFA_Widget')
        self.DFA_Widget = self.findChild(QWidget, 'DFA_Widget')
        self.fromNodeTxt = self.findChild(QLineEdit, 'fromNodeTxt')
        self.toNodeTxt = self.findChild(QLineEdit, 'toNodeTxt')
        self.edgeLabelTxt = self.findChild(QLineEdit, 'edgeLabelTxt')
        self.convertBtn = self.findChild(QPushButton, 'convertBtn')
        self.backbtn = self.findChild(QPushButton, 'backbtn')
        self.addEdgeBtn = self.findChild(QPushButton, 'addEdgeBtn')
        self.generateBtn = self.findChild(QPushButton, 'generateGraphBtn')
        self.clearBtn = self.findChild(QPushButton, 'clearGraphBtn')
        self.fromIsInitial = self.findChild(QCheckBox, 'initial1')
        self.toIsInitial = self.findChild(QCheckBox, 'initial2')
        self.fromIsFinal = self.findChild(QCheckBox, 'final1')
        self.toIsFinal = self.findChild(QCheckBox, 'final2')
        self.error_empty_fields = self.findChild(QLabel, 'error_empty_fields')
        self.star_from_node = self.findChild(QLabel, 'star_from_node')
        self.star_to_node = self.findChild(QLabel, 'star_to_node')
        self.star_transition_edge = self.findChild(
            QLabel, 'star_transition_edge')
        self.NFA = nx.DiGraph()
        self.DFA = nx.DiGraph()
        self.NFA_viz = gv.Digraph()
        self.DFA_viz = gv.Digraph()
        self.NFA_lbl = QLabel(self)
        self.DFA_lbl = QLabel(self)
        self.NFA_viz.node('', shape='none')
        self.NFA_layout = QVBoxLayout(self.NFA_Widget)
        self.DFA_layout = QVBoxLayout(self.DFA_Widget)
        # assign some event listeners to excute some functions when cliked
        self.addEdgeBtn.clicked.connect(self.addEdge)
        self.convertBtn.clicked.connect(self.convert)
        self.generateBtn.clicked.connect(self.generateGraph)
        self.clearBtn.clicked.connect(self.clear)
        self.backbtn.clicked.connect(self.goback)

    def goback(self):
        """function used to change scene to the index window
        """
        sceneStack.resize(875, 540)
        sceneStack.setCurrentIndex(0)
        sceneStack_Manuals.close()

    def generateGraph(self):
        """for easy testing we created ready to use graphs that show by a click of button
        """
        self.NFA_viz = gv.Digraph()
        self.NFA_viz.node('', shape='none')
        graph, graphindex = generateRandom_graph(self.lastRand)

        self.NFA = graph
        self.lastRand = graphindex

        self.fromNXtoGV(self.NFA, self.NFA_viz)
        self.plot('NFA', self.NFA_viz, self.NFA_layout, self.NFA_lbl)

    def clear(self):
        """clear all input field,warning, and graphs in the page
        """
        # create empty graphs
        self.NFA = nx.DiGraph()
        self.DFA = nx.DiGraph()
        # show the empty graphs to simulate empty ones
        self.NFA_viz = gv.Digraph()
        self.NFA_viz.node('', shape='none')
        self.plot('NFA', self.NFA_viz, self.NFA_layout, self.NFA_lbl)

        self.DFA_viz = gv.Digraph()
        self.DFA_viz.node('', shape='none')
        self.plot('DFA', self.DFA_viz, self.DFA_layout, self.DFA_lbl)
        # clear the input fields
        self.clearStarFields()

    def plot(self, imgName, graph_viz, layout, label):
        """show the graph inside the Qt window in the gadget

        Args:
            imgName (str): the name of the image shown
            graph_viz (graphviz): the graph made using the graphviz
        """
        self.layout = layout
        self.layout.addWidget(label, alignment=Qt.AlignCenter)
        graph_viz.format = 'png'
        graph_viz.render(imgName, view=False)
        aspectResize(imgName+'.png', self.NFA_Widget.width(),
                     self.NFA_Widget.height())
        pixmap = QPixmap(imgName+'.png')
        label.setPixmap(pixmap)

    def fromNXtoGV(self, graph, graph_viz):
        """turn a networkx digraph into a graphviz graph

        Args:
            graph (Digraph()): network directed graph 
            graph_viz (graphviz):the graphviz where we will store the new graph
        """
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
            if labels[edge] == 'eps':
                graph_viz.edge(edge[0], edge[1], label='ε')
            else:
                graph_viz.edge(edge[0], edge[1], label=labels[edge])

    def addEdge(self):
        """
        add edges to the current graph
        """
        emptyField = False
        fromNode = self.fromNodeTxt.text()
        toNode = self.toNodeTxt.text()
        edgeLbl = self.edgeLabelTxt.text()
        # showing a * where an input field is empty
        if fromNode == '':
            emptyField = True
            self.star_from_node.setText('*')
        else:
            self.star_from_node.setText('')

        if toNode == '':
            emptyField = True
            self.star_to_node.setText('*')
        else:
            self.star_to_node.setText('')

        if edgeLbl == '':
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
                            self.errorMessage(
                                'Error', 'NFA can have only one initial state')
                            self.clearStarFields()
                            return
            else:
                for node in nx.nodes(self.NFA):
                    if self.NFA.nodes[node]['initial']:
                        self.errorMessage(
                            'Error', 'NFA can have only one initial state')
                        self.clearStarFields()
                        return

        if self.toIsInitial.isChecked():
            if toNode in nx.nodes(self.NFA):
                if self.NFA.nodes[toNode]['initial']:
                    pass
                else:
                    for node in nx.nodes(self.NFA):
                        if self.NFA.nodes[node]['initial']:
                            self.errorMessage(
                                'Error', 'NFA can have only one initial state')
                            self.clearStarFields()
                            return
            else:
                for node in nx.nodes(self.NFA):
                    if self.NFA.nodes[node]['initial']:
                        self.errorMessage(
                            'Error', 'NFA can have only one initial state')
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

        # end of checking
        # show the final result
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
        """add epsilons symbols to edges

        Args:
            nodeList (List): Node list
            visited (List): visited nodes list

        Returns:
            set: _description_
        """
        nodeSet = set(nodeList)
        for node in nodeList:
            if node not in visited:
                visited.append(node)
                epsDstNodes = self.NFA.nodes[node]['eps']
                if len(epsDstNodes) != 0:
                    nodeSet = nodeSet.union(epsDstNodes)
                    nodeSet = self.addEpsilonTransitions(
                        list(nodeSet), visited)
        return nodeSet

    def getNextNodeSet(self, nodeList, alpha, isEpsilonNFA):
        nextNodeSet = set()
        for node in nodeList:
            nextNodeSet = nextNodeSet.union(self.NFA.nodes[node][alpha])
        if isEpsilonNFA:
            visited = []
            nextNodeSet = self.addEpsilonTransitions(
                list(nextNodeSet), visited)
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
            if (len(newClusters[i]) == 0):
                remove = i
        if remove != -1:
            newClusters.pop(remove)

        # perform divisive clustering
        while (len(oldClusters) != len(newClusters)):
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
                self.DFA_optimized.add_edge(
                    newNodes[i], newNodes[j], label=",".join(list(newTransitions[i][j])))

        self.DFA = self.DFA_optimized

    def convert(self):
        initialFlag = False
        finalFlag = False
        if len(nx.nodes(self.NFA)) == 0:
            self.errorMessage('Error', 'Please enter your NFA')
            return

        for node in nx.nodes(self.NFA):
            if self.NFA.nodes[node]['initial']:
                initialFlag = True
            if self.NFA.nodes[node]['final']:
                finalFlag = True

        if not initialFlag:
            self.errorMessage(
                'Error', 'NFA must have at least one initial state')
            return
        if not finalFlag:
            self.errorMessage(
                'Error', 'NFA must have at least one final state')
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
            initialNodeSet = self.addEpsilonTransitions(
                list(initialNodeSet), visited)
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
        self.addTransitionTuple(
            alphabet, initialNodeList, visited, nodePattern)

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

    def errorMessage(self, title, text):
        """show error messages during run time

        Args:
            title (str): the title of the error that will be shown on top of the error message
            text (str): error description
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def clearStarFields(self) -> None:
        """function used to clear all input fields and set them to empty strings
        """
        self.star_from_node.setText('')
        self.star_to_node.setText('')
        self.star_transition_edge.setText('')
        self.error_empty_fields.setText('')

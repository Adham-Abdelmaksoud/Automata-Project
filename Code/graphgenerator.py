import networkx as nx

from util import *

graph1 = nx.DiGraph()
graph1.add_edge('q0', 'q0', label='0')
graph1.add_edge('q0', 'q1', label='0,1')
graph1.add_edge('q1', 'q0', label='1')
graph1.add_edge('q1', 'q1', label='1')
for node in graph1.nodes:
    graph1.nodes[node]['initial'] = False
    graph1.nodes[node]['final'] = False
graph1.nodes['q0']['initial'] = True
graph1.nodes['q1']['final'] = True

graph2 = nx.DiGraph()
graph2.add_edge('q0', 'q0', label='0')
graph2.add_edge('q0', 'q1', label='1')
graph2.add_edge('q1', 'q1', label='0,1')
graph2.add_edge('q1', 'q2', label='0')
graph2.add_edge('q2', 'q1', label='1')
graph2.add_edge('q2', 'q2', label='0,1')
for node in graph2.nodes:
    graph2.nodes[node]['initial'] = False
    graph2.nodes[node]['final'] = False
graph2.nodes['q0']['initial'] = True
graph2.nodes['q2']['final'] = True

graph3 = nx.DiGraph()
graph3.add_edge('1', '2', label='eps')
graph3.add_edge('1', '4', label='eps')
graph3.add_edge('2', '3', label='a')
graph3.add_edge('3', '2', label='eps')
graph3.add_edge('3', '4', label='eps')
graph3.add_edge('4', '5', label='eps')
graph3.add_edge('4', '6', label='eps')
graph3.add_edge('5', '7', label='a')
graph3.add_edge('6', '8', label='b')
graph3.add_edge('7', '9', label='eps')
graph3.add_edge('8', '9', label='eps')
for node in graph3.nodes:
    graph3.nodes[node]['initial'] = False
    graph3.nodes[node]['final'] = False
graph3.nodes['1']['initial'] = True
graph3.nodes['9']['final'] = True

graph4 = nx.DiGraph()
graph4.add_edge('1', '2', label='eps')
graph4.add_edge('1', '3', label='eps')
graph4.add_edge('1', '4', label='eps')
graph4.add_edge('2', '5', label='a')
graph4.add_edge('3', '6', label='b')
graph4.add_edge('4', '7', label='a')
graph4.add_edge('7', '8', label='b')
graph4.add_edge('5', '9', label='eps')
graph4.add_edge('6', '9', label='eps')
graph4.add_edge('8', '9', label='eps')
for node in graph4.nodes:
    graph4.nodes[node]['initial'] = False
    graph4.nodes[node]['final'] = False
graph4.nodes['1']['initial'] = True
graph4.nodes['9']['final'] = True

graph5 = nx.DiGraph()
graph5.add_edge('q0', 'q1', label='1')
graph5.add_edge('q0', 'q2', label='eps')
graph5.add_edge('q1', 'q0', label='0')
graph5.add_edge('q1', 'q2', label='0,1')
for node in graph5.nodes:
    graph5.nodes[node]['initial'] = False
    graph5.nodes[node]['final'] = False
graph5.nodes['q0']['initial'] = True
graph5.nodes['q0']['final'] = True

graph6 = nx.DiGraph()
graph6.add_edge('q0', 'q1', label='eps')
graph6.add_edge('q0', 'q2', label='eps')
graph6.add_edge('q1', 'q0', label='eps')
graph6.add_edge('q2', 'q6', label='eps')
graph6.add_edge('q2', 'q4', label='eps')
graph6.add_edge('q6', 'q7', label='b')
graph6.add_edge('q4', 'q5', label='a')
graph6.add_edge('q5', 'q3', label='eps')
graph6.add_edge('q7', 'q3', label='eps')
graph6.add_edge('q3', 'q1', label='eps')
for node in graph6.nodes:
    graph6.nodes[node]['initial'] = False
    graph6.nodes[node]['final'] = False
graph6.nodes['q0']['initial'] = True
graph6.nodes['q1']['final'] = True

graphs = [graph1, graph2, graph3, graph4, graph5, graph6]


def generateRandom_graph(lastRand):
    """when generate is clicked on the gui the function randomly generate a number between 1 to 6 and check that the same is not repeated twice when the last graph index is not equal the new one returns the graph and the index

    Args:
        lastRand (Integer): the index of the last used graph to avoid redunduncy

    Returns:
        nx digraph:the random graph that will be used as an example
        integer: the index of the new example graph
    """
    rand = int(random()*len(graphs))
    while rand == lastRand:
        rand = int(random()*len(graphs))
    return graphs[rand], rand

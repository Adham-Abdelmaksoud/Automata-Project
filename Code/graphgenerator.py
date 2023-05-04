import networkx as nx

from util import *

graph1 = nx.DiGraph()
graph1.add_edges_from([
    ('q0', 'q0', {'label': '0'}),
    ('q0', 'q1', {'label': '0,1'}),
    ('q1', 'q0', {'label': '1'}),
    ('q1', 'q1', {'label': '1'}),
])
for node in graph1.nodes:
    graph1.nodes[node]['initial'] = False
    graph1.nodes[node]['final'] = False
graph1.nodes['q0']['initial'] = True
graph1.nodes['q1']['final'] = True

graph2 = nx.DiGraph()
graph2.add_edges_from([
    ('q0', 'q0', {'label': '0'}),
    ('q0', 'q1', {'label': '1'}),
    ('q1', 'q1', {'label': '0,1'}),
    ('q1', 'q2', {'label': '0'}),
    ('q2', 'q1', {'label': '1'}),
    ('q2', 'q2', {'label': '0,1'}),
])
for node in graph2.nodes:
    graph2.nodes[node]['initial'] = False
    graph2.nodes[node]['final'] = False
graph2.nodes['q0']['initial'] = True
graph2.nodes['q2']['final'] = True

graph3 = nx.DiGraph()
graph3.add_edges_from([
    ('1', '2', {'label': 'eps'}),
    ('1', '4', {'label': 'eps'}),
    ('2', '3', {'label': 'a'}),
    ('3', '2', {'label': 'eps'}),
    ('3', '4', {'label': 'eps'}),
    ('4', '5', {'label': 'eps'}),
    ('4', '6', {'label': 'eps'}),
    ('5', '7', {'label': 'a'}),
    ('6', '8', {'label': 'b'}),
    ('7', '9', {'label': 'eps'}),
    ('8', '9', {'label': 'eps'}),
])
for node in graph3.nodes:
    graph3.nodes[node]['initial'] = False
    graph3.nodes[node]['final'] = False
graph3.nodes['1']['initial'] = True
graph3.nodes['9']['final'] = True

graph4 = nx.DiGraph()
graph4.add_edges_from([('1', '2', {'label': 'eps'}),
                      ('1', '3', {'label': 'eps'}),
                      ('1', '4', {'label': 'eps'}),
                      ('2', '5', {'label': 'a'}),
                      ('3', '6', {'label': 'b'}),
                      ('4', '7', {'label': 'a'}),
                      ('7', '8', {'label': 'b'}),
                      ('5', '9', {'label': 'eps'}),
                      ('6', '9', {'label': 'eps'}),
                      ('8', '9', {'label': 'eps'})
                       ])
for node in graph4.nodes:
    graph4.nodes[node]['initial'] = False
    graph4.nodes[node]['final'] = False
graph4.nodes['1']['initial'] = True
graph4.nodes['9']['final'] = True

graph5 = nx.DiGraph()
graph5.add_edges_from([('q0', 'q1', {'label': '1'}),
                       ('q0', 'q2', {'label': 'eps'}),
                       ('q1', 'q0', {'label': '0'}),
                       ('q1', 'q2', {'label': '0,1'}),
                       ])
for node in graph5.nodes:
    graph5.nodes[node]['initial'] = False
    graph5.nodes[node]['final'] = False
graph5.nodes['q0']['initial'] = True
graph5.nodes['q0']['final'] = True

graph6 = nx.DiGraph()
graph6.add_edges_from([('q0', 'q1', {'label': 'eps'}),
                       ('q0', 'q2', {'label': 'eps'}),
                       ('q1', 'q0', {'label': 'eps'}),
                       ('q2', 'q6', {'label': 'eps'}),
                       ('q2', 'q4', {'label': 'eps'}),
                       ('q6', 'q7', {'label': 'b'}),
                       ('q4', 'q5', {'label': 'a'}),
                       ('q5', 'q3', {'label': 'eps'}),
                       ('q7', 'q3', {'label': 'eps'}),
                       ('q3', 'q1', {'label': 'eps'})
                       ])
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

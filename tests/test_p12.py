
import matplotlib.pyplot as plt
import networkx as nx
import pytest

import copy

from productions import P12, P12_prim
from visualization import draw_graph

def base_graph():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(-1, 1), layer=1)
    G.add_node(2, label='E', pos=(1, 1), layer=1)
    G.add_node(3, label='E', pos=(1, -1), layer=1)
    G.add_node(4, label='E', pos=(-1, -1), layer=1)
    G.add_node(5, label='I', pos=(0, 0), layer=1)
    G.add_edges_from([(5, i) for i in range(1, 5)])
    G.add_edges_from([(i, (i % 4) + 1) for i in range(1, 5)])

    return G

def test_p12_with_match():
    G = base_graph()

    assert P12.apply(G)

    assert [
        # first graph
        (1, {'label': 'E', 'pos': (-1, 1), 'layer': 1}),
        (2, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
        (3, {'label': 'E', 'pos': (1, -1), 'layer': 1}),
        (4, {'label': 'E', 'pos': (-1, -1), 'layer': 1}),
        (5, {'label': 'i', 'pos': (0, 0), 'layer': 1}),
        # second graph
        (6, {'label': 'E', 'pos': (-1, 1), 'layer': 2}),
        (7, {'label': 'E', 'pos': (1, 1), 'layer': 2}),
        (8, {'label': 'E', 'pos': (1, -1), 'layer': 2}),
        (9, {'label': 'E', 'pos': (-1, -1), 'layer': 2}),
        (10, {'label': 'I', 'pos': (0, 0), 'layer': 2}),
    ] == list(G.nodes(data=True))

    assert {
        # first graph,
        (1, 5), (2, 5), (3, 5), (4, 5),
        (1, 2), (1, 4), (2, 3), (3, 4),
        # connecting I nodes 
        (5, 10),
        # second graph
        (6, 10), (7, 10), (8, 10), (9, 10),
        (6, 7), (7, 8), (8, 9), (6, 9),
    } == set(G.edges)

def test_p12_without_match():
    G = base_graph()
    # remove a single edge from I node
    G.remove_edge(5, 1)

    assert False == P12.apply(G)


def test_p12_prim_with_match():
    G = base_graph()
    G.remove_edge(2, 3)
    G.add_node(6, label='E',pos=(1, 0), layer=1)
    G.add_edges_from([(2, 6), (3, 6)])

    assert P12_prim.apply(G)

    assert [
        # first graph
        (1, {'label': 'E', 'pos': (-1, 1), 'layer': 1}),
        (2, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
        (3, {'label': 'E', 'pos': (1, -1), 'layer': 1}),
        (4, {'label': 'E', 'pos': (-1, -1), 'layer': 1}),
        (5, {'label': 'i', 'pos': (0, 0), 'layer': 1}),
        (6, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
        # second graph
        (7, {'label': 'E', 'pos': (-1, 1), 'layer': 2}),
        (8, {'label': 'E', 'pos': (1, 1), 'layer': 2}),
        (9, {'label': 'E', 'pos': (1, 0), 'layer': 2}),
        (10, {'label': 'E', 'pos': (1, -1), 'layer': 2}),
        (11, {'label': 'E', 'pos': (-1, -1), 'layer': 2}),
        (12, {'label': 'I', 'pos': (0, 0), 'layer': 2}),
    ] == list(G.nodes(data=True))

    assert {
        # first graph,
        (1, 5), (2, 5), (3, 5), (4, 5),
        (1, 2), (1, 4), (2, 6), (3, 6), (3, 4),
        # connecting I nodes 
        (5, 12),
        # second graph
        (7, 12), (8, 12), (10, 12), (11, 12),
        (7, 8), (7, 11), (8, 9), (9, 10), (10, 11),
    } == set(G.edges)




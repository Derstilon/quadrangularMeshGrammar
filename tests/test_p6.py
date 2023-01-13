import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P6
from visualization import draw_graph


def test_p6_should_be_applied_right():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(1, 0.5), layer=0)
    G.add_node(7, label='E', pos=(0.5, 1), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 4)
    G.add_edge(2, 3)
    G.add_edge(3, 6)
    G.add_edge(5, 6)
    G.add_edge(4, 7)
    G.add_edge(5, 7)

    assert True == P6.apply(G)

def test_p6_should_be_applied_top():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(0.5, 0), layer=0)
    G.add_node(7, label='E', pos=(1, 0.5), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 4)
    G.add_edge(2, 6)
    G.add_edge(3, 6)
    G.add_edge(3, 7)
    G.add_edge(4, 5)
    G.add_edge(5, 7)

    assert True == P6.apply(G)


def test_p6_should_be_applied_left():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(0.5, 0), layer=0)
    G.add_node(7, label='E', pos=(0, 0.5), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 7)
    G.add_edge(2, 6)
    G.add_edge(3, 6)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 7)

    assert True == P6.apply(G)

def test_p6_should_be_not_applied_wrong_label():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='I', pos=(0.5, 0), layer=0)
    G.add_node(7, label='E', pos=(0, 0.5), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 7)
    G.add_edge(2, 6)
    G.add_edge(3, 6)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 7)

    assert False == P6.apply(G)

def test_p6_should_be_not_applied_wrong_coordinates():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(0.5, 0), layer=0)
    G.add_node(7, label='E', pos=(0, 0.4), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 7)
    G.add_edge(2, 6)
    G.add_edge(3, 6)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 7)

    assert False == P6.apply(G)


def test_p6_should_be_not_applied_wrong_coordinates_additional_node():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(0.5, 0), layer=0)
    G.add_node(7, label='E', pos=(0, 0.5), layer=0)
    G.add_node(8, label='E', pos=(-1, 0), layer=0)
    G.add_node(9, label='E', pos=(2, 0.5), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 7)
    G.add_edge(2, 6)
    G.add_edge(3, 6)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 7)
    G.add_edge(2, 8)
    G.add_edge(3, 9)

    assert True == P6.apply(G)

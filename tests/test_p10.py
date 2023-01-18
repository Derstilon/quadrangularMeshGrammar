import networkx as nx
import pytest

from productions.p10 import P10


@pytest.fixture
def G():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(1 / 2, 0), layer=0)
    G.add_node(2, label='i', pos=(1 / 4, 1), layer=0)
    G.add_node(3, label='i', pos=(3 / 4, 1), layer=0)

    G.add_node(4, label='E', pos=(1 / 2, 2), layer=0)

    G.add_node(6, label='I', pos=(0, 3), layer=0)
    G.add_node(7, label='I', pos=(1, 3), layer=0)

    G.add_node(8, label='E', pos=(1 / 2, 4), layer=0)
    G.add_node(9, label='E', pos=(1 / 2, 4), layer=0)

    G.add_node(10, label='I', pos=(0, 5), layer=0)
    G.add_node(11, label='I', pos=(1, 5), layer=0)

    G.add_node(12, label='E', pos=(1 / 2, 6), layer=0)
    G.add_node(13, label='E', pos=(1 / 2, 6), layer=0)

    G.add_edges_from([(1, 2), (1, 3)])

    G.add_edges_from([(2, i) for i in (6, 10)])
    G.add_edges_from([(3, i) for i in (7, 11)])
    #
    G.add_edges_from([(6, i) for i in (4, 8)])
    G.add_edges_from([(7, i) for i in (9, 4)])

    G.add_edges_from([(10, i) for i in (8, 12)])
    G.add_edges_from([(11, i) for i in (9, 13)])

    G.add_edges_from([(4, 8), (8, 12)])
    G.add_edges_from([(9, 13)])

    return G


def test_p10_should_be_applied_full_proper_graph(G):
    assert P10.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0.5, 0), 'layer': 0}), (2, {'label': 'i', 'pos': (0.25, 1), 'layer': 0}),
            (3, {'label': 'i', 'pos': (0.75, 1), 'layer': 0}), (4, {'label': 'E', 'pos': (0.5, 2), 'layer': 0}),
            (6, {'label': 'I', 'pos': (0, 3), 'layer': 0}), (7, {'label': 'I', 'pos': (1, 3), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0.5, 4), 'layer': 0}), (10, {'label': 'I', 'pos': (0, 5), 'layer': 0}),
            (11, {'label': 'I', 'pos': (1, 5), 'layer': 0}), (13, {'label': 'E', 'pos': (0.5, 6), 'layer': 0})] \
           == list(G.nodes(data=True))

    assert {(9, 10), (1, 2), (9, 13), (6, 9), (4, 9), (3, 7), (2, 10), (4, 6), (11, 13), (10, 13), (7, 9), (2, 6),
            (9, 11), (1, 3), (4, 7), (3, 11)} \
           == set(G.edges)

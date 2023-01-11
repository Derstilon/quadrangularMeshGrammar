import copy

import networkx as nx
import pytest

from productions.p9 import P9


@pytest.fixture
def G():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(1 / 2, 0), layer=0)
    G.add_node(2, label='i', pos=(1 / 4, 1), layer=0)
    G.add_node(3, label='i', pos=(3 / 4, 1), layer=0)

    G.add_node(4, label='E', pos=(1 / 2, 2), layer=0)
    G.add_node(5, label='E', pos=(1 / 2, 2), layer=0)

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

    G.add_edges_from([(6, i) for i in (4, 8)])
    G.add_edges_from([(7, i) for i in (5, 9)])

    G.add_edges_from([(10, i) for i in (8, 12)])
    G.add_edges_from([(11, i) for i in (9, 13)])

    G.add_edges_from([(4, 8), (8, 12)])
    G.add_edges_from([(5, 9), (9, 13)])

    return G


def test_p9_should_be_applied_full_proper_graph(G):
    assert P9.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0.5, 0), 'layer': 0}),
            (2, {'label': 'i', 'pos': (0.25, 1), 'layer': 0}),
            (3, {'label': 'i', 'pos': (0.75, 1), 'layer': 0}),
            (5, {'label': 'E', 'pos': (0.5, 2), 'layer': 0}),
            (6, {'label': 'I', 'pos': (0, 3), 'layer': 0}),
            (7, {'label': 'I', 'pos': (1, 3), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0.5, 4), 'layer': 0}),
            (10, {'label': 'I', 'pos': (0, 5), 'layer': 0}),
            (11, {'label': 'I', 'pos': (1, 5), 'layer': 0}),
            (13, {'label': 'E', 'pos': (0.5, 6), 'layer': 0})] \
           == list(G.nodes(data=True))

    assert {(9, 10), (1, 2), (9, 13), (6, 9), (3, 7), (2, 10), (9, 11), (11, 13), (5, 7), (10, 13), (7, 9), (2, 6),
            (5, 6), (5, 9), (1, 3), (3, 11)} \
           == set(G.edges)


def test_p9_should_apply_with_added_nodes(G):
    G.add_node(14, label='E', pos=(0, 7), layer=0)
    G.add_edge(14, 1)
    G.add_edge(14, 2)
    G.add_edge(14, 3)
    G.add_edge(14, 6)
    G.add_edge(14, 11)

    assert P9.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0.5, 0), 'layer': 0}),
            (2, {'label': 'i', 'pos': (0.25, 1), 'layer': 0}),
            (3, {'label': 'i', 'pos': (0.75, 1), 'layer': 0}),
            (4, {'label': 'E', 'pos': (0.5, 2), 'layer': 0}),
            (6, {'label': 'I', 'pos': (0, 3), 'layer': 0}),
            (7, {'label': 'I', 'pos': (1, 3), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0.5, 4), 'layer': 0}),
            (10, {'label': 'I', 'pos': (0, 5), 'layer': 0}),
            (11, {'label': 'I', 'pos': (1, 5), 'layer': 0}),
            (13, {'label': 'E', 'pos': (0.5, 6), 'layer': 0}),
            (14, {'label': 'E', 'pos': (0, 7), 'layer': 0})] == \
           list(G.nodes(data=True))

    assert {(3, 7), (4, 6), (9, 11), (11, 14), (1, 3), (2, 14), (6, 14), (9, 10), (1, 2), (9, 13), (11, 13), (2, 10),
            (1, 14), (7, 9), (4, 7), (3, 11), (3, 14), (10, 13), (2, 6), (6, 9)} == set(
        G.edges)


def test_p9_should_not_apply_with_added_nodes(G):
    G.add_node(14, label='E', pos=(0, 7), layer=0)
    G.remove_edge(1, 2)
    G.add_edge(1, 14)
    G.add_edge(14, 2)

    assert P9.apply(G) is False


def test_p9_should_not_apply_node_removed(G):
    for i in range(1, 12):
        _G = copy.deepcopy(G)

        _G.remove_node(i)

        assert P9.apply(_G) is False


def test_p9_should_not_apply_edge_removed(G):
    for i in range(1, 14):
        _G = copy.deepcopy(G)

        (v1, v2) = list(_G.edges)[i]
        _G.remove_edge(v1, v2)

        assert P9.apply(_G) is False


def test_p9_should_not_apply_node_label_changed(G):
    for i in range(1, 12):
        _G = copy.deepcopy(G)

        _G.nodes[i]['label'] = 'm'

        assert P9.apply(_G) is False

import networkx as nx

from productions import P15


def get_basic_graph():
    basic_graph = nx.Graph()
    basic_graph.add_node(1, label='E', pos=(0, 6), layer=0)
    basic_graph.add_node(2, label='i', pos=(-1, 5), layer=0)
    basic_graph.add_node(3, label='i', pos=(1, 5), layer=0)
    basic_graph.add_node(4, label='I', pos=(-2, 3), layer=0)
    basic_graph.add_node(5, label='I', pos=(2, 3), layer=0)
    basic_graph.add_node(6, label='E', pos=(0, 4), layer=0)
    basic_graph.add_node(7, label='E', pos=(0, 0), layer=0)
    basic_graph.add_node(8, label='E', pos=(0, 4), layer=0)
    basic_graph.add_node(9, label='E', pos=(0, 0), layer=0)
    basic_graph.add_edge(1, 2)
    basic_graph.add_edge(1, 3)
    basic_graph.add_edge(2, 4)
    basic_graph.add_edge(3, 5)
    basic_graph.add_edge(4, 6)
    basic_graph.add_edge(4, 7)
    basic_graph.add_edge(5, 8)
    basic_graph.add_edge(5, 9)
    basic_graph.add_edge(6, 7)
    basic_graph.add_edge(8, 9)
    return basic_graph


def test_P15_should_apply_basic():
    G = get_basic_graph()

    assert P15.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0, 6), 'layer': 0}),
            (2, {'label': 'i', 'pos': (-1, 5), 'layer': 0}),
            (3, {'label': 'i', 'pos': (1, 5), 'layer': 0}),
            (4, {'label': 'I', 'pos': (-2, 3), 'layer': 0}),
            (5, {'label': 'I', 'pos': (2, 3), 'layer': 0}),
            (8, {'label': 'E', 'pos': (0, 4), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 0})] == list(G.nodes(data=True))

    assert {(2, 4), (1, 2), (5, 8), (4, 9), (4, 8), (5, 9), (1, 3), (3, 5), (8, 9)} == set(G.edges)


def test_P15_should_apply_with_added_nodes():
    G = get_basic_graph()
    G.add_node(10, label='E', pos=(0, 7), layer=0)
    G.add_edge(10, 1)
    G.add_edge(10, 2)
    G.add_edge(10, 3)
    G.add_edge(10, 4)
    G.add_edge(10, 5)

    assert P15.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0, 6), 'layer': 0}),
            (2, {'label': 'i', 'pos': (-1, 5), 'layer': 0}),
            (3, {'label': 'i', 'pos': (1, 5), 'layer': 0}),
            (4, {'label': 'I', 'pos': (-2, 3), 'layer': 0}),
            (5, {'label': 'I', 'pos': (2, 3), 'layer': 0}),
            (8, {'label': 'E', 'pos': (0, 4), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 0}),
            (10, {'label': 'E', 'pos': (0, 7), 'layer': 0})] == list(G.nodes(data=True))

    assert {(1, 2), (1, 3), (1, 10), (2, 4), (2, 10), (3, 5), (3, 10), (4, 8), (4, 9), (4, 10), (5, 8), (5, 9), (5, 10), (8, 9)} == set(G.edges)


def test_P15_should_apply_with_added_nodes_2():
    G = get_basic_graph()
    G.add_node(10, label='E', pos=(0, 7), layer=0)
    G.add_edge(10, 6)
    G.add_edge(10, 7)

    assert P15.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0, 6), 'layer': 0}),
            (2, {'label': 'i', 'pos': (-1, 5), 'layer': 0}),
            (3, {'label': 'i', 'pos': (1, 5), 'layer': 0}),
            (4, {'label': 'I', 'pos': (-2, 3), 'layer': 0}),
            (5, {'label': 'I', 'pos': (2, 3), 'layer': 0}),
            (8, {'label': 'E', 'pos': (0, 4), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 0}),
            (10, {'label': 'E', 'pos': (0, 7), 'layer': 0})] == list(G.nodes(data=True))

    assert {(1, 2), (1, 3), (2, 4), (3, 5), (4, 8), (4, 9), (5, 8), (5, 9), (8, 9), (8, 10), (9, 10)} == set(G.edges)

def test_P15_should_not_apply_with_added_nodes():
    G = get_basic_graph()
    G.add_node(12, label='E', pos=(0, 7), layer=0)
    G.remove_edge(1, 2)
    G.add_edge(1, 12)
    G.add_edge(12, 2)

    assert P15.apply(G) is False


def test_P15_should_not_apply_node_removed():
    for i in range(1, 9):
        G = get_basic_graph()

        G.remove_node(i)

        assert P15.apply(G) is False


def test_P15_should_not_apply_edge_removed():
    for i in range(0, 10):
        G = get_basic_graph()

        (v1, v2) = list(G.edges)[i]
        G.remove_edge(v1, v2)

        assert P15.apply(G) is False


def test_P15_should_not_apply_node_label_changed():
    for i in range(1, 9):
        G = get_basic_graph()

        G.nodes[i]['label'] = 'm'

        assert P15.apply(G) is False


def test_P15_should_not_apply_wrong_coordinates_1():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(0, 6), layer=0)
    G.add_node(2, label='i', pos=(-1, 5), layer=0)
    G.add_node(3, label='i', pos=(1, 5), layer=0)
    G.add_node(4, label='I', pos=(-2, 3), layer=0)
    G.add_node(5, label='I', pos=(2, 3), layer=0)
    G.add_node(6, label='E', pos=(0, 1), layer=0)
    G.add_node(7, label='E', pos=(0, 0), layer=0)
    G.add_node(8, label='E', pos=(0, 4), layer=0)
    G.add_node(9, label='E', pos=(0, 8), layer=0)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 6)
    G.add_edge(4, 7)
    G.add_edge(5, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 7)
    G.add_edge(8, 9)

    assert P15.apply(G) is False


def test_P15_should_not_apply_wrong_coordinates_2():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(0, 6), layer=0)
    G.add_node(2, label='i', pos=(-1, 5), layer=0)
    G.add_node(3, label='i', pos=(1, 5), layer=0)
    G.add_node(4, label='I', pos=(-2, 3), layer=0)
    G.add_node(5, label='I', pos=(2, 3), layer=0)
    G.add_node(6, label='E', pos=(0, 0), layer=0)
    G.add_node(7, label='E', pos=(0, 0), layer=0)
    G.add_node(8, label='E', pos=(0, 4), layer=0)
    G.add_node(9, label='E', pos=(0, 0), layer=0)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 6)
    G.add_edge(4, 7)
    G.add_edge(5, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 7)
    G.add_edge(8, 9)

    assert P15.apply(G) is False

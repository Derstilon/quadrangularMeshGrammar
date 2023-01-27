import networkx as nx
from productions import P1, P2


def test_p1_p2_p2_p2_should_create_correct_structure():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert True == P1.apply(G)
    assert True == P2.apply(G)
    assert True == P2.apply(G)
    assert True == P2.apply(G)

    expected_nodes = [
        (1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
        (2, {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1}),
        (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
        (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
        (5, {'label': 'E', 'pos': (0, 1), 'layer': 1}),
        (6, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
        # SECOND LAYER
        (7, {'label': 'i', 'pos': (0.25, 0.5), 'layer': 2}),
        (8, {'label': 'i', 'pos': (0.75, 0.5), 'layer': 2}),
        (9, {'label': 'E', 'pos': (0, 0), 'layer': 2}),
        (10, {'label': 'E', 'pos': (0.5, 0.), 'layer': 2}),
        (11, {'label': 'E', 'pos': (1, 0), 'layer': 2}),
        (12, {'label': 'E', 'pos': (0, 1), 'layer': 2}),
        (13, {'label': 'E', 'pos': (0.5, 1.), 'layer': 2}),
        (14, {'label': 'E', 'pos': (1, 1), 'layer': 2}),
        # THIRD LAYER
        (15, {'label': 'I', 'pos': (0.125, 0.5), 'layer': 3}),
        (16, {'label': 'I', 'pos': (0.375, 0.5), 'layer': 3}),
        (17, {'label': 'E', 'pos': (0, 0), 'layer': 3}),
        (18, {'label': 'E', 'pos': (0.25, 0.), 'layer': 3}),
        (19, {'label': 'E', 'pos': (0.5, 0.), 'layer': 3}),
        (20, {'label': 'E', 'pos': (0, 1), 'layer': 3}),
        (21, {'label': 'E', 'pos': (0.25, 1.), 'layer': 3}),
        (22, {'label': 'E', 'pos': (0.5, 1.), 'layer': 3}),

        (23, {'label': 'I', 'pos': (0.625, 0.5), 'layer': 3}),
        (24, {'label': 'I', 'pos': (0.875, 0.5), 'layer': 3}),
        (25, {'label': 'E', 'pos': (0.5, 0.), 'layer': 3}),
        (26, {'label': 'E', 'pos': (0.75, 0.), 'layer': 3}),
        (27, {'label': 'E', 'pos': (1, 0), 'layer': 3}),
        (28, {'label': 'E', 'pos': (0.5, 1), 'layer': 3}),
        (29, {'label': 'E', 'pos': (0.75, 1), 'layer': 3}),
        (30, {'label': 'E', 'pos': (1, 1), 'layer': 3}),
    ]

    assert sorted(expected_nodes, key=lambda val: val[0]) == \
           sorted(G.nodes(data=True), key=lambda val: val[0])

    assert {(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4),
            (3, 5), (4, 6), (5, 6), (2, 7), (7, 9), (7, 10),
            (7, 12), (2, 8), (8, 10), (8, 11), (8, 13),
            (7, 13), (8, 14), (9, 10), (10, 11), (9, 12),
            (15, 21), (17, 20), (16, 19), (15, 17), (7, 16),
            (21, 22), (16, 22), (15, 20), (18, 19), (16, 21),
            (19, 22), (16, 18), (7, 15), (18, 21), (17, 18),
            (20, 21), (15, 18), (10, 13), (13, 14), (11, 14),
            (12, 13), (24, 30), (8, 24), (24, 27), (8, 23),
            (26, 27), (25, 28), (24, 26), (27, 30), (28, 29),
            (23, 26), (24, 29), (23, 29), (23, 28), (26, 29),
            (23, 25), (25, 26), (29, 30)} == set(G.edges)


def test_p1_p2_p2_should_apply_p2_on_the_right_for_wrong_label():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert True == P1.apply(G)
    assert True == P2.apply(G)

    G.nodes[7]['label'] = 'WRONG LABEL'

    assert True == P2.apply(G)

    expected_nodes = [
        (1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
        (2, {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1}),
        (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
        (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
        (5, {'label': 'E', 'pos': (0, 1), 'layer': 1}),
        (6, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
        (7, {'label': 'WRONG LABEL', 'pos': (0.25, 0.5), 'layer': 2}),
        (8, {'label': 'i', 'pos': (0.75, 0.5), 'layer': 2}),
        (9, {'label': 'E', 'pos': (0, 0), 'layer': 2}),
        (10, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 2}),
        (11, {'label': 'E', 'pos': (1, 0), 'layer': 2}),
        (12, {'label': 'E', 'pos': (0, 1), 'layer': 2}),
        (13, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 2}),
        (14, {'label': 'E', 'pos': (1, 1), 'layer': 2}),
        (15, {'label': 'I', 'pos': (0.625, 0.5), 'layer': 3}),
        (16, {'label': 'I', 'pos': (0.875, 0.5), 'layer': 3}),
        (17, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 3}),
        (18, {'label': 'E', 'pos': (0.75, 0.0), 'layer': 3}),
        (19, {'label': 'E', 'pos': (1, 0), 'layer': 3}),
        (20, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 3}),
        (21, {'label': 'E', 'pos': (0.75, 1.0), 'layer': 3}),
        (22, {'label': 'E', 'pos': (1, 1), 'layer': 3})
    ]

    assert sorted(expected_nodes, key=lambda val: val[0]) == \
           sorted(G.nodes(data=True), key=lambda val: val[0])

    assert {(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (2, 8), (3, 4), (3, 5), (4, 6), (5, 6), (7, 9),
            (7, 10), (7, 12), (7, 13), (8, 10), (8, 11), (8, 13),
            (8, 14), (8, 15), (8, 16), (9, 10), (9, 12), (10, 11),
            (10, 13), (11, 14), (12, 13), (13, 14), (15, 17),
            (15, 18), (15, 20), (15, 21), (16, 18), (16, 19),
            (16, 21), (16, 22), (17, 18), (17, 20), (18, 19),
            (18, 21), (19, 22), (20, 21), (21, 22)} == set(G.edges)


def test_p1_p2_p2_should_apply_p2_on_the_right_for_additional_node():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert True == P1.apply(G)
    assert True == P2.apply(G)

    G.remove_edge(9, 10)
    G.add_node(50, label='E', pos=(0.25, 0), layer=2)
    G.add_edge(9, 50)
    G.add_edge(10, 50)

    assert True == P2.apply(G)

    expected_nodes = [
        (1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
        (2, {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1}),
        (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
        (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
        (5, {'label': 'E', 'pos': (0, 1), 'layer': 1}),
        (6, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
        (7, {'label': 'I', 'pos': (0.25, 0.5), 'layer': 2}),
        (8, {'label': 'i', 'pos': (0.75, 0.5), 'layer': 2}),
        (9, {'label': 'E', 'pos': (0, 0), 'layer': 2}),
        (10, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 2}),
        (11, {'label': 'E', 'pos': (1, 0), 'layer': 2}),
        (12, {'label': 'E', 'pos': (0, 1), 'layer': 2}),
        (13, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 2}),
        (14, {'label': 'E', 'pos': (1, 1), 'layer': 2}),
        (50, {'label': 'E', 'pos': (0.25, 0), 'layer': 2}),
        (51, {'label': 'I', 'pos': (0.625, 0.5), 'layer': 3}),
        (52, {'label': 'I', 'pos': (0.875, 0.5), 'layer': 3}),
        (53, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 3}),
        (54, {'label': 'E', 'pos': (0.75, 0.0), 'layer': 3}),
        (55, {'label': 'E', 'pos': (1, 0), 'layer': 3}),
        (56, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 3}),
        (57, {'label': 'E', 'pos': (0.75, 1.0), 'layer': 3}),
        (58, {'label': 'E', 'pos': (1, 1), 'layer': 3})
    ]

    assert sorted(expected_nodes, key=lambda val: val[0]) == \
           sorted(G.nodes(data=True), key=lambda val: val[0])

    assert {(3, 4), (51, 53), (8, 52), (52, 58), (4, 6),
            (12, 13), (51, 56), (52, 55), (2, 5), (11, 14),
            (2, 8), (13, 14), (53, 56), (54, 55), (7, 10),
            (7, 13), (9, 50), (52, 54), (5, 6), (8, 51),
            (52, 57), (8, 11), (2, 4), (1, 2), (8, 14),
            (10, 11), (2, 7), (54, 57), (7, 9), (55, 58),
            (7, 12), (56, 57), (3, 5), (51, 54), (10, 50),
            (51, 57), (57, 58), (9, 12), (8, 10), (10, 13),
            (2, 3), (8, 13), (2, 6), (53, 54)} == set(G.edges)

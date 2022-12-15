import networkx as nx
from productions.decorators import first_isomorphism, isomorphism_P5, isomorphism_P6
from typing import Dict


class P6():
    left = nx.Graph()
    left.add_node(1, label='I')
    left.add_node(2, label='E')
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='E')
    left.add_node(6, label='E')
    left.add_node(7, label='E')
    left.add_edges_from([(1, i) for i in range(2, 6)])
    left.add_edge(3, 5)
    left.add_edge(4, 5)
    left.add_edge(2, 6)
    left.add_edge(4, 6)
    left.add_edge(2, 7)
    left.add_edge(3, 7)

    @staticmethod
    @isomorphism_P6(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())

        E_pos = []
        I_node = None
        I_node_id = None
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]
                I_node_id = node
            elif G.nodes[node]['label'] == 'E':
                E_pos.append(G.nodes[node]['pos'])

        I_node['label'] = 'i'

        layer = I_node['layer']
        pos = sorted(E_pos, key=lambda e: (e[1], e[0]))
        print(pos)
        [(x1, y1), (x6, y6), (x2, y2), (x5, y5), (x3, y3), (x4, y4)] = pos

        size = G.number_of_nodes()

        G.add_node(size + 1, label='I', pos=((3 * x1 + x2) / 4, (3 * y1 + y3) / 4), layer=layer + 1)
        G.add_node(size + 2, label='I', pos=((3 * x1 + x2) / 4, (y1 + 3 * y3) / 4), layer=layer + 1)
        G.add_node(size + 3, label='I', pos=((x1 + 3 * x2) / 4, (3 * y1 + y3) / 4), layer=layer + 1)
        G.add_node(size + 4, label='I', pos=((x1 + 3 * x2) / 4, (y1 + 3 * y3) / 4), layer=layer + 1)

        G.add_edge(size + 1, I_node_id)
        G.add_edge(size + 2, I_node_id)
        G.add_edge(size + 3, I_node_id)
        G.add_edge(size + 4, I_node_id)

        G.add_node(size + 5, label='E', pos=(x1, y1), layer=layer + 1)
        G.add_node(size + 6, label='E', pos=((x1 + x2) / 2, (y1 + y2) / 2), layer=layer + 1)
        G.add_node(size + 7, label='E', pos=(x2, y2), layer=layer + 1)

        G.add_node(size + 8, label='E', pos=((x1 + x3) / 2, (y1 + y3) / 2), layer=layer + 1)
        G.add_node(size + 9, label='E', pos=((x1 + x4) / 2, (y1 + y4) / 2), layer=layer + 1)
        G.add_node(size +10, label='E', pos=((x2 + x4) / 2, (y2 + y4) / 2), layer=layer + 1)

        G.add_node(size +11, label='E', pos=(x3, y3), layer=layer + 1)
        G.add_node(size +12, label='E', pos=((x3 + x4) / 2, (y3 + y4) / 2), layer=layer + 1)
        G.add_node(size +13, label='E', pos=(x4, y4), layer=layer + 1)

        #
        G.add_edges_from([(size + 1, size + i) for i in (5, 6, 8, 9)])
        G.add_edges_from([(size + 2, size + i) for i in (8, 9, 11, 12)])
        G.add_edges_from([(size + 3, size + i) for i in (6, 7, 9, 10)])
        G.add_edges_from([(size + 4, size + i) for i in (9, 10, 12, 13)])

        def with_size(pairs):
            return [(size + i, size + j) for i, j in pairs]

        G.add_edges_from(with_size([
            (5,  6),
            (6,  7),
            (8,  9),
            (9, 10),
            (11, 12),
            (12, 13),
            (5, 8),
            (8, 11),
            (6, 9),
            (9, 12),
            (7, 10),
            (10, 13),
        ]))

        return True

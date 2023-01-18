import networkx as nx
from productions.decorators import first_isomorphism_for_p9
from typing import Dict


class P9:
    @staticmethod
    def __left():
        left = nx.Graph()
        left.add_node(1, label='E')
        left.add_node(2, label='i')
        left.add_node(3, label='i')

        left.add_node(4, label='E')
        left.add_node(5, label='E')

        left.add_node(6, label='I')
        left.add_node(7, label='I')

        left.add_node(8, label='E')
        left.add_node(9, label='E')

        left.add_node(10, label='I')
        left.add_node(11, label='I')

        left.add_node(12, label='E')
        left.add_node(13, label='E')

        left.add_edges_from([(1, 2), (1, 3)])

        left.add_edges_from([(2, i) for i in (6, 10)])
        left.add_edges_from([(3, i) for i in (7, 11)])

        left.add_edges_from([(6, i) for i in (4, 8)])
        left.add_edges_from([(7, i) for i in (5, 9)])

        left.add_edges_from([(10, i) for i in (8, 12)])
        left.add_edges_from([(11, i) for i in (9, 13)])

        left.add_edges_from([(4, 8), (8, 12)])
        left.add_edges_from([(5, 9), (9, 13)])

        return left

    left = __left.__func__()

    @staticmethod
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    @staticmethod
    @first_isomorphism_for_p9(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())
        E_nodes = []

        for node in nodes_in_G:
            # all E nodes
            if G.nodes[node]['label'] == 'E':
                adjacency = G.adj[node]
                is_connected_to_i = False
                # find if connected to any i
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                # add all valid E nodes
                if not is_connected_to_i:
                    E_nodes.append(node)

        E_nodes = sorted(E_nodes, key=lambda node: G.nodes[node]['pos'])
        E_chunks = P9.chunks(E_nodes, 2)

        for left, right in E_chunks:
            if G.nodes[left]['pos'] != G.nodes[right]['pos']:
                continue
            adjacency = G.adj[left]
            G.remove_node(left)
            for adj in adjacency:
                G.add_edge(right, adj)

        return True



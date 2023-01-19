import networkx as nx
from productions.decorators import p15_isomorphism
from typing import Dict


class P15:
    left = nx.Graph()
    left.add_node(1, label='E')
    left.add_node(2, label='i')
    left.add_node(3, label='i')
    left.add_node(4, label='I')
    left.add_node(5, label='I')
    left.add_node(6, label='E')
    left.add_node(7, label='E')
    left.add_node(8, label='E')
    left.add_node(9, label='E')
    left.add_edge(1, 2)
    left.add_edge(1, 3)
    left.add_edge(2, 4)
    left.add_edge(3, 5)
    left.add_edge(4, 6)
    left.add_edge(4, 7)
    left.add_edge(5, 8)
    left.add_edge(5, 9)
    left.add_edge(6, 7)
    left.add_edge(8, 9)

    @staticmethod
    @p15_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())

        to_remove_1 = None
        to_remove_2 = None

        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'E':
                adjacency = G.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'i' and neighbour in nodes_in_G:
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    to_remove_1 = (node, tuple(G.nodes[node]['pos']), G.nodes[node]['layer'])
                    for neighbour in adjacency:
                        if neighbour in nodes_in_G and G.nodes[neighbour]['label'] == 'E':
                            to_remove_2 = (neighbour, tuple(G.nodes[neighbour]['pos']), G.nodes[neighbour]['layer'])
                    break

        to_remove_1_neighbours = G.adj[to_remove_1[0]]
        to_remove_2_neighbours = G.adj[to_remove_2[0]]

        G.remove_node(to_remove_1[0])
        G.remove_node(to_remove_2[0])
        nodes_in_G.remove(to_remove_1[0])
        nodes_in_G.remove(to_remove_2[0])

        for node in nodes_in_G:
            pos = tuple(G.nodes[node]['pos'])
            if pos == to_remove_1[1] and G.nodes[node]['label'] == 'E' and G.nodes[node]['layer'] == to_remove_1[2]:
                for neighbour in to_remove_1_neighbours:
                    if neighbour != to_remove_2[0]:
                        G.add_edge(node, neighbour)
            elif pos == to_remove_2[1] and G.nodes[node]['label'] == 'E' and G.nodes[node]['layer'] == to_remove_2[2]:
                for neighbour in to_remove_2_neighbours:
                    if neighbour != to_remove_1[0]:
                        G.add_edge(node, neighbour)

        return True
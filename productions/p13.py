import networkx as nx
from productions.decorators import p13_isomorphism
from typing import Dict

class P13:
    left = nx.Graph()
    left.add_node(1, label='E')
    left.add_node(2, label='i')
    left.add_node(3, label='i')
    left.add_node(4, label='I')
    left.add_node(5, label='I')
    left.add_node(6, label='I')
    left.add_node(7, label='E')
    left.add_node(8, label='E')
    left.add_node(9, label='E')
    left.add_node(10, label='E')
    left.add_node(11, label='E')
    left.add_edge(1, 2)
    left.add_edge(1, 3)
    left.add_edge(2, 4)
    left.add_edge(2, 5)
    left.add_edge(3, 6)
    left.add_edge(4, 7)
    left.add_edge(4, 8)
    left.add_edge(5, 8)
    left.add_edge(5, 9)
    left.add_edge(6, 10)
    left.add_edge(6, 11)
    left.add_edge(7, 8)
    left.add_edge(8, 9)
    left.add_edge(10, 11)

    @staticmethod
    @p13_isomorphism(left, all_isomorphisms=True)
    def apply(G: nx.Graph, isomorphisms: Dict = None, options: Dict = None):
        if not isomorphisms or len(isomorphisms) == 0:
            return False

        isomorphism = None
        if options['apply'] is not None:
            for i in isomorphisms:
                if options['apply'](i):
                    isomorphism = i
            if isomorphism is None:
                return False
        else:
            isomorphism = isomorphisms[0]

        nodes_in_G = list(isomorphism.keys())
        E_nodes = []        
        #!!!!!!!!!! changed from E_coeff = set() to E_coeff = [] !!!!!!!!!!!!!!
        E_coeff = []

        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'E':
                adjacency = G.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    E_nodes.append(node)
                    E_coeff.append(G.nodes[node]['pos'])
        
        #!!!!!!!!!! changed from E_coeff = sorted(E_coeff) to E_coeff = sorted(E_coeff, key=lambda x: (x[0], x[1])) !!!!!!!!!!!!!!
        E_coeff = sorted(E_coeff, key=lambda x: (x[0], x[1]))

        to_remove_1 = None
        to_remove_2 = None

        for node in E_nodes:
            adjacency = G.adj[node]
            pos = G.nodes[node]['pos']
            if pos == E_coeff[0] or pos == E_coeff[2]:
                to_remove = True
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'E' and G.nodes[neighbour]['pos'] == E_coeff[1]:
                        to_remove = False
                if to_remove:
                    to_remove_1 = (node, G.nodes[node]['pos'])
                    for neighbour in adjacency:
                        if G.nodes[neighbour]['label'] == 'E' and neighbour in nodes_in_G:
                            to_remove_2 = (neighbour, G.nodes[neighbour]['pos'])
                    break

        to_remove_1_neighbours = G.adj[to_remove_1[0]]
        to_remove_2_neighbours = G.adj[to_remove_2[0]]

        E_nodes.remove(to_remove_1[0])
        E_nodes.remove(to_remove_2[0])
        G.remove_node(to_remove_1[0])
        G.remove_node(to_remove_2[0])

        for node in E_nodes:
            pos = G.nodes[node]['pos']
            if pos == to_remove_1[1]:
                for neighbour in to_remove_1_neighbours:
                    if neighbour != to_remove_2[0]:
                        G.add_edge(node, neighbour)
            elif pos == to_remove_2[1]:
                for neighbour in to_remove_2_neighbours:
                    if neighbour != to_remove_1[0]:
                        G.add_edge(node, neighbour)

        return True

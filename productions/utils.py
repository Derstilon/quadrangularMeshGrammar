from typing import Dict, List

from networkx import Graph
from networkx.algorithms.isomorphism import GraphMatcher


def get_adj_in_isomorphism(G_main: Graph, isomorphism_nodes: list, node: int) -> List[int]:
    adjacency = list(G_main.adj[node])
    for neighbour in adjacency:
        if neighbour not in isomorphism_nodes:
            adjacency.remove(neighbour)
    return adjacency


def find_isomorphisms(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    GM = GraphMatcher(G_main, G_to_find, node_match=lambda n1, n2: n1['label'] == n2['label'])

    filtered_isomorphisms = []
    for isomorphism in GM.subgraph_isomorphisms_iter():
        if all([isomorphism.keys() != filtered_isomorphism.keys() for filtered_isomorphism in filtered_isomorphisms]):
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms

def are_same_coords(a, b):
    return a[0] == b[0] and a[1] == b[1]

def isomorphism_has_node(G, coords, expected_layer):
    def has_node(isomorphism):
        for a, b in isomorphism.items():
            for node in [a, b]:
                if are_same_coords(G.nodes[node]['pos'], coords) and G.nodes[node]['layer'] == expected_layer:
                    return True

        return False
    return has_node

def isomorphism_is_rotated(G, axis, expected_layer):
    pos_index = 0 if axis == 'x' else 1 if axis == 'y' else None
    def is_rotated(isomorphism):
        vertical_pos = None
        if pos_index is None:
            return False
        for a, b in isomorphism.items():
            for node in [a, b]:
                if G.nodes[node]['layer'] != expected_layer or G.nodes[node]['label'] != 'E':
                    continue
                if vertical_pos is None:
                    vertical_pos = G.nodes[node]['pos'][pos_index]
                elif vertical_pos != G.nodes[node]['pos'][pos_index]:
                    return False
        return True
    return is_rotated

def find_isomorphisms_for_p9(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    isomorphisms = find_isomorphisms(G_main, G_to_find)

    filtered_isomorphisms = []

    for isomorphism in isomorphisms:
        is_correct = True
        E_coeff = set()
        E_nodes = []
        nodes_in_graph = list(isomorphism.keys())
        subgr = G_main.subgraph(nodes_in_graph)
        for node in nodes_in_graph:
            if subgr.nodes[node]['label'] == 'E':
                adjacency = subgr.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if subgr.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    E_coeff.add(tuple(subgr.nodes[node]['pos']))
                    E_nodes.append(node)
        if len(E_coeff) != 3:
            is_correct = False

        if len(E_nodes) != 6:
            is_correct = False

        E_coeff = sorted(list(E_coeff))
        if (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1] and\
                (E_coeff[0][0] + E_coeff[2][0]) / 2 != E_coeff[1][0]:
            is_correct = False

        if (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1]:
            is_correct = False

        for node in E_nodes:
            adjs = [subgr.nodes[adj]['label'] for adj in subgr.adj[node]]
            if (subgr.nodes[node]['pos'] in [E_coeff[0], E_coeff[2]]) and \
                    adjs.count('I') != 1 and adjs.count('E') < 1:
                is_correct = False
            if (subgr.nodes[node]['pos'] == E_coeff[1]) and \
                    adjs.count('I') != 2 and adjs.count('E') < 2:
                is_correct = False
        if is_correct:
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms


def find_isomorphisms_for_p10(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    isomorphisms = find_isomorphisms(G_main, G_to_find)

    filtered_isomorphisms = []

    for isomorphism in isomorphisms:
        is_correct = True
        E_coeff = set()
        E_nodes = []
        nodes_in_graph = list(isomorphism.keys())
        for node in nodes_in_graph:
            if G_main.nodes[node]['label'] == 'E':
                adjacency = G_main.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G_main.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    E_coeff.add(G_main.nodes[node]['pos'])
                    E_nodes.append(node)
        if len(E_coeff) != 3:
            is_correct = False

        if len(E_nodes) != 5:
            is_correct = False

        E_coeff = sorted(list(E_coeff))
        if (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1] and\
                (E_coeff[0][0] + E_coeff[2][0]) / 2 != E_coeff[1][0]:
            is_correct = False

        if (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1]:
            is_correct = False

        for node in E_nodes:
            adjs = [G_main.nodes[adj]['label'] for adj in G_main.adj[node]]
            if (G_main.nodes[node]['pos'] in [E_coeff[0], E_coeff[2]]) and \
                    adjs.count('I') != 1 and adjs.count('E') < 1:
                is_correct = False
            if (G_main.nodes[node]['pos'] == E_coeff[1]) and \
                    adjs.count('I') != 2 and adjs.count('E') < 2:
                is_correct = False
        if is_correct:
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms


def find_isomorphisms_for_p13(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    isomorphisms = find_isomorphisms(G_main, G_to_find)

    filtered_isomorphisms_for_p13 = []

    for isomorphism in isomorphisms:
        is_correct = True
        E_coeff = []
        E_nodes = []
        nodes_in_graph = list(isomorphism.keys())
        for node in nodes_in_graph:
            if G_main.nodes[node]['label'] == 'E':
                adjacency = G_main.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G_main.nodes[neighbour]['label'] == 'i' and neighbour in nodes_in_graph:
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    if tuple(G_main.nodes[node]['pos']) not in E_coeff:
                        E_coeff.append(tuple(G_main.nodes[node]['pos']))
                    E_nodes.append(node)
        if len(E_coeff) != 3:
            is_correct = False
        E_coeff = sorted(E_coeff, key=lambda x: (x[0], x[1]))
        if (E_coeff[0][0] + E_coeff[2][0]) / 2 != E_coeff[1][0] or (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1]:
            is_correct = False
        for node in E_nodes:
            if (G_main.nodes[node]['pos'] == E_coeff[1]) and len(
                    get_adj_in_isomorphism(G_main, nodes_in_graph, node)) != 4:
                is_correct = False
        if is_correct:
            filtered_isomorphisms_for_p13.append(isomorphism)

    return filtered_isomorphisms_for_p13


def find_isomorphisms_for_p15(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    isomorphisms = find_isomorphisms(G_main, G_to_find)
    filtered_isomorphisms_for_p15 = []

    for isomorphism in isomorphisms:
        is_correct = True
        E_coeff = []
        E_nodes = []
        nodes_in_graph = list(isomorphism.keys())
        for node in nodes_in_graph:
            if G_main.nodes[node]['label'] == 'E':
                adjacency = G_main.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G_main.nodes[neighbour]['label'] == 'i' and neighbour in nodes_in_graph:
                        is_connected_to_i = True
                        break
                    
                if not is_connected_to_i:
                    if tuple(G_main.nodes[node]['pos']) not in E_coeff:
                        E_coeff.append(tuple(G_main.nodes[node]['pos']))
                    E_nodes.append(node)
                    
        if len(E_coeff) != 2:
            is_correct = False
            
        for node in E_nodes:
            adjacency = G_main.adj[node]
            pos = tuple(G_main.nodes[node]['pos'])
            for neighbour in adjacency:
                if neighbour in E_nodes and tuple(G_main.nodes[neighbour]['pos']) == pos:
                    is_correct = False
                    break
                
        if is_correct:
            filtered_isomorphisms_for_p15.append(isomorphism)

    return filtered_isomorphisms_for_p15

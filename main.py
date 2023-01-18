import argparse
import sys
from productions import P1, P2, P3, P12, P13, P15
from visualization import draw_graph
import networkx as nx

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
    

def main(args):
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)
    draw_graph(G)

    print("P1", P1.apply(G))
    draw_graph(G)
    print("P3", P3.apply(G))
    draw_graph(G)
    print("P2", P2.apply(G, options={"rotate": True, "apply": isomorphism_has_node(G, (0.0, 0.0), 2)}))
    print("P2", P2.apply(G, options={"rotate": False, "apply": isomorphism_has_node(G, (0.0, 1.0), 2)}))
    print("P12", P12.apply(G, options={"apply": isomorphism_has_node(G, (1.0, 0.0), 2)}))
    print("P2", P2.apply(G, options={"rotate": True, "apply": isomorphism_has_node(G, (1.0, 1.0), 2)}))
    draw_graph(G)
    # print("P13", P13.apply(G, options={}))
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'x', 3)}))
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'x', 3)}))
    draw_graph(G)
    print("P15", P15.apply(G))
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'y', 3)}))
    draw_graph(G)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

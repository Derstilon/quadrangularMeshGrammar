import argparse
import sys

import networkx as nx

from productions import P1, P2, P3, P12, P13, P15, P15p
from productions.utils import isomorphism_has_node, isomorphism_is_rotated
from visualization import draw_graph


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

    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'x', 3)}))
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'x', 3)}))
    draw_graph(G)
    
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'y', 3)}))
    print("P15p", P15p.apply(G))
    draw_graph(G)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

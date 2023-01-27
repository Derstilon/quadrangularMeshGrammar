import argparse
import sys

import matplotlib.pyplot as plt
import networkx as nx

from productions import P1, P2, P4, P9, P13, P15, P15p
from productions.utils import isomorphism_has_node, isomorphism_is_rotated
from visualization import draw_graph


def main(args):
    print("Step 0/6")
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)
    # plt.subplot(231)
    # draw_graph(G)
    
    plt.subplots_adjust(left=0.15, right=0.85, bottom=0, top=0.96, wspace=0.32, hspace=0.05)

    print("\nStep 1/6")
    print("P1", P1.apply(G))
    ax = plt.subplot(231)
    ax.set_title('P1')
    draw_graph(G, None, False)
    # draw_graph(G)

    print("\nStep 2/6")
    print("P2 normal", P2.apply(G))
    ax = plt.subplot(232)
    ax.set_title('P2')
    draw_graph(G, None, False)
    # draw_graph(G)

    print("\nStep 3/6")
    print("P2 rotated", P2.apply(G, options={"rotate": True, "apply": isomorphism_has_node(G, (0.0, 0.0), 2)}))
    print("P2 normal", P2.apply(G))
    ax = plt.subplot(233)
    ax.set_title('P2, P2')
    draw_graph(G, None, False)
    # draw_graph(G)

    print("\nStep 4/6")
    print("P13", P13.apply(G, options={"apply": isomorphism_is_rotated(G, 'y', 2)}))
    ax = plt.subplot(234)
    ax.set_title('P13')
    draw_graph(G, None, False)
    # draw_graph(G)

    print("\nStep 5/6")
    print("P4 ", P4.apply(G))
    print("P2 normal", P2.apply(G, options={"rotate": False, "apply": isomorphism_has_node(G, (0.0, 0.0), 3)}))
    print("P2 normal", P2.apply(G, options={"rotate": False, "apply": isomorphism_has_node(G, (0.0, 1.0), 3)}))
    print("P2 roatated", P2.apply(G, options={"rotate": True, "apply": isomorphism_has_node(G, (1.0, 0.0), 3)}))
    ax = plt.subplot(235)
    ax.set_title('P4, P2, P2, P2')
    draw_graph(G, None, False)
    # draw_graph(G)

    print("\nStep 6/6")
    print("P9 ", P9.apply(G))
    print("P15", P15.apply(G))
    print("P15p", P15p.apply(G))
    print("P15", P15.apply(G))
    print("P15p", P15p.apply(G))
    # print("P9 ", P9.apply(G))
    # print("P9 ", P9.apply(G))
    ax = plt.subplot(236)
    ax.set_title('P9, P15, P15p, P15, P15p')
    draw_graph(G, None, False)
    # draw_graph(G)

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

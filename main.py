import argparse
import sys

import networkx as nx

from productions import P1, P5
from visualization import draw_graph


def main(args):
    # p2.show()
    # p12.show_prim()

    # G = nx.Graph()
    # G.add_node(1, label='El', pos=(0, 0), layer=0)
    #
    # P1.apply(G)
    # P5.apply(G)

    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)
    G.add_node(3, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(4, label='E', pos=(0, 1), layer=0)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    G.add_edge(2, 3)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(2, 6)
    G.add_edge(4, 6)

    G.add_node(6, label='E', pos=(0, 0.5), layer=0)
    #
    P5.apply(G)

    draw_graph(G)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

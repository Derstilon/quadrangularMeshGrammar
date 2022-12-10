import argparse
import sys
import matplotlib.pyplot as plt
import networkx as nx
from productions import P1, P2
from visualization import draw_graph


def main(args):
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    P1.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)

    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)

    draw_graph(G)
    # draw_graph(G, 2) # draw layer 1

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

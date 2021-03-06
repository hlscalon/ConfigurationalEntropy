import sys

import matplotlib.pyplot as plt
import networkx as nx

G = nx.grid_2d_graph(5, 5)  # 5x5 grid
try:  # Python 2.6+
    nx.write_adjlist(G, sys.stdout)  # write adjacency list to screen
except TypeError:  # Python 3.x
    nx.write_adjlist(G, sys.stdout.buffer)  # write adjacency list to screen
# write edgelist to grid.edgelist
nx. write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

nx.draw(H)
plt.show()

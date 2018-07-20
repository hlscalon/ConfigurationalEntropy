import boost_graph

g = boost_graph.Graph()
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(6, 7)
g.add_node(10)
print g.has_node(2)
print g.has_node(8)
print g.has_neighbor(2, 3)
print g.has_neighbor(6, 7)
print g.has_neighbor(2, 5)
print g.has_neighbor(4, 4)
g.printG()

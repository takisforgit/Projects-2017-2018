import matplotlib.pyplot as plt
import networkx as nx

labels = {}
edge_colors = []


def draw1(G, title ):
	# positions for all nodes
	pos = nx.shell_layout(G)
	## nodes
	nx.draw_networkx_nodes(G, pos, node_size=700)
	## edges
	nx.draw_networkx_edges(G, pos)
	## labels
	nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
	plt.axis('off')
	plt.title(title)
	plt.draw()
	plt.pause(0.5)


def draw2(G, title):
	# positions for all nodes
	nx.draw_networkx(G, font_size=16, node_size=500, font_family='sans-serif')
	plt.axis('off')
	plt.title(title)
	plt.draw()
	plt.pause(0.5)



G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3,4,5])
draw2(G,'Title 1')
plt.clf()



H=nx.path_graph(10)
# print(H.nodes(),"\n",H.edges())



G.add_nodes_from(H)
draw1(G,'G.add_nodes_from(H)')
plt.clf()

G.add_node(H)
draw1(G,'H as a node)')
plt.clf()


G3 = nx.grid_2d_graph(2, 3, periodic=False, create_using=None )
# print(G3.nodes(),"\n",G3.edges())
draw2(G3,'grid_2d_graph')
plt.clf()



G4 = nx.balanced_tree(2, 4, create_using=None)
# print(G4.nodes(),"\n",G4.edges())
draw2(G4,'balanced_tree')
plt.clf()


# ## One can demolish the graph in a similar fashion;
# ## using Graph.remove_node(), Graph.remove_nodes_from(),
# ## Graph.remove_edge() and Graph.remove_edges_from(), e.g.

G=nx.Graph()

G.add_edges_from([(1,2),(1,3),(3,4),(4,2),(5,3),(2,8)])
G[1][2]['color']='red'
G[1][3]['color']='blue'
G[1][2]['weight'] = 4.7
G.add_node("spam")       # adds node "spam"
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'

e=(2,3)
G.add_edge(*e) # unpack edge tuple*

# print( G.nodes(), G.edges(),  G.neighbors(1) )

# print("EDGES:",list(G.edges(data=True)))
# for x in G.edges():
# 	print(x)

print("--------------------\n")
#for n,nbrs in G.adjacency():
#	print(n,nbrs)
	# for nbr,eattr in nbrs.items():
	# 	print('(%d, %s)' % (nbr,eattr))





draw1(G,'Edges Added')
plt.show()




# G.nodes()

# G.remove_edge(1,3)

# ## You can safely set the attributes of an edge using subscript notation
# ## if the edge already exists.

# G.add_edge(1,3)
# G[1][3]['color']='blue'


# ## Fast examination of all edges is achieved using adjacency iterators.
# ## Note that for undirected graphs this actually looks at each edge twice.

# # FG=nx.Graph()
# # FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
# # for n,nbrs in FG.adjacency_iter():
# # 	for nbr,eattr in nbrs.items():
# 		data=eattr['weight']
# 		if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))


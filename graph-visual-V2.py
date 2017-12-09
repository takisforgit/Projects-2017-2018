####
## graph-visual1.py
## Simple Graph Visualization
####

import networkx as nx
import matplotlib.pyplot as plt
#import matplotlib.animation
from matplotlib.pyplot import pause


graph = {
0: [1,5],
1: [0,2,3,6],
2: [1,4,6],
3: [1,4,5,6],
4: [2,3,5],
5: [0,3,4],
6: [1,2,3]
}


## extract nodes from graph
nodes = [node for node in graph]
# print("Nodes:",nodes)

edges = [graph[node] for node in graph]
# print("Per Node Edges List:",edges)

labels = {}
edge_colors = []

## create networkx graph
G=nx.Graph()
## add nodes
for node in nodes:

	# numOfNeigbors = len(graph[node])
	# print("Neighbors of node",node,":", end=" ")
	# print(edges[node])
	G.add_node(node)
	# Add label to each node
	labels[node] = node

## add edges
	for n in edges[node]:
		# print(node,"-->",n)
		G.add_edge(node,n,  edge_color='grey')

## Update edge colors
edge_colors = [e[2]['edge_color'] for e in G.edges(data=True)]

# print(labels)
print(G.nodes)
print(G.edges)
# print(edge_colors)

#### Print Initial Edge colors
# for e in G.edges(data=True):
# 	print(e, e[2]['edge_color'] )


## positions for all nodes
pos = nx.shell_layout(G)
## nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
## edges
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=G.edges(), width=2)
## labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

## show graph


plt.axis('off')
plt.title("Simple Graph Visualization")
plt.draw()
pause(2.5)




########### DFS iteratively ##############
def dfs_iteratively(graph, root):

	global edge_colors, visited, nodes_not_visited

	visited = []
	stack = [root]
	nodes_not_visited = []

	while stack:

		# Pop the LAST item in stack
		node = stack.pop()
		print("Popping Node:", node)

		# node.node_color = '#A0CBE2'

		if node not in visited:
			visited.append(node)
			print("Visited Nodes:",visited)
			print("Neighbors of Node",node,":",list( G.neighbors(node)))
			###


			# For all Neighbors of the node
			for x in list( G.neighbors(node)):
				if x not in visited:
					# Add NOT visited Neighbors to the stack
					stack.append(x)
				else:
					print("From Nodes", list( G.neighbors(node)) ,"Already VISITED:",x)
					G.add_edge(node,x, edge_color='red')
					## Update edge colors
					# edge_colors = [e[2]['edge_color'] for e in G.edges(data=True)]

					# for e in G.edges(data=True):
					# 	print(e, e[2]['edge_color'] )

			print("Stack:",stack)
			## Get list of nodes not yet visited, to draw in original color
			nodes_not_visited = list(set(nodes).difference(visited))
			# print("Not_Visited yet:",nodes_not_visited)

			## positions for all nodes
			pos = nx.shell_layout(G)

			## nodes
			## if node in visited , draw in othet color :
			nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color="green", node_size=700)
			nx.draw_networkx_nodes(G, pos, nodelist=nodes_not_visited,  node_color="red", node_size=400)

			## edges
			nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=G.edges(data=True), width=2)
			## labels
			nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

			## show graph
			plt.axis('off')
			plt.title("Simple Graph Visualization\n"+"Visiting node:"+str(node) )
			## Redraw figure with changes
			plt.draw()
#			plt.show()
			pause(2.5)




	print("Stack is EMPTY. We have visited ALL nodes !")
	return visited



print("DFS iteratively: ",dfs_iteratively(graph,0))


######################################
### Print ONLY the DFS path  ###
dfs_path = []
edge_colors = []

for n in visited:
	if(visited.index(n)+1 < len(visited)):
		# print(n, visited[visited.index(n)+1] )
		dfs_path.append((n, visited[visited.index(n)+1]))
		G.add_edge(n, visited[visited.index(n)+1] , edge_color='blue')

# print(dfs_path)
# print(edge_colors)

## positions for all nodes
pos = nx.shell_layout(G)

## nodes
## if node in visited , draw in othet color :
nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color="green", node_size=700)

for n in visited:
	if(visited.index(n)+1 < len(visited)):
		# print(n, visited[visited.index(n)+1] )
		dfs_path.append((n, visited[visited.index(n)+1]))
		G.add_edge(n, visited[visited.index(n)+1] , edge_color='red')
		edge_colors.append('red')
		edge_colors.append('red')

# print(edge_colors)
## edges
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=dfs_path, width=2)
## labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

## show graph
plt.axis('off')
t = str(visited)
plt.title("FINAL DFS PATH : "+t)
plt.show()
####
## graph-visual-V5.py
## DFS Graph Visualization
####

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import pause
from random import shuffle

from networkx.drawing.nx_agraph import graphviz_layout


graph = {
0: [1,2],
1: [0,3,4],
2: [0,5,6],
3: [],
4: [],
5: [7,8,11,20],
6: [9,10]
}



## extract nodes from graph
nodes = [key for key in graph]
edges = [graph[key] for key in graph]
# print("Per Node Edges List:",edges)

labels = {}
edge_colors = []
node_colors = []
initial_color= 'r'
node_colors2 = ""

## create networkx graph
G=nx.Graph()
## add nodes
for node in nodes:

    G.add_node(node)
    # Add label to each node
    labels[node] = node

    ## Add edges
    for n in edges[node]:
        G.add_edge(node,n)

print(G.nodes())
print(G.edges())

## Set initial Color to ALL nodes
for i in range(len(G.nodes())) :
    node_colors.append(initial_color)


print(node_colors)

#############################################################
#------------- Graphviz Layout --------------#
nx.draw_networkx(G, pos=graphviz_layout(G), node_size=800,node_color=node_colors, 
       font_size=12, prog='neato')
plt.axis('off')
plt.title("DFS of a Graphn" )
plt.draw()
pause(2.5)
#plt.show()
#plt.clf()
############################################################

########### DFS iteratively ##############
def dfs_iteratively(graph, root):

    global edge_colors, node_colors , node_colors2, visited, nodes_not_visited

    visited = []
    stack = [root]
    nodes_not_visited = []

    while stack:

        ## Pop the LAST item in stack
        node = stack.pop()
        print("Popping Node:", node)
        ## Change color of popped Node
        idx =list(G.nodes()).index(node)
        
        print("index of {} is {}".format(node, idx) )
        node_colors[idx] = 'g'
        ## Convert FROM List TO String !!!
        node_colors2 = "".join(node_colors)  
        ## Convert back FROM String TO List !!!
        node_colors = list(node_colors2)


        if node not in visited:
            visited.append(node)
            print("Visited Nodes:",visited)
            print("Neighbors of Node",node,":",list( G.neighbors(node)))

###-----------------------------------------------------------###
### Only for checking - use Random choice of neighbors ####           
            geitones = list( G.neighbors(node))
            ## Shuffle list of neighbors ##
            print("Geitones", geitones)
            shuffle(geitones)
            print("Shuffled Geitones", geitones)
            geitones.reverse()
###-----------------------------------------------------------###

            # For all Neighbors of the node
            for x in geitones :
                if (x not in visited) and (x not in stack) :
                    # Add NOT visited Neighbors to the stack
                    stack.append(x)
                else:
                    print("From Nodes", list( G.neighbors(node)) ,"Already VISITED:",x)
#                    G.add_edge(node,x, edge_color='red')
               

        print("Stack:",stack)
        plt.draw()
        pause(2.5)
   
 
        ## show graph
        plt.axis('off')
        plt.title("DFS of a Graph\n"+"Visiting node:"+str(node) )
        ## Redraw figure with changes
#############################################################
        #------------- Graphviz Layout --------------#
        nx.draw_networkx(G, pos=graphviz_layout(G), node_size=800, 
               node_color=node_colors , font_size=12, prog='neato')
        plt.axis('off')
        plt.draw()
        pause(2.5)

############################################################
    print("Stack is EMPTY. We have visited ALL nodes !")
    return visited


#--------------------------------------------------------------#
#----- Main program -------------#
print("DFS iteratively: ",dfs_iteratively(graph,0))

### Print ONLY the DFS path  ###
dfs_path = []
edge_colors = []
#############################################################
#------------- Graphviz Layout --------------#
nx.draw_networkx(G, pos=graphviz_layout(G), node_size=800,
         node_color=node_colors, font_size=12, prog='dot')
plt.axis('off')
plt.draw()
pause(2.5)

############################################################
## show graph
t = str(visited)
plt.title("We have visited ALL nodes!\nDFS PATH : "+t[1:-1])

#------------- Graphviz Layout --------------#
nx.draw_networkx(G, pos=graphviz_layout(G), node_size=800,  node_color=node_colors , font_size=12, prog='dot')
plt.axis('off')
plt.draw()
pause(2.5)
##-----------------------------------##
############################################################

plt.show()
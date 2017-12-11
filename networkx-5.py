# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:23:47 2017

@author: takis
"""

#from networkx.drawing.nx_agraph import graphviz_layout
##import graphviz
#import networkx as nx
#G = nx.Graph()
#G.add_node("ROOT")
#
#for i in range(5):
#    G.add_node("Child_%i" % i)
#    G.add_node("Grandchild_%i" % i)
#    G.add_node("Greatgrandchild_%i" % i)
#    G.add_edge("ROOT", "Child_%i" % i)
#    G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
#    G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)
#
#
#A= nx.nx_agraph.to_agraph(G)
#A.layout('dot', args='-Nfontsize=10 -Nwidth=".2" -Nheight=".2" -Nmargin=0 -Gfontsize=8')
#A.draw('test.png')
#



import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from networkx.drawing.nx_agraph import write_dot


G = nx.DiGraph()

G.add_node("ROOT")

for i in range(5):
    G.add_node("Child_%i" % i)
    G.add_node("Grandchild_%i" % i)
    G.add_node("Greatgrandchild_%i" % i)

    G.add_edge("ROOT", "Child_%i" % i)
    G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
    G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
#write_dot(G,'test.dot')

# same layout using matplotlib with no labels
plt.title('draw_networkx')
#pos=graphviz_layout(G, prog='dot')
nx.draw_networkx(G,  pos=graphviz_layout(G), prog='dot')
#plt.savefig('nx_test.png')
plt.draw()
plt.show()

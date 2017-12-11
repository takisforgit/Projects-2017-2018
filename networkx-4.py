#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:03:59 2017

@author: takis
"""
#import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt

## Examples
#G = nx.complete_graph(7)
#A = nx.nx_agraph.to_agraph(G)
#H = nx.nx_agraph.from_agraph(A)
#
#nx.draw(H)
#plt.draw()
#plt.show()

## Examples
#G = nx.complete_graph(5)
#A = nx.nx_agraph.to_agraph(G)
#H = nx.nx_agraph.from_agraph(A)


## Examples
G = nx.petersen_graph()
pos = nx.nx_agraph.graphviz_layout(G)
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
nx.draw(G,pos)
plt.draw()
plt.show()











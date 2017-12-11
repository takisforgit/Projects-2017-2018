#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:25:50 2017

@author: takis
"""

import pygraphviz as pgv

#G=pgv.AGraph()
G=pgv.AGraph(strict=False,directed=True)

#G=pgv.AGraph('graph {1 - 2}')
d={'1': {'2': None}, '2': {'1': None, '3': None}, '3': {'2': None}}

A=pgv.AGraph(d)
G.graph_attr['label']='Name of graph'

G.add_node('a') # adds node 'a'
G.add_edge('b','c') # adds edge 'b'-'c' (and also nodes 'b', 'c')
G.add_edge('a','d')
G.add_edge('a','b')
G.add_edge('b','d')

G.node_attr['shape']='circle'
G.edge_attr['color']='red'

n=G.get_node('a')
n.attr['shape']='ellipse'

s=G.string()
print(s)

G.write("file1.dot")

G.layout() # default to neato
#G.layout(prog='dot') # use dot

G.draw('file1.dot')  # write previously positioned graph to PNG file
G.draw('file1.ps',prog='circo') # use circo to position, write PS file

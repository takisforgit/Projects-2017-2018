import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Optionnal if you want to animate in your notebook
# from JSAnimation import IPython_display

def update_func(step, data, nodes):
    # the step parameter is mandatory for matplotlib
    # Set new value for figure data
    # update node color here
    new_data = data + 1
    nodes.set_array(new_data)
    return nodes

def diffuse_anim(inputs, G, data, nb_frames=50):
    fig = plt.figure()
    nodes = nx.draw_networkx_nodes(G, pos, node_size=30, node_color='b')
    return animation.FuncAnimation(fig, update_func, frames=xrange(nb_frames), fargs=(data, nodes))
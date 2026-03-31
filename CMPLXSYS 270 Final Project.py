import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv

# Read CSV file into a list of dictionaries
with open('CMPLXSYS 270 Final Project data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    edges = [(row['Departing Airport Code'], row['Arriving Airport Code'], float(row['Length'])) for row in reader]

# Create a directed graph
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# Use Kamada-Kawai layout with edge weights
pos = nx.kamada_kawai_layout(G, dist['Departing Airport Code']['Arriving Airport Code'] = ['length'], weight='weight')

# Extract edge distances as a dictionary
edge_distances = nx.get_edge_attributes(G, 'weight')

# Draw the graph with edge distances as labels
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', arrowsize=20, connectionstyle='arc3,rad=0.1')

# Draw edge labels with distances
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_distances)

plt.show()


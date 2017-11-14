import numpy as np
import pandas as pd

class Graph:
	""" creat a graph using data frames """
	def __init__(self, num_nodes, index=None, directed=False):
		
		self.num_nodes 	= num_nodes
		self.directed = directed
		# list of strings for indices (rows & columns)
		self.index 	= index		 
		# initialize the dataFrame/graph 
		self.graph = pd.DataFrame(
			np.zeros(self.num_nodes*self.num_nodes
				).reshape(self.num_nodes, self.num_nodes),
				self.index, self.index)

	def add_edge(self, fst_node, snd_node, weight=1):

		self.graph.loc[fst_node,snd_node] = weight
		if self.directed == False:
			self.graph.loc[snd_node,fst_node] = weight

	def get_weight(self, fst_node, snd_node):
		return self.graph.loc[fst_node,snd_node]

	def get_adjacents(self, node):
		return self.graph.columns[(self.graph.loc[node] > 0)]
		
	def display(self):
		print(self.graph)
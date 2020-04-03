# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:44:28 2020

@author: tm_sh
"""

# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 

import sys # Library for INT_MAX 

class Graph(): 

	def __init__(self, vertices):  
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	# A utility function to print the constructed MST stored in parent[], according to numerical order
	def printMST(self, parent): 
		print ("Edge \tWeight")
		for i in range(1, self.V): 
			print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ],'\n') 

	# A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree 
	# key[v] is the closest dist from a point to no.v point
	def minKey(self, key, mstSet): 

		# Initilaize min value 
		min = sys.maxsize 

		for v in range(self.V): 
			if key[v] < min and mstSet[v] == False: 
				min = key[v] 
				min_index = v 
				print ("minkey在v=",v,"次的输出是min=",min,"与min_index=",min_index,'\n')

		return min_index 

	# Function to construct and print MST for a graph 
	# represented using adjacency matrix representation 
	def primMST(self): 

		# Key values used to pick minimum weight edge in cut 
		key = [sys.maxsize] * self.V   #initially key is all INF, if a road is built up, then update it in update block
		parent = [None] * self.V # Array to store constructed MST 
		# Make key 0 so that this vertex is picked as first vertex 
		key[0] = 0
		mstSet = [False] * self.V   #boolean array used to judge whether vertices are included in shortest path tree

		parent[0] = -1 # First node is always the root of 

		for cout in range(self.V): 

			# Pick the minimum distance vertex from the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			print ("在cout=",cout,"时")
			u = self.minKey(key, mstSet) 

			# Put the minimum distance vertex in the shortest path tree 
			mstSet[u] = True
            
			# This is update block
            
			# Update dist value of the adjacent vertices of the picked vertex 
            # only if the current distance is greater than new distance and the vertex in not in the shotest path tree 
			for v in range(self.V): 
				# graph[u][v] is non zero only for adjacent vertices of m 
				# mstSet[v] is false for vertices not yet included in MST 
				# Update the key only if graph[u][v] is smaller than key[v] 
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
						key[v] = self.graph[u][v] 
						parent[v] = u 
						print ("update块的","v是",v,"时","update块的key[v]是",key[v],"parent[v]是",parent[v],'\n')

		self.printMST(parent) 
print ("example #1",'\n')
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 

g.primMST(); 
print ("example #2",'\n')
g = Graph(5) 
g.graph = [ [0, 2, 0, 8, 0], 
			[2, 0, 3, 6, 5], 
			[0, 3, 0, 0, 7], 
			[8, 6, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 

g.primMST(); 
print ("example #3",'\n')
g = Graph(6) 
g.graph = [ [0,7,4,0,0,0],   
                    [7,0,6,2,0,4], 
                    [4,6,0,0,9,8], 
                    [0,2,0,0,0,7], 
                    [0,0,9,0,0,1], 
                    [0,4,8,7,1,0]]
g.primMST(); 
# Contributed by Divyanshu Mehta 

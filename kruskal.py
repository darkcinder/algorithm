# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = [] # default dictionary 
								# to store graph 


	# function to add an edge to graph 
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w])  #The append() method adds an item to the end of the list.

	# A utility function to find set of an element i 
	# (uses path compression technique) 
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1
			print ("if x != y而且xroot=",xroot,"yroot=",yroot,"rank相同, 把parent[y的parent] 替换为 x的parent,","rank是",rank,'\n')
	# The main function to construct MST using Kruskal's 
		# algorithm 
	def KruskalMST(self): 

		result =[] #This will store the resultant MST 

		i = 0 # An index variable, used for sorted edges 
		e = 0 # An index variable, used for result[] 

			# Step 1: Sort all the edges in non-decreasing 
				# order of their 
				# weight. If we are not allowed to change the 
				# given graph, we can create a copy of graph 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 
		print ("self.graph是",self.graph,'\n')

		parent = [] ; rank = [] 

		# Create V subsets with single elements 
        # this is MakeSet(X)
		for node in range(self.V): 
			parent.append(node)     #parent is [0, 1, 2, 3]
			rank.append(0)          #rank is [0, 0, 0, 0]
		# Number of edges to be taken is equal to V-1 
		while e < self.V -1 : 

			# Step 2: Pick the smallest edge and increment 
					# the index for next iteration 
            # for each e th, pick up one acceptable edge         
			u,v,w = self.graph[i] 
            # for each i th, pick up one possible edge   
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v)
			print ("当e=",e,"时","i=",i-1,"时",'\n')
			print ("x是",x,'\n',"y是",y,'\n')
			# If including this edge does't cause cycle, 
						# include it in result and increment the index 
						# of result for next edge 
            # 如果u的parent=v的parent，说明成环            
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
				print ("if x != y,","parent是",parent,'\n')
            # Else discard the edge 

		# print the contents of result[] to display the built MST 
		print ("Following are the edges in the constructed MST")
		for u,v,weight in result: 
			#print str(u) + " -- " + str(v) + " == " + str(weight) 
			print ("%d -- %d == %d" % (u,v,weight)) 

# Driver code 
g = Graph(4)          #input sum. of vertices
g.addEdge(0, 1, 10)   #input edges and weight
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST() 

#This code is contributed by Neelam Yadav 

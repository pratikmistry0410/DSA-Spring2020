from collections import defaultdict
from queue import PriorityQueue                    # Use of priority queue referred from https://www.educative.io/edpresso/what-is-the-python-priority-queue
from time import time

# Undirected Weighted Edge Class
class WeightedEdge():
    def __init__(self,u,v,weight):              # Default Constructor for initializing the Weighted Edge Class private variables
        self.__u = u
        self.__v = v
        self.__weight = weight
    
    def either(self):                           # Function to return first vertex
        return self.__u
    
    def other(self,vertex):                     # Function to return other vertex
        if vertex == self.__u: 
            return self.__v
        return self.__u
    
    def edgeWeight(self):                       # Function to return edge weight
        return self.__weight

# Undirected Graph Class
class Graph():                                      # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __V = 0
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                           # Default Constructor to initialize graph with number of vertices
        self.__V = V
    
    def addEdge(self,edge):                         # Function to add edge in the graph
        u = edge.either()
        v = edge.other(u)
        if edge not in self.__graph[u][::]:
            self.__graph[u].append(edge)            # Insert the edge at source vertex
            self.__graph[v].append(edge)            # Insert the edge at destination vertex because its undirected graph
            self.__E+=1
    
    def V(self):                                    # Function to return vertices count
        return self.__V

    def E(self):                                    # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):                      # Function to return adjacency list i.e. edgelists at given vertex
        return self.__graph[V]

    def edges(self):                                # Function to return list of all the graph edges in format - (weight,(u,v))
        graph_edges = []
        for vertex,edgelist in self.__graph.items():
            for edge in range(len(edgelist)):
                u = edgelist[edge].either()
                v = edgelist[edge].other(u)
                weight = edgelist[edge].edgeWeight()
                if (weight,(u,v)) not in graph_edges:
                    graph_edges.append((weight,(u,v)))
        return graph_edges 

# Kruskal's MST Class   -   Implementation Idea is referred from lecture slides
class KruskalMST():
    def __init__(self,graph):                       # Default constructor to Initialize private variables and execute Kruskal's algorithm to Find MST edges
        self.__mst = []                             # Array to store MST edges
        self.__pq = PriorityQueue()                 # Priority queue to store graph edges with minimum weight on top
        edges = graph.edges()                       # Get graph edges in format - (weight,(u,v))
        for e in edges:
            self.__pq.put(e)                        # Insert each graph edge in minimum priority queue
    
        uf = UnionFind(graph.V())                   # creating object of union-find used for finding MST edges

        # While priority queue is not empty and MST list has less than V-1 edges
        while not self.__pq.empty() and len(self.__mst) < graph.V()-1:              
            e = self.__pq.get()                     # Get the min edge from PQ
            u = e[1][0]                             # Extract U and V
            v = e[1][1]
            if not uf.isConnected(u,v):             # Check whether U and V is connected 
                uf.union(u,v)                       # union U and v if not connected
                self.__mst.append(e)                # Append the edge to the list 

    def mst_edges(self):                            # Return list of MST edges - (Weight,(U,V))
        return self.__mst

# Union Find class 
class UnionFind():
    __inputArray = []                               # Array for denoting the connections between two elements/nodes
    def __init__(self,total_vertices):              # Default constructor to initialize the array with V vertices
        for i in range(total_vertices):
            self.__inputArray.append(i)             # Initializing the array based on the index numbers
    
    def isConnected(self,index1,index2):            # Function to find whether the elements/pairs are connected i.e both has same index numbers
        if self.__inputArray[index1] == self.__inputArray[index2]:
            return True
        return False
    
    def union(self,index1,index2):                  # Function to connect/union if two elements/pairs are not connected 
        num1 = self.__inputArray[index1]
        num2 = self.__inputArray[index2]

        for i in range(len(self.__inputArray)):             # Traverse through entire array
            if self.__inputArray[i] == num1:                # If the number associated with first location of the pair is encountered
                self.__inputArray[i] = num2				    # assign the number associated with the second location of the pair		

# Driver/Main Function
if __name__ == "__main__":
    file = open("mediumEWG.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    undirectedGraph = Graph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on space
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = WeightedEdge(u,v,weight)     # Create weighted edge object
        undirectedGraph.addEdge(edge)       # Add edge to graph

    start_time = time()
    kmst = KruskalMST(undirectedGraph)      # Execute the Kruskal MST on graph 
    mst_edges = kmst.mst_edges()            # Get the MST edges
    end_time = time()
    
    # print("The MST Edges are: ")          # Uncomment to print the MST Edges
    mst_weight = 0
    for edge in mst_edges:                  # Print the MST edges and MST weight
        mst_weight += edge[0]
        # print(edge)                       # Uncomment to print the MST edges
    print("Weight of MST for the graph is: ", mst_weight,"\n")
    print("Time taken to run Kruskal's algorithm for Minimum Spanning Tree is: ",end_time-start_time, "seconds \n")
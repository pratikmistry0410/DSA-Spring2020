from collections import defaultdict
from queue import PriorityQueue                         # Use of priority queue referred from https://www.educative.io/edpresso/what-is-the-python-priority-queue
from time import time

# Undirected Weighted Edge Class
class WeightedEdge():
    def __init__(self,u,v,weight):          # Default Constructor for initializing the Weighted Edge Class private variables
        self.__u = u
        self.__v = v
        self.__weight = weight
    
    def either(self):                       # Function to return first vertex
        return self.__u 

    def other(self,vertex):                 # Function to return other vertex
        if vertex == self.__u: 
            return self.__v
        return self.__u
    
    def edgeWeight(self):                   # Function to return edge weight
        return self.__weight

# Undirected Graph Class
class Graph():                                          # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __V = 0
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                               # Default Constructor to initialize graph with number of vertices
        self.__V = V
    
    def addEdge(self,edge):                             # Function to add edge in the graph
        u = edge.either()
        v = edge.other(u)
        if edge not in self.__graph[u][::]:
            self.__graph[u].append(edge)                # Insert the edge at source vertex
            self.__graph[v].append(edge)                # Insert the edge at destination vertex because its undirected graph
            self.__E+=1
    
    
    def V(self):                                        # Function to return vertices count
        return self.__V

    def E(self):                                        # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):                          # Function to return adjacency list i.e. edgelists at given vertex
        return self.__graph[V]

    def edges(self):                                    # Function to return list of all the graph edges in format - (weight,(u,v))
        graph_edges = []
        for vertex,edgelist in self.__graph.items():
            for edge in range(len(edgelist)):
                u = edgelist[edge].either()
                v = edgelist[edge].other(u)
                weight = edgelist[edge].edgeWeight()
                if (weight,(u,v)) not in graph_edges:
                    graph_edges.append((weight,(u,v)))
        return graph_edges
 
# Prim's MST Class   -   Implementation Idea is referred from lecture slides
class PrimMST():
    def __init__(self,graph):                           # Default constructor to Initialize private variables and execute Prim's algorithm to find MST edges
        self.__mst = []                                 # Array to store MST edges
        self.__pq = PriorityQueue()                     # Priority queue to store graph edges with minimum weight on top
        self.__marked = [False]*graph.V()               # Private Boolean array of size V for storing whether the vertex is VISITED or not
        self.__visit(graph,0)                           # Visit vertex 0 and add adjancent edges in the Priority Queue

        # While priority queue is not empty and MST list has less than V-1 edges
        while not self.__pq.empty() and len(self.__mst) < graph.V()-1:
            e = self.__pq.get()                         # Get the min edge from PQ
            u = e[1][0]                                 # Extract U and V
            v = e[1][1]
            
            if self.__marked[u] and self.__marked[v]:   # If both the vertices are not visited, continue with other edge
                continue
            self.__mst.append(e)                        # Append edge in MST list
            if not self.__marked[u]:                    # If U is not visited, visit the vertex and add edges adjacent to it in Priority Queue
                self.__visit(graph,u)
            if not self.__marked[v]:                    # If U is not visited, visit the vertex and add edges adjacent to it in Priority Queue
                self.__visit(graph,v)
            

    def __visit(self,graph,vertex):                     # Function to visit the vertex and add the adjacent edges in Priorit Queue
        self.__marked[vertex] = True
        edgeList = graph.adjacencyList(vertex)
        for edge in range(len(edgeList)):
            u = edgeList[edge].either()
            v = edgeList[edge].other(u)
            weight = edgeList[edge].edgeWeight()        
            if not self.__marked[v] or not self.__marked[u]:    # VERY IMPORTANT: If any of the vertex of edge is not visited, add the edge to Priority Queue
                self.__pq.put((weight,(u,v)))

    def mst_edges(self):                                        # Return list of MST edges - (Weight,(U,V))
        return self.__mst
        
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
    pmst = PrimMST(undirectedGraph)         # Execute the Prim's MST on graph
    mst_edges = pmst.mst_edges()            # Get the MST edges
    end_time = time()

    # print("The MST Edges are: ")          # Uncomment to print the MST edges
    mst_weight = 0
    for edge in mst_edges:                  # Print the MST edges and MST weight
        mst_weight += edge[0]    
        # print(edge)                       # Uncomment to print the MST edges
    print("Weight of MST for the graph is: ", mst_weight,"\n")
    print("Time taken to run Prims's algorithm (Lazy Approach) for Minimum Spanning Tree is: ",end_time-start_time, "seconds \n")
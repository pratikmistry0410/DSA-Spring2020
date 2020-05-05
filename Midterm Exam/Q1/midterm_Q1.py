from collections import defaultdict
from queue import PriorityQueue
import heapq
import sys

sys.setrecursionlimit(1000000000)             # Setting Maximum recursion depth limit to avoid recursion depth limit erro

# DirectedWeightedEdge Class
class DirectedWeightedEdge():                 # Default Constructor for initializing the Weighted Edge Class variables 
    def __init__(self,u,v,weight):                      
        self.__u = u
        self.__v = v
        self.__weight = weight
    
    def fromVertex(self):                       # Function to return source vertex
        return self.__u
    
    def toVertex(self):                         # Function to return destination vertex
        return self.__v
    
    def edgeWeight(self):                       # Function to return edge weight
        return self.__weight

# Directed Weighted Graph Class
class DirectedGraph():                        # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __V = 0
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                       # Default Constructor to initialize graph with number of vertices
        self.__V = V
    
    def addEdge(self,edge):                     # Function to add edge in the graph
        u = edge.fromVertex()
        v = edge.toVertex()
        if edge not in self.__graph[u][::]:
            self.__graph[u].append(edge)        # Insert the edge at vertex of origination
            self.__E+=1                         
    
    def V(self):                                # Function to return vertices count
        return self.__V

    def E(self):                                # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):                  # Function to return adjacency list i.e. edgelists at given vertex
        return self.__graph[V]

    def printGraph(self):                       # Function to print graph
        for vertex,edgelist in self.__graph.items():
            for edge in range(len(edgelist)):
                u = edgelist[edge].fromVertex()
                v = edgelist[edge].toVertex()
                print(u ,"->", v, edgelist[edge].edgeWeight())

# Dijkstra Class
class Dijkstra():
    def __init__(self,graph,s):                     # Default constructor
        self.__edgeTo = {}                          # Edge to dictionary to hold edge from where it is travelled to each vertices
        self.__distTo = [float('inf')]*graph.V()    # Initializing Distance to each vertex as INFINITY which will later hold shortest distance to visit each vertex
        self.__heap = []                            # Min Heap to store the edges with minimum priority first i.e. minimum vertex on top
        self.__source = s                           # Source vertex variable

        self.__distTo[self.__source] = 0.0                      # distance to source vertex is 0
        self.__edgeTo[self.__source] = DirectedWeightedEdge(0,0,0.0)    # edge to source vertex is considered 0
        heapq.heappush(self.__heap,(self.__source,0.0))         # pushing source vertex and minimum distance in min heap

        while len(self.__heap):                     # While heap has vertex
            edge = heapq.heappop(self.__heap)       # Remove the min vertex from heap
            vertex = edge[0]                        # Extract vertex from edge
            for e in graph.adjacencyList(vertex):   # For each adjacent edge, relax the edge
                self.__relax(e)

    def __relax(self,e):                            # Function to relax the edge
        u = e.fromVertex()                          
        v = e.toVertex()
        weight = e.edgeWeight()
        if self.__distTo[v] > self.__distTo[u] + weight:    # If distance to adjacent vertex is greater than distance to parent and weight of edge u->v
            oldDist = self.__distTo[v]                      # Retrieve the old distance first because we will update it
            self.__distTo[v] = self.__distTo[u] + weight    # Update the new distance
            self.__edgeTo[v] = e                            # Update edge to for the vertex visited with current edge
        
            # Condition to check if weight at any node goes below -1000 
            # which means program is in infinite loop and graph has negative weight cycle
            # Print the appropriate message and exit the program
            if self.__distTo[u] + weight < -1000:           
                print("Negative cycle detected in the graph. Cannot Perform Dijkstra Algorithm on graph with negative weight cycles...!!!\n")
                exit(-1)

            # Very important: If vertex visited is already in the heap, 
            # update the distance to vertex i.e. Decrease Key functionality of Heap
            # else, push the vertex visited with distance in heap
            if (v,oldDist) in self.__heap:
                index = self.__heap.index((v,oldDist))
                self.__heap[index] = (v,self.__distTo[v])
            else:                                               
                heapq.heappush(self.__heap,(v,self.__distTo[v]))

    def getMaximumDistance(self):                   # Function to return the maximum shortest path distance computed for a given source vertex
        max_distance = 0                            # Variable to track maximum distance 
        for i in range(len(self.__distTo)):
            if self.__distTo[i] > max_distance and self.__distTo[i] != float('inf'):    
                max_distance = self.__distTo[i]     # If maximum distance is less than distance to current vertex in graph and distance is not infinity, update the variable
        return max_distance

    def printresults(self):                                     # Function to print the Shortest Path to each vertex and its corresponding parent edge
        print("Vertex","\t","Dist To","\t","Edge To")
        for i in range(len(self.__distTo)):
            if i == self.__source:                              
                print(i,"\t",round(self.__distTo[i],4),"\t\t","-")
                continue
            
            if i in self.__edgeTo.keys():
                edge = self.__edgeTo[i]
                u = edge.fromVertex()
                v = edge.toVertex()
                print(i,"\t",round(self.__distTo[i],4),"\t\t",str(u) + "->" + str(v))
                continue

            print(i,"\t",round(self.__distTo[i],4),"\t\t","-")


    
# Function to create graph and run Dijkstra algorithm for tinyEWD dataset
def tinyEWD():
    file = open("tinyEWD.txt","r")          # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    directedGraph = DirectedGraph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = DirectedWeightedEdge(u,v,weight)     # Create weighted edge object

        directedGraph.addEdge(edge)         # Add edge to graph

    diameter = 0
    for i in range(total_vertices):
        dijkstra_spt = Dijkstra(directedGraph,i)                # Running Dijkstra code with source vertex as 0
        max_distance = dijkstra_spt.getMaximumDistance()
        if diameter < max_distance:
            diameter = max_distance
    print("The diameter of a directed graph i.e. the maximum-length shortest path connecting any two vertices for tinyEWD dataset is: ", diameter)

# Function to create graph and run Dijkstra algorithm for mediumEWD dataset
def mediumEWD():
    file = open("mediumEWD.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    directedGraph = DirectedGraph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = DirectedWeightedEdge(u,v,weight)     # Create weighted edge object

        directedGraph.addEdge(edge)         # Add edge to graph

    diameter = 0
    for i in range(total_vertices):
        dijkstra_spt = Dijkstra(directedGraph,i)                # Running Dijkstra code with source vertex as 0
        max_distance = dijkstra_spt.getMaximumDistance()
        if diameter < max_distance:
            diameter = max_distance
    print("The diameter of a directed graph i.e. the maximum-length shortest path connecting any two vertices for mediumEWD dataset is: ", diameter)

# Function to create graph and run Dijkstra algorithm for 1000EWD dataset
def EWD_1000():
    file = open("1000EWD.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    directedGraph = DirectedGraph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = DirectedWeightedEdge(u,v,weight)     # Create weighted edge object

        directedGraph.addEdge(edge)         # Add edge to graph

    diameter = 0
    for i in range(total_vertices):
        dijkstra_spt = Dijkstra(directedGraph,i)                # Running Dijkstra code with source vertex as 0
        max_distance = dijkstra_spt.getMaximumDistance()
        if diameter < max_distance:
            diameter = max_distance
    print("The diameter of a directed graph i.e. the maximum-length shortest path connecting any two vertices for 1000EWD dataset is: ", diameter)

# Function to create graph and run Dijkstra algorithm for 10000EWD dataset
def EWD_10000():
    file = open("10000EWD.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    directedGraph = DirectedGraph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = DirectedWeightedEdge(u,v,weight)     # Create weighted edge object

        directedGraph.addEdge(edge)         # Add edge to graph

    diameter = 0
    for i in range(total_vertices):
        dijkstra_spt = Dijkstra(directedGraph,i)                # Running Dijkstra code with source vertex as 0
        max_distance = dijkstra_spt.getMaximumDistance()
        if diameter < max_distance:
            diameter = max_distance
    print("The diameter of a directed graph i.e. the maximum-length shortest path connecting any two vertices for 10000EWD dataset is: ", diameter)

# Driver/Main Function
if __name__ == "__main__":
    tinyEWD()                        # execute program for tinyEWD dataset
    mediumEWD()                      # execute program for mediumEWD dataset
    # EWD_1000()                       # Uncomment to execute program for 1000EWD dataset
    # EWD_10000()                      # Uncomment to execute program for 10000EWD dataset
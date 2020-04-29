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

# Dijkstra Class   -   Implementation Idea is referred from lecture slides
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

    def printresults(self):                                     # Function to print the Shortest Path to each vertex and its corresponding parent edge
        print("Vertex","\t","Dist To","\t","Edge To")
        for i in range(len(self.__distTo)):
            if i == self.__source:                              
                print(i,"\t",round(self.__distTo[i],4),"\t\t","-")
                continue
            edge = self.__edgeTo[i]
            u = edge.fromVertex()
            v = edge.toVertex()
            print(i,"\t",round(self.__distTo[i],4),"\t\t",str(u) + "->" + str(v))
    
# Function to create graph and run Djikstra algorithm for data as per example in lecture slides
def slideExample():
    directedGraph = DirectedGraph(8)
    edge = DirectedWeightedEdge(0,1,5.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,4,9.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,7,8.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(1,2,12.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(1,3,15.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(1,7,4.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(2,3,3.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(2,6,11.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(3,6,9.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(4,5,4.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(4,6,20.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(4,7,5.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,2,1.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,6,13.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,5,6.0)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,2,7.0)
    directedGraph.addEdge(edge)

    dijkstra_spt = Dijkstra(directedGraph,0)        # Running Dijkstra code with source vertex as 0
    dijkstra_spt.printresults()

# Function to create graph and run Dijkstra algorithm for data given in question 4a
def homework4a():
    directedGraph = DirectedGraph(8)
    edge = DirectedWeightedEdge(4,5,0.35)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,4,0.35)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(4,7,0.37)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,7,0.28)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,5,0.28)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,1,0.32)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,4,0.38)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,2,0.26)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,3,0.39)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(1,3,0.29)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(2,7,0.34)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,2,-1.20)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(3,6,0.52)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,0,-1.40)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,4,-1.25)
    directedGraph.addEdge(edge)
    # directedGraph.printGraph()

    dijkstra_spt = Dijkstra(directedGraph,0)                # Running Dijkstra code with source vertex as 0
    dijkstra_spt.printresults()
    
# Function to create graph and run Dijkstra algorithm for data given in question 4b
def homework4b():
    directedGraph = DirectedGraph(8)
    edge = DirectedWeightedEdge(4,5,0.35)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,4,-0.66)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(4,7,0.37)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,7,0.28)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,5,0.28)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(5,1,0.32)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,4,0.38)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(0,2,0.26)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(7,3,0.39)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(1,3,0.29)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(2,7,0.34)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,2,0.40)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(3,6,0.52)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,0,0.58)
    directedGraph.addEdge(edge)
    edge = DirectedWeightedEdge(6,4,0.93)
    directedGraph.addEdge(edge)
    # directedGraph.printGraph()

    dijkstra_spt = Dijkstra(directedGraph,0)                # Running Dijkstra code with source vertex as 0
    dijkstra_spt.printresults()

# Driver/Main Function
if __name__ == "__main__":
    # print("Executing Dijkstra Algorithm for graph given in lecture slides: ")
    # slideExample()                    # Uncomment to calculate shortest path for the graph example present in lecture slides

    print("\nExecuting Dijkstra Algorithm for graph with data of Question 4a: ")
    homework4a()                        # execute program for data given in Question 4a and passing Source as Vertex 0
    print("\nExecuting Dijkstra Algorithm for graph with data of Question 4b: ")
    homework4b()                        # execute program for data given in Question 4b and passing Source as Vertex 0
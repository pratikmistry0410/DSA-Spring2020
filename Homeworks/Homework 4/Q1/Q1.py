from collections import defaultdict

# Undirected Weighted Edge Class
class WeightedEdge():
    def __init__(self,u,v,weight):                 # Default Constructor for initializing the Weighted Edge Class private variables
        self.__u = u
        self.__v = v
        self.__weight = weight
    
    def either(self):                              # Function to return first vertex
        return self.__u 
    
    def other(self,vertex):                        # Function to return other vertex
        if vertex == self.__u: 
            return self.__v
        return self.__u
    
    def edgeWeight(self):                          # Function to return edge weight
        return self.__weight

# Undirected Graph Class
class Graph():
    __V = 0                                         # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                           # Default Constructor to initialize graph with number of vertices
        self.__V = V
        self.__marked = [False] * V                 # Private Boolean array of size V for storing whether the vertex is VISITED or not
    
    def addEdge(self,edge):                         # Function to add edge in the graph
        u = edge.either()                           
        v = edge.other(u)
        if edge not in self.__graph[u][::]:         
            self.__graph[u].append(edge)            # Insert the edge at source vertex
            self.__graph[v].append(edge)            # Insert the edge at destination vertex because its undirected graph
            self.__E+=1                             # Increase edges count by 1
    
    def V(self):                                    # Function to return vertices count
        return self.__V     

    def E(self):                                    # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):                      # Function to return adjacency list i.e. edgelists at given vertex
        return self.__graph[V]

    # Public Function to check if graph is acyclic or not
    def isAcyclic(self):
        for vertex in range(self.__V):                  # For each vertex in the graph, do the DFS
            if self.__marked[vertex] == False:          # if vertex is visited, skip the vertex
                if(self.__isCyclic(vertex,-1)):         # For doing DFS for each vertex, pass parent as -1 since no parent exist
                    return False
        return True
            
    # Part of the code is referred from: https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
    def __isCyclic(self,vertex,parent):
        self.__marked[vertex] = True                    # Mark the vertex visited as True
        edgeList = self.__graph[vertex]
        for edge in range(len(edgeList)):               # For each vertex implement the DFS
            u = edgeList[edge].either()
            v = edgeList[edge].other(u)
            if self.__marked[v] == False:               # If vertex of adjacency list is not visited
                if self.__isCyclic(v,vertex):           # Recursively find whether graph is cycle by passing vertex of adjacency list and current parent
                    return True 
                elif parent != v:                       # If visited vertex has parent other than vertex from where it is travelled then it has cycle
                    return True
        return False

# Driver/Main Function
if __name__ == "__main__":
    file = open("mediumEWG.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    undirectedGraph = Graph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = float(edge_data[2])        # Read weight of the edge
        edge = WeightedEdge(u,v,weight)     # Create weighted edge object

        undirectedGraph.addEdge(edge)       # Add edge to graph

    if(undirectedGraph.isAcyclic()):        # Check if graph is acyclic or not
        print("The graph is acyclic..!!")
    else:
        print("The graph is not acyclic..!!")
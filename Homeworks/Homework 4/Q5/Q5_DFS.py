from collections import defaultdict

# Undirected Weighted Edge Class
class WeightedEdge():
    def __init__(self,u,v,weight):           # Default Constructor for initializing the Weighted Edge Class private variables      
        self.__u = u
        self.__v = v
        self.__weight = weight
    
    def either(self):                        # Function to return first vertex
        return self.__u
    
    def other(self,vertex):                  # Function to return other vertex
        if vertex == self.__u: 
            return self.__v
        return self.__u
    
    def edgeWeight(self):                    # Function to return edge weight
        return self.__weight

# Undirected Graph Class
class Graph():
    __V = 0                                 # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                   # Default Constructor to initialize graph with number of vertices
        self.__V = V
    
    def addEdge(self,edge):                 # Function to add edge in the graph
        u = edge.either()
        v = edge.other(u)
        if edge not in self.__graph[u]:
            self.__graph[u].append(edge)    # Insert the edge at source vertex
            self.__graph[v].append(edge)    # Insert the edge at destination vertex because its undirected graph
            self.__E+=1                     # Increase edges count by 1
    
    def V(self):                            # Function to return vertices count
        return self.__V 

    def E(self):                            # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):              # Function to return adjacency list i.e. edgelists at given vertex    
        return self.__graph[V]

# Depth first search class   -   Implementation Idea is referred from lecture slides
class DFS():
    __dfslist = []                          # List to store sequence of vertex visited in DFS
    def __init__(self,graph,s):             # Default Constructor
        self.__marked = [False] * graph.V() # Private Boolean array of size V for storing whether the vertex is VISITED or not
        self.__totalVisited = 0             # Counter to count visited nodes
        self.__DFS(graph,s)                 # Call private DFS function starting with source vertex passed in constructor
    
    def __DFS(self,graph,s):                # Private function to perform DFS
        stack = []                          # Using list as Stack to store the visiting vertex
        stack.append(s)                     # Insert source vertex in stack
        self.__marked[s] = True             # Mark source vertex as visited

        while(len(stack)):                  # While stack has vertex, perform DFS
            vertex = stack.pop()            # VERY IMPORTANT FOR DFS: Get top of stack last vertex
            self.__dfslist.append(vertex)   # add vertex to DFS list
            # print("Vertex ",vertex," visited!!!")
            self.__totalVisited+=1  
            edgeList = graph.adjacencyList(vertex)  # Get edges(adjacent vertices) at vertex
            for edge in range(len(edgeList)):       # For each vertex in edge
                u = edgeList[edge].either()
                v = edgeList[edge].other(u)
                if not self.__marked[v]:            # if not visited then add it to stack
                    stack.append(v)                 
                    self.__marked[v] = True         # mark it as visited
                    self.__dfslist.append(v)        # Store vertex to list

    def total_visited(self):                # Function to return total visited nodes in DFS
        return self.__totalVisited

    def dfs_list(self):                     # Function to return DFS list
        return self.__dfslist

# Driver/Main Function
if __name__ == "__main__":
    file = open("NYC.txt","r")              # Open the dataset file
    data = file.readlines()                 # Read all the lines
    total_vertices = int(data[0])           # Reading total vertices
    total_edges = int(data[1])              # Reading total edges
    
    undirectedGraph = Graph(total_vertices) # Creating object of Undirected Graph
    for i in range(2,total_edges+2):        # Reading all the edges iteratively and adding edge to the graph
        edge_data = data[i].split()         # Splitting the line based on spaces
        u = int(edge_data[0])               # Read source vertex
        v = int(edge_data[1])               # Read destination vertex
        weight = int(edge_data[2])          # Read weight of the edge
        edge = WeightedEdge(u,v,weight)     # Create weighted edge object    

        undirectedGraph.addEdge(edge)       # Add edge to graph
    
    dfs = DFS(undirectedGraph,1)            # Performing DFS on graph with source vertex as 1

    # print("The list of edges traversed using DFS are: ")      # Uncomment to print the Order of Edges visited
    # print(dfs.dfs_list())                                     # Uncomment to print the Order of Edges visited

    print("Total nodes traversed in depth first search: ",dfs.total_visited())
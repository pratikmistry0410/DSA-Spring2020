from collections import defaultdict

# Undirected Weighted Edge Class
class WeightedEdge():
    def __init__(self,u,v,weight):           # Default Constructor for initializing the Weighted Edge Class variables      
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

# Breadth First Search Class   -   Implementation Idea is referred from lecture slides
class BFS():
    __bfslist = []                                      # List to store sequence of vertex visited in BFS
    def __init__(self,graph,s):                         # Default Constructor
        self.__marked = [False] * graph.V()             # Private Boolean array of size V for storing whether the vertex is VISITED or not
        self.__totalVisited = 0                         # Counter to count visited nodes
        self.__BFS(graph,s)                             # Call private BFS function starting with source vertex passed in constructor
    
    def __BFS(self,graph,s):
        queue = []                                      # Using list as Queue to store visiting vertex
        queue.append(s)                                 # Insert source vertex in Queue
        self.__marked[s] = True                         # Mark source vertex as visited

        while(len(queue)):                              # While queue has vertex, perform BFS
            vertex = queue.pop(0)                       # VERY IMPORTANT FOR BFS: Get first vertex of queue
            self.__bfslist.append(vertex)               # add vertex to DFS list
            # print("Vertex ",vertex," visited!!!")
            self.__totalVisited+=1              
            edgeList = graph.adjacencyList(vertex)      # Get edges(adjacent vertices) at vertex
            for edge in range(len(edgeList)):           # For each vertex in edge
                u = edgeList[edge].either()
                v = edgeList[edge].other(u)
                if not self.__marked[v]:                 # if not visited then add it to queue
                    queue.append(v)
                    self.__marked[v] = True              # mark it as visited
                    self.__bfslist.append(v)             # Store vertex to list

    def total_visited(self):                             # Function to return total visited nodes in DFS
        return self.__totalVisited

    def bfs_list(self):                     # Function to return BFS list
        return self.__bfslist


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
    
    bfs = BFS(undirectedGraph,1)            # Performing BFS on graph with source vertex as 1

    # print("The list of edges traversed using DFS are: ")            # Uncomment to print the Order of Edges visited 
    # print(bfs.bfs_list())                                           # Uncomment to print the Order of Edges visited

    print("Total nodes traversed in breadth first search: ",bfs.total_visited())
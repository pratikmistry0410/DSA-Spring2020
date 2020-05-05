from collections import defaultdict

# Symbol Table Class to store the Movie and Cast Names as key-value pair
class SymbolTable():
    def __init__(self):
        self.symbol_table_list = []             # Creating symbol table list

    def insert(self,stringValue):               # Function to insert the movie/cast name in the symbol table list
        if self.symbol_table_list.count(stringValue) > 0:       # if movie/cast name exists is symbol table list then return else insert in list
            return
        else:
            self.symbol_table_list.append(stringValue)

    def getIndex(self,stringValue):             # Function to get the "KEY" i.e. index of movie/cast name in the symbol table list
        return self.symbol_table_list.index(stringValue)
    
    def print_symbolTable(self):                # Function to print Symbol Table as Key,Value pairs i.e. index,movie/cast name
        for i in range(len(self.symbol_table_list)):
            print(i," ", self.symbol_table_list[i])

    def size(self):                             # Function to return the length/size of symbol table list
        return len(self.symbol_table_list)
    

# Undirected Graph Class
class Graph():
    __V = 0                                 # Declaring private variables - no. of vertex and edges and graph as list of edgelists
    __E = 0
    __graph = defaultdict(list) 

    def __init__(self,V):                   # Default Constructor to initialize graph with number of vertices
        self.__V = V
    
    def addEdge(self,u,v):                 # Function to add edge in the graph
        self.__graph[u].append(v)          # Insert the edge at source vertex
        self.__graph[v].append(u)          # Insert the edge at destination vertex because its undirected graph
        self.__E+=1                        # Increase edges count by 1
    
    def V(self):                            # Function to return vertices count
        return self.__V 

    def E(self):                            # Function to return edges count
        return self.__E
    
    def adjacencyList(self,V):              # Function to return adjacency list i.e. edgelists at given vertex    
        return self.__graph[V]


# Connected Components Class
class ConnectedComponents():
    def __init__(self,graph):                   # Default Constructor
        self.__marked = [False] * graph.V()     # Private Boolean array of size V for storing whether the vertex is VISITED or not
        self.__id = [0] * graph.V()             # ID array to store ID of component containing v
        self.__count = 0                        # Variable to track the count of connected components and maintaining the ID as well
        self.__frequencyCounter = {}            # Dictionary to store the total connected components for a given component id
        self.__connectedComponents(graph)       # Calling Private function to compute the connected components for a given graph

    def __connectedComponents(self,graph):      # Private function to compute the connected components for a given graph
        for s in range(graph.V()):              # For each unvisited vertex, run the DFS to find all the connected components
            total_frequency = 0                 # Variable to store the total connected components for given component
            if not self.__marked[s]:            
                self.__count += 1
                total_frequency = self.__DFS(graph,s)            # Run DFS for unvisited vertex s
                self.__frequencyCounter[self.__count] = total_frequency     # Store the total connected components for a given component id in dictionary
                
                
    def __DFS(self,graph,s):                # Private function to perform DFS
        total = 0                           # Variable to count the connected components for given component id
        stack = []                          # Using list as Stack to store the visiting vertex
        stack.append(s)                     # Insert source vertex in stack
        self.__marked[s] = True             # Mark source vertex as visited
        self.__id[s] = self.__count         # Update the ID array
        total += 1                          # Increment total connected components

        while(len(stack)):                  # While stack has vertex, perform DFS
            vertex = stack.pop()            # VERY IMPORTANT FOR DFS: Get top of stack last vertex
            edgeList = graph.adjacencyList(vertex)  # Get edges(adjacent vertices) at vertex
            for v in edgeList:              # For each vertex in edge
                if not self.__marked[v]:    # if not visited then add it to stack
                    stack.append(v)                 
                    self.__marked[v] = True    # mark it as visited
                    self.__id[v] = self.__count     # Update the ID array 
                    total += 1                      # Increment total connected components

        return total                        # Return total components

    def count(self):                        # Function to return the total number of components
        return self.__count
    
    def size_largestComponent(self):        # Function to return Size of largest components
        return max(self.__frequencyCounter.values())
    
    def component_lessThan10(self):         # Function to Number of components less than 10 for data provided
        result = sum(1 for i in self.__frequencyCounter.values() if i < 10)
        return result



# Driver/Main Function
if __name__ == "__main__":
    # Creating Symbol Table
    symbol_table = SymbolTable()            # Creating symbol table object
    file = open("movies.txt","r")           # Open the dataset file
    data = file.readlines()                 # Read lines i.e. each movie and its cast
    for i in range(len(data)):           
        data[i] = data[i].rstrip('\n')      # Remove the "\n" i.e. newline character from the line
        line = data[i].split('/')           # Split the line based on "/" delimiter to get movie name and cast names
        for j in range(len(line)):          # For each movie + cast names, insert the name in symbol table
            symbol_table.insert(line[j])

    file.close()                            # Very important: Close the file because we will have to open and read file again
    

    # Creating Graph
    undirectedGraph = Graph(symbol_table.size())    # Creating object of Undirected Graph with vertices as symbol table size
    file = open("movies.txt","r")           # Open the dataset file
    data = file.readlines()                 # Read lines i.e. each movie and its cast   
    for i in range(len(data)):
        data[i] = data[i].rstrip('\n')      # Remove the "\n" i.e. newline character from the line
        line = data[i].split('/')           # Split the line based on "/" delimiter to get movie name and cast names
        movie_index = symbol_table.getIndex(line[0])    # Get the index i.e. key/index from symbol table for movie name
        for j in range(1,len(line)):        # For each cast name get the key/index from symbol table
            adjacent_index = symbol_table.getIndex(line[j])
            undirectedGraph.addEdge(movie_index,adjacent_index)       # Add edge to graph as movie_name,cast_name

    file.close()                        # Close the file

    # Creating and computing connected components in the given undirected graph
    connected_components = ConnectedComponents(undirectedGraph)

    # Printing required outputs by calling functions of connected components class
    print("Total number of components are: ",connected_components.count())                       
    print("Size of largest components is: ",connected_components.size_largestComponent())
    print("Number of components less than 10 for data provided are: ",connected_components.component_lessThan10())
import random
import math
import csv

class RedBlackBST():                                    # Red-Black Tree Class
    def __init__(self):                                 # Default constructor
        self.__root = None                              # Initializing Private Root Node to null
        self.__RED = True                               # Variable for red node indication
        self.__BLACK = False                            # Variable for black node indication
    
    class __Node():                                     # Private Node Class
        def __init__ (self,key,value,color):            # Default Constructor
            self.key = key                              # Initializing key
            self.value = value                          # Initlializing value
            self.color = color                          # Initializing color
            self.right = None                           # Pointer to left node as null
            self.left = None                            # Pointer to right node as null
            self.nodes = 1                              # Default size of node is 1

    def inorder(self):                                  # Public Function to traverse inorder
        self.__inorder(self.__root)                     # Calling Private Function to traverse inorder

    def __inorder(self,N):                              # Private Function to traverse inorder
        if N is not None: 
            self.__inorder(N.left)
            print(N.key,N.color,N.nodes)
            self.__inorder(N.right)

    def put(self,key,value):                            # Public Function to insert node in tree
        self.__root = self.__put(self.__root,key,value) # Calling private function to insert node in tree
        self.__root.color = self.__BLACK                # Very Important - root of tree will always be black node

    def __put(self,N,key,value):                        # Private Function to insert node in tree
            if N == None:                               # If tree/sub-tree is empty, create new node
                x = self.__Node(key,value,self.__RED)
                return x
            if key < N.key:                             # If key is less than parent key, traverse left to insert node
                N.left = self.__put(N.left,key,value)
            elif key > N.key:                           # If Key is greater than parent key, traverse right to insert node
                N.right = self.__put(N.right,key,value)
            else:
                N.value = value                         # If node is already present, update the value
               
            if self.__isRed(N.right) and not self.__isRed(N.left):      # Rotate left if right child node is red
                N = self.__rotateLeft(N)
            if self.__isRed(N.left) and self.__isRed(N.left.left):      # Rotate right if left child and left grandchild node is red     
                N = self.__rotateRight(N)
            if self.__isRed(N.left) and self.__isRed(N.right):          # Flip colors if both the child nodes are red
                self.__flipColors(N)
            N.nodes = 1 + self.__size(N.left) +self.__size(N.right)     # Update the size of the node
            return N

    def __isRed(self,node_x):                                       # Private Function to check if node is red
        if node_x == None:
            return False                                    
        return node_x.color == self.__RED
        
    def __rotateLeft(self,node_h):                                  # Private Function to rotate the sub-tree to left with root h
        if self.__isRed(node_h.right):                              # Check condition
            node_x = node_h.right
            node_h.right = node_x.left
            node_x.left = node_h
            node_x.color = node_h.color                             # Copy color of old root node to new root node
            node_h.color = self.__RED                               # Assign the new left node of tree as Red
            node_x.nodes = node_h.nodes                             # Assign the size of tree with new root node equal to old root node size
            node_h.nodes = 1 + self.__size(node_h.left) + self.__size(node_h.right) # Update the size of old root node
            return node_x                                           # Return new root node of subtree
 
    def __rotateRight(self,node_h):                                 # Private Function to rotate the sub-tree to right with root h
        if self.__isRed(node_h.left):                               # Check condition     
            node_x = node_h.left
            node_h.left = node_x.right
            node_x.right= node_h
            node_x.color = node_h.color                             # Copy color of root node to temp node
            node_h.color= self.__RED                                # Assign the new right node of tree as Red    
            node_x.nodes = node_h.nodes                             # Assign the size of tree with new root node equal to old root node size
            node_h.nodes = 1 + self.__size(node_h.left) + self.__size(node_h.right) # Update the size of old root node   
            return node_x                                           # Return new root node of subtree

    def __flipColors(self,node_h):                                  # Private Function to flip colors of sub-tree
        if not self.__isRed(node_h):                                # Check conditions for flipping
            if self.__isRed(node_h.left) :              
                if self.__isRed(node_h.right):
                    node_h.color = self.__RED                       # Change color of root of subtree to red
                    node_h.left.color = self.__BLACK                # Change color of left child to black
                    node_h.right.color = self.__BLACK               # Change color of black child to black

    def size(self):                                 # Public function to find size of red-black tree
        return self.__size(self.__root)             # Calling Private function to find size of whole tree
 
    def __size(self,N):                             # Private function to find the size of tree with root N
        if N == None:
            return 0
        return N.nodes 

    def internalPathLength(self):                   # Public function to find internal path length of tree
        return self.__internalPathLength(self.__root)/self.size() # Return (Internal path length/Size of tree)
    
    def __internalPathLength(self,N):               # Private Function to find internal path length
        if N == None:                               # If node is null, return 0
            return 0
        pathLength = 0                              # Initializing path length as 0

        # Calculate recursively: Internal Path Length = Size of tree at Node + internal path lengths of left and right tree
        pathLength = N.nodes + self.__internalPathLength(N.left) + self.__internalPathLength(N.right)
        return pathLength

def randomInsert(size):                                             # Function to create red-black tree by random insertion
    red_black_tree = RedBlackBST()                                  # Creating object of red-black tree    
    node_keys = []                                                  # List to store keys of tree
    for i in range(size):                                           # Creating list of keys for the tree as 0 to size-1
        node_keys.append(i)
    random.shuffle(node_keys)                                       # Shuffling the keys of tree

    for i in range(size):                                           # Creating random tree with random keys from the list
        red_black_tree.put(node_keys[i],i)
    return red_black_tree                                           # Return tree


def main_allNodes():
    NODES = 10000                                                   # Maximum size of tree i.e 10000
    TRIALS = 1000.0                                                 # Number of trials to find internal path length of tree of size 1 to 10000

    with open('q4_results_allNodes.csv', 'w', newline='') as file:           # Opening file stream to write results in CSV file
        writer = csv.writer(file)                                   
        writer.writerow(["Nodes","Average Path Length","Standard Deviation"]) # Writing the headers of CSV
        
        for i in range(1,NODES+1):                                  # For-loop for finding the average internal path length and standard deviation of tree size 1 to 10000
            pathLengths = 0                                         # Variable to store total internal path length for all trials
            pathDeviations = []                                     # List to store path lengths for all trials
            for j in range(int(TRIALS)):                            
                b_random = randomInsert(i)                          # Creating red-black tree for each trial of size 1 to 10000
                intPathLen = b_random.internalPathLength()          # Calculating internal path length of tree
                pathLengths += intPathLen                           # Adding length for all trials
                pathDeviations.append(intPathLen)                   # Storing length for each trial
            averagePathLength = pathLengths/TRIALS                  # Calculating Average Path Length after all trials

            stdDeviation = 0                                        # Variable for standard deviation
            deviations = 0                                          # Variable to calculate deviations in length for all trials with respect to average path length
            for j in range(int(TRIALS)):
                deviations += (pathDeviations[j] - averagePathLength)**2 # Adding deviations in length for all trials with respect to average path length
            stdDeviation = math.sqrt(deviations/TRIALS)             # Finding the standard deviation

            writer.writerow([i, averagePathLength, stdDeviation])   # Writing results in CSV file
    file.close()


def main_selectedNodes():
    nodes = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,10000]                                                   # Maximum size of tree i.e 10000
    TRIALS = 1000.0                                                 # Number of trials to find internal path length of tree of size 1 to 10000

    with open('q4_results_selectedNodes.csv', 'w', newline='') as file:           # Opening file stream to write results in CSV file
        writer = csv.writer(file)                                   
        writer.writerow(["Nodes","Average Path Length","Standard Deviation"]) # Writing the headers of CSV
        
        for i in range(len(nodes)):                                  # For-loop for finding the average internal path length and standard deviation of tree size 1 to 10000
            pathLengths = 0                                         # Variable to store total internal path length for all trials
            pathDeviations = []                                     # List to store path lengths for all trials
            for j in range(int(TRIALS)):                            
                b_random = randomInsert(nodes[i])                          # Creating red-black tree for each trial of size 1 to 10000
                intPathLen = b_random.internalPathLength()          # Calculating internal path length of tree
                pathLengths += intPathLen                           # Adding length for all trials
                pathDeviations.append(intPathLen)                   # Storing length for each trial
            averagePathLength = pathLengths/TRIALS                  # Calculating Average Path Length after all trials

            stdDeviation = 0                                        # Variable for standard deviation
            deviations = 0                                          # Variable to calculate deviations in length for all trials with respect to average path length
            for j in range(int(TRIALS)):
                deviations += (pathDeviations[j] - averagePathLength)**2 # Adding deviations in length for all trials with respect to average path length
            stdDeviation = math.sqrt(deviations/TRIALS)             # Finding the standard deviation

            writer.writerow([nodes[i], averagePathLength, stdDeviation])   # Writing results in CSV file
    file.close()

# Main Function  
if __name__ == "__main__":                                          
    # main_allNodes()
    main_selectedNodes()
import random
import sys

sys.setrecursionlimit(100000000)                        # Setting Maximum recursion depth limit to avoid recursion depth limit error

class BST():                                            # Binary Tree Class
    def __init__(self):                                 # Default constructor
        self.__root = None                              # Initializing Private Root Node to null

    class __Node():                                     # Private Node Class
        def __init__ (self,key,value):                  # Default Constructor
            self.key = key                              # Initializing key
            self.value = value                          # Initlializing value
            self.right = None                           # Pointer to left node as null
            self.left = None                            # Pointer to right node as null
            self.nodes = 1                              # Default size of node is 1

    def put(self,key,value):                            # Public Function to insert node in tree
        self.__root = self.__put(self.__root,key,value) # Calling private function to insert node in tree

    def __put(self,N,key,value):                        # Private Function to insert node in tree
            if N == None:                               # If tree/sub-tree is empty, create new node
                x = self.__Node(key,value)
                return x
            if key < N.key:                             # If key is less than parent key, traverse left to insert node
                N.left = self.__put(N.left,key,value)
            elif key > N.key:                           # If Key is greater than parent key, traverse right to insert node
                N.right = self.__put(N.right,key,value)
            else:
                N.value = value                         # If node is already present, update the value
            N.nodes = 1 + self.__size(N.left) +self.__size(N.right)     # Update the size of the node
            return N

    def size(self):                                 # Public function to find size of red-black tree
        return self.__size(self.__root)             # Calling Private function to find size of whole tree
 
    def __size(self,N):                             # Private function to find the size of tree with root N
        if N == None:
            return 0
        return N.nodes

    def avgPathLength(self):                        # Public function to find average path length
        return self.__PathLength(self.__root)/self.size()    # Calling private function to find average path length
    
    def __PathLength(self,N):                       # Private function to find average path length
        if(N != None):                              # If Node is null, then return
            pathlength = self.__PathLength(N.left) + self.__PathLength(N.right) + N.nodes
            return pathlength
        else:
            return 0

def orderedInsert(size):                                            # Function to create red-black tree by ordered insertion
    red_black_tree = BST()                                          # Creating object of red-black tree
    for i in range(size):                                           # Creating ordered tree of entered size with key & value from 0 to size-1
        red_black_tree.put(i,i)
    return red_black_tree                                           # Return tree

def randomInsert(size):                                             # Function to create red-black tree by random insertion
    red_black_tree = BST()                                          # Creating object of red-black tree    
    node_keys = []                                                  # List to store keys of tree
    for i in range(size):                                           # Creating list of keys for the tree as 0 to size-1
        node_keys.append(i)
    random.shuffle(node_keys)                                       # Shuffling the keys of tree

    for i in range(size):                                           # Creating random tree with random keys from the list
        red_black_tree.put(node_keys[i],i)
    return red_black_tree                                           # Return tree

# Main Function
if __name__ == "__main__":
    nodes = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]       # List of sizes of tree whose average path length needs to be calculated
    print("\nAverage Path Lengths for both trees are: ")
    print("Tree Size","\t\t\t\t","Tree with ordered insertion","\t\t\t\t","Tree with random insertion")
    for i in range(len(nodes)):                                     
        rbTree_ordered = orderedInsert(nodes[i])                    # Created tree of each size from list by ordered insertion
        rbTree_random = randomInsert(nodes[i])                      # Created tree of each size from list by random insertion
        print(nodes[i],"\t\t\t\t\t",round(rbTree_ordered.avgPathLength(),3),"\t\t\t\t\t\t\t",round(rbTree_random.avgPathLength(),3)) # Print average length of both the trees of each size
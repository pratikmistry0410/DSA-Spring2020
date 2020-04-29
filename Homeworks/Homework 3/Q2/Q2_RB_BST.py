import random

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

    def avgPathLength(self):                        # Public function to find average path length
        return self.__avgPathLength(self.__root)    # Calling private function to find average path length
    
    def __avgPathLength(self,N):                    # Private function to find average path length
        pathLength=[]                           # List to store path length of each leaf node in tree
        avgLength = 0                           # Variable for Average path length
        totalPathLength = 0                     # Variable for total path length i.e. Sum of all path length to lead nodes
        if N != None:                           # If tree is not empty, calculate all the path length of all leaf node 
            self.__calculatePath(N,1,pathLength)

        if len(pathLength) > 0:                 # check path lengths of leaf nodes are calculated
            for i in range(len(pathLength)):    
                totalPathLength += pathLength[i]   # Add all the path lengths calculated

        # Average Path Length = Total Path Length/(Size of tree excluding red nodes)
        avgLength = totalPathLength/(self.__size(self.__root)-self.countRed())   
        return avgLength
    
    def __calculatePath(self,N,length,pathLength):                  # Private Function to calculate path lengths of all leaf nodes
        if self.__isRed(N):                                         # If node is red, traverse further left and right to find path length
            if N.left != None:
                self.__calculatePath(N.left, length, pathLength)
            if N.right != None:
                self.__calculatePath(N.right, length, pathLength)
        else:
            pathLength.append(length)                               # If node is black, append the path length to that node to list and traverse left and right to find further path length
            if N.left != None:                                      
                self.__calculatePath(N.left, length + 1, pathLength)
            if N.right != None:
                self.__calculatePath(N.right, length + 1, pathLength)

    def countRed(self):                                             # Public function to find the number of red nodes in tree
        red_node_list = []                                          # Array/List as counter for calculating number of red nodes
        self.__countRed(self.__root,red_node_list)                  # Calling private function to find number of red nodes
        return len(red_node_list)                                   # Return the length of list as number of red nodes

    def __countRed(self,N,red_node_list):                           # Private function to count the red nodes
            if N == None:                                           # If node is null, return 
                return
            if N.color == self.__RED:                               # If node is red, add 1 to counter/list and traverse left and right further
                red_node_list.append(1)
            self.__countRed(N.left,red_node_list)
            self.__countRed(N.right,red_node_list)

def orderedInsert(size):                                            # Function to create red-black tree by ordered insertion
    red_black_tree = RedBlackBST()                                  # Creating object of red-black tree
    for i in range(size):                                           # Creating ordered tree of entered size with key & value from 0 to size-1
        red_black_tree.put(i,i)
    return red_black_tree                                           # Return tree

def randomInsert(size):                                             # Function to create red-black tree by random insertion
    red_black_tree = RedBlackBST()                                  # Creating object of red-black tree    
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
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

    def inorder(self):                                  # Public Function to traverse inorder
        self.__inorder(self.__root)                     # Calling Private Function to traverse inorder

    def __inorder(self,N):                              # Private Function to traverse inorder
        if N is not None: 
            self.__inorder(N.left)
            print(N.key,"\t",N.value,"\t",N.color)
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
            return N

    def __isRed(self,node_x):                           # Private Function to check if node is red
        if node_x == None:
            return False
        return node_x.color == self.__RED
        
    def __rotateLeft(self,node_h):                      # Private Function to rotate the sub-tree to left with root h
        if self.__isRed(node_h.right):                  # Check condition
            node_x = node_h.right                       
            node_h.right = node_x.left                  
            node_x.left = node_h                         
            node_x.color = node_h.color                 # Copy color of old root node to new root node
            node_h.color = self.__RED                   # Assign the new left node of tree as Red
            return node_x                               # Return new root node of subtree

    def __rotateRight(self,node_h):                     # Private Function to rotate the sub-tree to right with root h
        if self.__isRed(node_h.left):                   # Check condition    
            node_x = node_h.left                           
            node_h.left = node_x.right                  
            node_x.right= node_h                        
            node_x.color = node_h.color                 # Copy color of root node to temp node
            node_h.color= self.__RED                    # Assign the new right node of tree as Red
            return node_x                               # Return new root node of subtree
 
    def __flipColors(self,node_h):                      # Private Function to flip colors of sub-tree
        if not self.__isRed(node_h):                    # Check conditions for flipping
            if self.__isRed(node_h.left) :              
                if self.__isRed(node_h.right):
                    node_h.color = self.__RED           # Change color of root of subtree to red
                    node_h.left.color = self.__BLACK    # Change color of left child to black
                    node_h.right.color = self.__BLACK   # Change color of black child to black
                
def main_input2():
    red_black_tree = RedBlackBST()                      # Creating object of Red-Black tree
    file = open("select-data.txt","r")
    keys = file.readlines()
    for i in range(len(keys)):
        keys[i] = int(keys[i])

    for i in range(len(keys)):
        red_black_tree.put(keys[i],i)

    red_black_tree.inorder()                            # Traversing the tree inorder and printing the nodes


def main_input1():
    red_black_tree = RedBlackBST()                      # Creating object of Red-Black tree
    test_array = ['s','e','a','r','c','h','e','x','a','m','p','l','e']
    for i in range(len(test_array)):
        red_black_tree.put(test_array[i],i)
    red_black_tree.inorder()                            # Traversing the tree inorder and printing the nodes

# Main Function
if __name__ == "__main__":
    print("Key","\t","Value","\t","Node Color")
    main_input1()                                       # Use for input = "SEARCHEXAMPLE" i.e. example of lecture slides
    # main_input2()                                     # Use for input dataset "select-data.txt" i.e. dataset given in assignment
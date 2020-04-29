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

    def inorder(self):                                  # Public Function to traverse inorder
        self.__inorder(self.__root)                     # Calling Private Function to traverse inorder

    def __inorder(self,N):                              # Private Function to traverse inorder
        if N is not None: 
            self.__inorder(N.left)
            print(N.key,N.nodes)
            self.__inorder(N.right)

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

    def rank(self,key):                             # Public function to find rank of key
        return self.__rank(key,self.__root)         # Calling private function to find rank of key

    def __rank(self,key,N):                         # Private Function to find rank of key
            if N == None:
                return 0                            # If tree is empty return 0
            if key < N.key:                         # key is less than key at root, return rank() of key in the left subtree
                return self.__rank(key,N.left)      
            elif key > N.key:                       # if key is larger than key at root, return keys in left tree + 1 + rank of the key in the right tree
                return self.__rank(key, N.right)+1+self.__size(N.left)
            else:                                   # key equals key at root, return # of keys in the left subtree   
                return self.__size(N.left)
    
    def select(self,rank):                          # Public function to calculate find the key of given rank
        return self.__select(self.__root,rank)      # Calling private function to find key

    def __select(self,N,rank):                      # Private function to find key of given rank
            if rank < self.__size(N.left):          # if rank if less than size of left subtree, find key of given rank in left subtree
                return self.__select(N.left,rank)
            elif self.__size(N.left)==rank:         # If rank equals size of left subtree, return the key
                return N.key
            else:                                   # If rank is greater than size of left subtree, find key of rank equal to rank-left_tree_size-1 in right tree
                return self.__select(N.right,rank-self.__size(N.left)-1)

# Main Function
if __name__ == "__main__":
    file = open("select-data.txt","r")              # Open the dataset file
    keys = file.readlines()                         # Read all the lines
    for i in range(len(keys)):
        keys[i] = int(keys[i])                      # Create the list of keys present in dataset
 
    binaryTree = BST()                              # Create binary tree object
    for i in range(len(keys)):
        binaryTree.put(keys[i],i)                   # Insert keys in the tree

    print("Key of entered rank is: ",binaryTree.select(7))                     # Print the key of rank 7
    print("Rank of entered key is: ",binaryTree.rank(7))                       # Print the rank of key 7
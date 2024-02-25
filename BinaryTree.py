class Tree:
    def __init__(self, data, left=None, right=None):
        """
        Initialize a node in the binary search tree.
        
        Args:
            data: The data to be stored in the node.
            left (Tree): The left child node.
            right (Tree): The right child node.
        """
        self.data = data  # Store the data in the node
        self.left = left  # Store the left child node
        self.right = right  # Store the right child node
    
    def insert(self, data):
        """
        Insert a new node with given data into the binary search tree.
        
        Args:
            data: The data to be inserted.
        
        Returns:
            bool: True if the data is inserted successfully, False if it already exists.
        """
        if self.data == data:
            return False  # Data already exists in the tree
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)  # Recursively insert into the left subtree
            else:
                self.left = Tree(data)  # Create a new node and set it as the left child
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)  # Recursively insert into the right subtree
            else:
                self.right = Tree(data)  # Create a new node and set it as the right child
                return True

    def find(self, data):
        """
        Find the node with given data in the binary search tree.
        
        Args:
            data: The data to be found.
        
        Returns:
            bool: The data if found, False if not found.
        """
        if self.data == data:
            return data  # Data found
        elif self.data > data:
            if self.left is None:
                return False  # Data not found
            else:
                return self.left.find(data)  # Recursively search in the left subtree
        elif self.data < data:
            if self.right is None:
                return False  # Data not found
            else:
                return self.right.find(data)  # Recursively search in the right subtree
            
    
    
# Create a binary search tree instance
tree = Tree(7)

# Insert elements into the binary search tree
tree.insert(9)
for i in [15, 20, 5, 6, 16, 18]:
    tree.insert(i)

# Search for elements in the binary search tree
for i in range(10):
    print(tree.find(i), end=' ')  # Print the result of searching for each element

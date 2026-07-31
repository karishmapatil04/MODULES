class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, new_value):
        """Insert a new node with the given value into the BST."""
        if new_value < self.data:
            if self.left_child is None:
                self.left_child = BinaryTreeNode(new_value)
                print(f"Inserted {new_value} to the left of {self.data}")
            else:
                self.left_child.insert(new_value)
        elif new_value > self.data:
            if self.right_child is None:
                self.right_child = BinaryTreeNode(new_value)
                print(f"Inserted {new_value} to the right of {self.data}")
            else:
                self.right_child.insert(new_value)
        else:
            # Duplicate value found; not inserted
            print(f"Value {new_value} already exists in the tree.")

    def search(self, key):
        """Search for a node with the specified key in the BST."""
        if self.data == key:
            print(f"Found {key}")
            return True
        elif key < self.data:
            if self.left_child is not None:
                return self.left_child.search(key)
            else:
                print(f"Key not found in the tree.")
                return False
        else:  # key > self.data
            if self.right_child is not None:
                return self.right_child.search(key)
            else:
                print(f"Key not found in the tree.")
                return False

# Example usage
if __name__ == "__main__":
    root = BinaryTreeNode(13)
    root.insert(10)
    root.insert(25)
    root.insert(6)
    root.insert(14)
    root.insert(20)
    root.insert(60)

    # Searching for nodes
    root.search(14)  # Should find the node
    root.search(99)  # Should report that the node is not found
    root.search(6)
    root.search(88)
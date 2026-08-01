class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# A utility function to search a given key in BST
def search(root, key):

    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# Create a sample BST
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Driver code
key = int(input("Enter key to search: "))
result = search(root, key)

if result:
    print("Key found:", result.val)
else:
    print("Key not found")
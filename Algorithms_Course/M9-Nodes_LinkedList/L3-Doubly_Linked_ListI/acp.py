class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create Doubly Linked List
n = int(input("Enter the number of nodes: "))

head = None
tail = None

for i in range(n):
    data = int(input("Enter data: "))
    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node

# Display Doubly Linked List
print("Doubly Linked List:")
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
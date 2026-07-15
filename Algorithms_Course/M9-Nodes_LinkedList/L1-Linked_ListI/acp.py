class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
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
        tail = new_node

# Search element
key = int(input("Enter the element to search: "))

temp = head
position = 1
found = False

while temp is not None:
    if temp.data == key:
        found = True
        print("Element found at position", position)
        break
    temp = temp.next
    position += 1

if not found:
    print("Element not found in the linked list.")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Linked List
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

# Reverse the linked list
prev = None
current = head

while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

# Display reversed linked list
print("Reversed Linked List:")
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
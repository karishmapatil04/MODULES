class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Create doubly linked list
    def create(self, n):
        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp

    # Insert after a specific position
    def insert_after_position(self, pos, data):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        count = 1

        while temp is not None and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position.")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Main Program
dll = DoublyLinkedList()

n = int(input("Enter number of nodes: "))
dll.create(n)

print("\nOriginal List:")
dll.display()

position = int(input("Enter the position after which to insert: "))
value = int(input("Enter the value to insert: "))

dll.insert_after_position(position, value)

print("\nList after insertion:")
dll.display()
from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_to_beginning(self, data):
        node = Node(data)

        if self.head.next is None:
            print("This is the only value!")
            return
        else:
            temporary_node = self.head.next
            self.head = node
            self.head.next = temporary_node

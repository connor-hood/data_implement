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
        new_start = Node(data)

        if self.head.next is None:
            print("This is the only value")
        else:
            temporary_node = self.head
            self.head = new_start
            self.head.next = temporary_node

    def find_node(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
            print("we do not have this value")
        return curr

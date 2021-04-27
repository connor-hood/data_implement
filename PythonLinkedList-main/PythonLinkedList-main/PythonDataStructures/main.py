from linkedlist import LinkedList
from bst import BinaryTree

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.append_node(70)
    linked_list.append_node(75)
    linked_list.append_node(80)
    linked_list.append_node(85)
    linked_list.add_to_beginning(50)
    linked_list.add_to_beginning(30)

    linked_list.find_node(10)

    tree = BinaryTree()


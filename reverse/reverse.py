class Node:
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.prev_node = prev_node
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_next):
        self.prev_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        node = Node(value)
        
        # if empty then set both
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev_node = self.head
            self.head = node
            self.head.next = node
        
    

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if the node is None return
        if node is None:
            return
        # if the prev is none then make that node the tail
        if prev is None:
            node = self.tail
        
        # if it is next then make it
        if node.next_node is None:
            node = self.head
        else:
            node.prev_node = node.next_node

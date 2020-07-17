class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev_node = None
        self.value = value
        self.next_node = None

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
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node
        
    

    def contains(self, value):
        # set current
        current = self.head

        while current:
            # check current value
            # if equal then return true
            if current.value == value:
                return True
            # other wise change current to 
            else:
                current = current.next_node

        return False

    def reverse_list(self, node, prev):
        # if prev is none
        # then the node is the head and we set it to be tail
        if node is None:
            return
        if prev is None:
            self.tail = node
        if node.next_node is None:
            self.head = node
        self.reverse_list(node.next_node, node)
        node.prev_node = node.next_node
        node.next_node = prev
        
        
"""
Binary search trees are a value structure that enforce an ordering over
the value they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of value in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# don't allow duplicates
# order = []


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # the node we want to instantiate
        node = BSTNode(value)

        # check if there current node has a value
        if self.value:
            # check if value is greater than or equal to the current value then go right
            if value >= self.value:
                # if the right has no value then instantiate node into right
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(value)
            # check if value is less than the current value then go left
            elif value < self.value:
                # if the right has no value then instantiate node into right
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(value)
        # if current node doesn't have a value then the current node value becomes the value
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check the current nodes value
        # if it is equal to target then return True
        if self.value == target:
            return True
        # the target is greater than current than go right
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # if target is less than current go left
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        # otherwise return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check if a value exists to the right
        if self.right is None:
            # if it doesn't exist the max value is the current value
            return self.value
        # rerun the function on the right node
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # always run the function on current value
        fn(self.value)
        # if there is a right node then run the function
        if self.right:
            self.right.for_each(fn)
        # if there is a left node then run the function
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # base case:
        # check if left or right exist
        if node.left is None and node.right is None:
            print(node.value)
        elif node.left is None and node.right:
            print(node.value)
            self.in_order_print(node.right)
        elif node.left and node.right is None:
            self.in_order_print(node.left)
            print(node.value)
        elif node.left and node.right:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []
        # add the first node to the queue
        queue.append(node)
        # while queue is not empty
        while len(queue) > 0:
            
            # remove the first node
            node = queue.pop(0)
            # print what was removed
            print(node.value)
            # add all children
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

                

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node:
            print(node.value)
            self.dft_print(node.left)    
            self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        
        if node:
            print(node.value)
            self.dft_print(node.left)    
            self.dft_print(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.dft_print(node.left)                
            self.dft_print(node.right)
            print(node.value)
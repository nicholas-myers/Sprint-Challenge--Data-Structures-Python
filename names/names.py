import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
            return node
    
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

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# create a binary search tree on first list
# then iterate once through the second list 
# check if the binary tree contains the value
# if the tree contains the value append to duplicates
first_name = BSTNode(names_1[0])
for i in names_1:
    if i != names_1[0]:
        first_name.insert(i)
    
# first_name.in_order_print(first_name)
for i in names_2:
    if first_name.contains(i):
        duplicates.append(i)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

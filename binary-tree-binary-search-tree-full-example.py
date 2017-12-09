"""
https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c
"""
from queue import Queue


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.value


    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            self.left_child = new_node
            new_node.left_child = self.left_child

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            self.right_child = new_node
            new_node.right_child = self.right_child

### When we go deep to the leaf and backtrack, this is called DFS algorithm.
###	types of DFS: pre-order, in-order, and post-order

    def pre_order(self):
        print(self.value, end=" ")

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()


    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value, end=" ")

        if self.right_child:
            self.right_child.in_order()


    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value, end=" ")

    ## BFS Travesal
    def bfs(self):
        queue = Queue()
        queue.put(self)


        while not queue.empty():
            current_node = queue.get()
            print(current_node.value, end=" ")

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)


############################################################################
## 1st example
# tree = BinaryTree('a')
# print(tree.value) # a
# print(tree.left_child) # None
# print(tree.right_child) # None

#####
## 2nd example - Add nodes

# a_node = BinaryTree('a')
# a_node.insert_left('b')
# b_node = a_node.left_child

# print(b_node, a_node.left_child )

# a_node.insert_right('c')
# c_node = a_node.right_child
# print("Node {}: Left is {}, Right is {}.".format(a_node.value, a_node.left_child.value, a_node.right_child.value))

# b_node.insert_right('d')
# d_node = b_node.right_child
# print("Node {}: Right is {}".format(b_node.value,b_node.right_child.value))

# b_node.insert_right('g')
# g_node = b_node.right_child
# print("Node {}: Right is {}".format(g_node.value,g_node.right_child.value))


# c_node.insert_left('e')
# e_node = c_node.left_child
# c_node.insert_right('f')
# f_node = c_node.right_child

# print("Node {}: Left is {}, Right is {}.".format(c_node.value, c_node.left_child.value, c_node.right_child.value))

# print("Node values:",a_node.value,b_node.value,c_node.value, d_node.value,e_node.value,f_node.value)




### New Binary tree
node1 = BinaryTree('1')
node1.insert_left('2')
node1.insert_right('5')

node2 = node1.left_child
node5 = node1.right_child

node2.insert_left('3')
node2.insert_right('4')

node3 = node2.left_child
node3 = node2.right_child

node5.insert_left('6')
node5.insert_right('7')

node6 = node5.left_child
node7 = node5.right_child


print("\n3 types of DFS traversal\n")
print("In order:" , end=" ")
node1.in_order()
print()
print("Pre order", end=" ")
node1.pre_order()
print()
print("Post order", end=" ")
node1.post_order()
print()

print("\nBFS traversal:", end=" ")
node1.bfs()
print("\n")




#########################################
""" The powerful part of this algorithm is the recursion part, which is on
line 187 and line 191. Both lines of code call the insert_node method,
and use it for its left and right children, respectively.
Lines 180 and 184 are the ones that do the insertion for each child
"""

class BinarySearchTree:
    ''' Treat Nodes of Binary Search Tree'''

    def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    def __str__(self):
        return str(self.value)

    def insert_node(self, value):
            if value <= self.value and self.left_child:
                    self.left_child.insert_node(value)
            elif value <= self.value:
                    self.left_child = BinarySearchTree(value)
            elif value > self.value and self.right_child:
                    self.right_child.insert_node(value)
            else:
                    self.right_child = BinarySearchTree(value)

    def find_node(self, value):
#        print("Searching value:", value)
        ## Check LEFT subtree
        if( (value < self.value) and (self.left_child) ):
            print("{} < {} --> Search LEFT subtree of {}. Moving to node {}".format( value, self.value, self.value, self.left_child.value))
            return self.left_child.find_node(value)
        ## Check RIGHT subtree
        if value > self.value and self.right_child:
            print("{} > {} --> Search RIGHT subtree of {}. Moving to node {}".format(value, self.value, self.value, self.right_child.value))
            return self.right_child.find_node(value)
        ## if FOUND value ( return True)
        return value == self.value


    def remove_node(self, value, parent):

        print("PARENT is:", parent)

        ## Check LEFT subtree if exists
        if value < self.value and self.left_child:
            print("{} < {} --> Check LEFT subtree of {}. Moving to node {}".format( value, self.value, self.value, self.left_child.value))
            # RECURSIVE check LEFT Subtree
            return self.left_child.remove_node(value, self)
        # NOT FOUND in LEFT subtree
        elif value < self.value:
            return False

        ## Check RIGHT subtree if exists
        elif value > self.value and self.right_child:
            print("{} > {} --> Check RIGHT subtree of {}. Moving to node {}".format(value, self.value, self.value, self.right_child.value))
            # RECURSIVE check RIGHT Subtree
            return self.right_child.remove_node(value, self)
        # NOT FOUND in RIGHT subtree
        elif value > self.value:
            return False

        ## We found the node value and will check all the possible cases
        else:
            # Node has no children & is LEFT CHILD OF PARENT
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            # Node has no children & is RIGHT CHILD OF PARENT
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            # Node has ONLY 1 LEFT child & is LEFT CHILD OF PARENT
            elif self.left_child and (self.right_child is None) and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            # Node has ONLY 1 LEFT child & is RIGHT CHILD OF PARENT
            elif self.left_child and (self.right_child is None) and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            # Node has ONLY 1 RIGHT child & is LEFT CHILD OF PARENT
            elif self.right_child and (self.left_child is None) and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            # Node has ONLY 1 RIGHT child & is RIGHT CHILD OF PARENT
            elif self.right_child and (self.left_child is None) and self == parent.right_child:
                parent.right_child = self.right_child
               	self.clear_node()
            # Node has 2 Children. RIGHT & LEFT !
            # Copy value of right child to parent and remove right child of parent !!!
            # This gives the sense of moving the right child to parent position !!!
            else:
                self.value = self.right_child.find_maximum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None


    def find_maximum_value(self):
        if self.right_child:
            return self.righr_child.find_maximum_value()
        else:
            return self.value


#    def find_minimum_value(self):
#        if self.left_child:
#            return self.left_child.find_minimum_value()
#        else:
#            return self.value

    def pre_order(self):
        print(self.value, end=" ")

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()


    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value, end=" ")

        if self.right_child:
            self.right_child.in_order()


    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value, end=" ")

 ## BFS Travesal
    def bfs(self):
        queue = Queue()
        queue.put(self)


        while not queue.empty():
            current_node = queue.get()
            print(current_node.value, end=" ")

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)



### BST Example ####
bst = BinarySearchTree(50)
##Insert nodes
bst.insert_node(76)
bst.insert_node(21)
bst.insert_node(4)
bst.insert_node(32)
bst.insert_node(100)
bst.insert_node(64)
bst.insert_node(52)
bst.insert_node(68)
bst.insert_node(24)
bst.insert_node(36)



## Find nodes

#print(bst.find_node(76)) #True
#print(bst.find_node(21)) #True
#print(bst.find_node(4))  #True
#print(bst.find_node(32)) #True
#print(bst.find_node(100))#True
#print(bst.find_node(64)) #True
#print(bst.find_node(52)) #True
#print(bst.find_node(50)) #True
#print(bst.find_node(0)) #False


node = 36
## FIND value in BST
if bst.find_node(node):
    print("Value {} found in BSTree".format(node))
else:
    print("Value {} NOT found in BSTree".format(node))



print("\nBST DFS Traversal")
print("In order:" , end=" ")
bst.in_order()
print()
print("Pre order", end=" ")
bst.pre_order()
print()
print("Post order", end=" ")
bst.post_order()
print()

print("\nBST BFS traversal:", end=" ")
bst.bfs()
print("\n")


## DELETE value from BST
print("\nRemove node {} :".format(node))
if bst.remove_node(node, None) :
    print("Value {} deleted from BSTree".format(node))
else:
    print("Value {} NOT found in BSTree".format(node))


print("\nBST DFS Traversal")
print("In order:" , end=" ")
bst.in_order()
print()
print("Pre order", end=" ")
bst.pre_order()
print()
print("Post order", end=" ")
bst.post_order()
print()

print("\nBST BFS traversal:", end=" ")
bst.bfs()
print("\n")

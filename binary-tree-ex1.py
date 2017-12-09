"""
https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c
"""
from queue import Queue


class BinaryTree:

	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None


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

### in_order & pre_oreder are opposite in the linked article !!! ###

	def in_order(self):

	    print(self.value, end=" ")

	    if self.left_child:
	        self.left_child.in_order()
	    
	    if self.right_child:
	    	self.right_child.in_order()


	def pre_order(self):
		
		if self.left_child:
			self.left_child.pre_order()
	
		print(self.value, end=" ")

		if self.right_child:
			self.right_child.pre_order()	   
	

	def post_order(self):

		if self.left_child:
		    self.left_child.post_order()

		if self.right_child:
			self.right_child.post_order()

		print(self.value, end=" ")


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
from collections import deque


def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None # or raise appropriate exception

if __name__ == '__main__':
    # a sample graph
    graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F', 'D'],
             'F': ['C']}

    for key in (sorted(graph.keys())):
        print(key, graph[key])

    print("\nBFS from node A")
    for node in bfs(graph,'A'):
        print(node)

    print("\nDFS from node A")
    for node in dfs(graph,'A'):
        print(node)

    print("Shortest Path: A->D  : ", end="")
    print(shortest_path(graph,'A', 'D'))
    




## ---------------------------------------------------##

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

n1 = Node(1)
n2 = Node(2)
n3 = Node(3,n1,n2)
n4 = Node(4)
n5 = Node(5,n4,n3)

print('Inorder  :', end=" ")
def inorder(n):
    if n == None:
        return
    inorder(n.left)
    print(n.value, end=" ")
    inorder(n.right)
    
    
inorder(n5)

print('\nPreorder :', end=" ")
def preorder(n):
    if n == None:
        return
    print(n.value, end=" ")
    preorder(n.left)
    preorder(n.right)
   
    
preorder(n5)

print ('\nPostorder:', end=" ")
def postorder(n):
    if n == None:
        return
    postorder(n.left)
    postorder(n.right)
    print(n.value, end=" ")
   

postorder(n5)

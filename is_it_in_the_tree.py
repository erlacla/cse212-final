class BST:
    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data == node.data:
            return data

        elif data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
    

    def __contains__(self, data):

        return self._contains(data, self.root)

    def _contains(self, data, node):
        
        if data == node.data:
            return True
        if data < node.data:
            if node.left:
                return self._contains(data, node.left)
            else:
                return False

        if data > node.data:
            if node.right:
                return self._contains(data, node.right)
            else:
                return False


print()
print()
tree = BST()
tree.insert(25)
tree.insert(3)
tree.insert(7)
tree.insert(77)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(66)
tree.insert(4)


print(3 in tree) 
print(25 in tree) 
print(7 in tree) 
print(6 in tree) 
print(9 in tree) 
print(1 in tree)
print()
print()
# Trees

Trees are a non-linear data structure in python with 3 basic parts: the parent node and then the left and the right child nodes. A balanced binary tree is one that is evenly distributed between the left and the right. The uppermost node is called the root node. BST stands for "Binary Search Tree". Trees have no duplicate values.

## Why Python Trees are Useful

In Python we try to make our programs as efficient as possible. We learn about Big-O Notation which is all about how efficient or fast your program can be. Trees are one structure in python that help make data organization and searching more effective. Each time we search deeper down into the tree we are essentially splitting the data we have to search through in half! This results in O(log n) performance, which is very fast and efficient. A balanced BST is the most effective tree structure for searching through data because the tree structure is balanced. It's also helpful when searching through date for the computer to know that there are no duplicate values.

Here is the beginning of a basic BST:
```python
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
```
You set a left and a right node to None because there is no data yet, along with the root (or top) of the tree. Then you use the insert function to either set the root of the tree or set the next node in line.


## Common Errors

A common error when working with trees is to use the **return** keyword instead of the **yield** keyword. Lets say you want to traverse through a tree, you use a for loop, but if you use **return** you wont be able to move through each node of the tree because it will start the iteration from the root of the tree each time. If you use **yield** the iteration will continue from the place you left off at.

```python
def __iter__(self):
       
        yield from self._traverse_forward(self.root)
```

## Example: Create a BST

This program creates a new BST from a given sorted list. You can use this BST to quickly search for values.

```python
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

def create_bst_from_sorted_list(sorted_list):
    
    bst = BST()
    sorted_list, 0, len(sorted_list)-1, bst
    return bst


tree = create_bst_from_sorted_list([1, 9, 16, 22, 53, 68]) 
```


##  Problem to Solve: Is it in the tree?


Write a program that first creates a BST and then will tell you if an inputted number is within the tree. You may use the above code to create the BST. 

You can check your code with the solution here: [Solution](is_it_in_the_tree.py)

[Back to Welcome Page](0-welcome.md)
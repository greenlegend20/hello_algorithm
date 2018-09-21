
class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BSTNode(data)
                    return self.left
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BSTNode(data)
                    return self.right
                else:
                    self.right.insert(data)
        else:
            self.data = data
            return self

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        return sum([self.left is not None, self.right is not None])

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            children_count = self.children_count()
            if children_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def compare_trees(self, node):
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def min(self):
        if self.data is None:
            return
        node = self
        while node.left:
            node = node.left
        return node.data

    def max(self):
        if self.data is None:
            return
        node = self
        while node.right:
            node = node.right
        return node.data

    def tree_data(self):
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right


class BST(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        return '\n'.join(self._str()[0])

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return self.root
        else:
            return self.root.insert(data)

    def lookup(self, data):
        return self.root.lookup(data)

    def delete(self, data):
        self.root.delete(data)

    def print_tree(self):
        return self.root.print_tree()

    def compare_trees(self, tree):
        return self.root.compare_trees(tree.root)

    def get_min(self):
        return self.root.min()

    def get_max(self):
        return self.root.max()

    def tree_data(self):
        return self.root.tree_data()

    def get_parent(self, data):
        return self.lookup(data)[1]

    def get_height(self, node):
        if node is None:
            return -1
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1


class AVL(BST):
    def left_rotate(self, x):
        y = x.right
        parent = self.get_parent(x.data)
        if parent is None:
            self.root = y
        else:
            if parent.left is x:
                parent.left = y
            else:
                parent.right = y
        x.right = y.left
        y.left = x

    def right_rotate(self, x):
        y = x.left
        parent = self.get_parent(x.data)
        if parent is None:
            self.root = y
        else:
            if parent.left is x:
                parent.left = y
            else:
                parent.right = y
        x.left = y.right
        y.right = x

    def rebalance(self, node):
        while node is not None:
            left_height = self.get_height(node.left)
            right_height = self.get_height(node.right)
            if left_height >= 2 + right_height:
                if self.get_height(node.left.left) >= self.get_height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif right_height >= 2+ left_height:
                if self.get_height(node.right.right) >= self.get_height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = self.get_parent(node.data)

    def insert(self, data):
        node = super(AVL, self).insert(data)
        self.rebalance(node)

    def delete(self, data):
        parent = self.get_parent(data)
        super().delete(data)
        self.rebalance(parent)


import random
bst = BST()
avl = AVL()
for i in range(100):
    a = random.randint(1, 1000000)
    bst.insert(a)
    avl.insert(a)

print(bst.get_height(bst.root))
print(avl.get_height(avl.root))
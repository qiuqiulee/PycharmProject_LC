class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left = self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, node, root=None):
        if not root:
            if not self.root:
                self.root = node
                return True
            else:
                root = self.root

        if node.start >= root.end:
            if not root.right:
                root.right = node
                return True
            return self.insert(node, root.right)
        elif node.end <= root.start:
            if not root.left:
                root.left = node
                return True
            return self.insert(node, root.left)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.tree = Tree()

    def book(self, start, end):
        return self.tree.insert(Node(start, end))

obj = MyCalendar()

print(obj.book(10,20))
print(obj.book(11,20))
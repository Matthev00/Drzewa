import sys


class avl_Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class AVLTree:
    def insert_node(self, root, value):
        # BST
        if not root:
            return avl_Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        # Height update
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) # noqa 5501

        # Check tree balance
        balance = self.get_balance(root)

        # Correct balance
        if balance > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            elif value > root.left.value: # equal won't change anything
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            elif value < root.right.value: # equal won't change anything
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    def exists(self, value, root):
        if root is None:
            return False
        else:
            if value == root.value:
                return True
            elif value < root.value and root.left is not None:
                return self.exists(value, root.left)
            elif value > root.value and root.right is not None:
                return self.exists(value, root.right)
            return False


# tree = AVLTree()
# root = None
# nums = [33, 13, 52, 9, 21, 61, 8, 11, 70]
# for num in nums:
#     root = tree.insert_node(root, num)
# tree.printHelper(root, "", True)
# print(tree.get_height(root))
# print(tree.exists(12, root), tree.exists(21, root))

import random


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):

        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def exists(self, val):

        if val == self.val:
            return True

        if val < self.val:
            if self.left:
                return self.left.search(val)
            return False

        if self.right:
            return self.right.search(val)

        return False

    def delete(self, val):

        if self is None:
            return self

        if val < self.val:
            self.left = self.left.delete(val)
            return self

        if val > self.val:
            self.right = self.right.delete(val)
            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_bigger = self.right
        while min_bigger.left:
            min_bigger = min_bigger.left
        self.val = min_bigger.val
        self.right = self.right.delete(min_bigger.val)
        return self

    def draw(self, space=0):
        if self.val is None:
            return
        space += 5
        if self.right:
            self.right.draw(space)
        for i in range(5, space):
            print(end=" ")
        print("|" + str(self.val) + "|<")
        if self.left:
            self.left.draw(space)


def main():
    numbers = []
    for i in range(15):
        numbers.append(random.randint(1, 50))
    bst = BSTNode()
    numbers = [15, 12, 17, 3, 5, 9, 10, 4, 2, 7]
    for number in numbers:
        bst.insert(number)

    bst.draw()
    bst.delete(3)
    bst.draw()


if __name__ == "__main__":
    main()

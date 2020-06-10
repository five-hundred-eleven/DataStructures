from DataStructures import Queue

class BSTNode:

    def __init__(self, obj, left=None, right=None):
        assert isinstance(left, BSTNode) or left is None
        assert isinstance(right, BSTNode) or right is None
        self.__val = obj
        self.__left = left
        self.__right = right

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, obj):
        self.__val = obj

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        assert isinstance(left, BSTNode) or left is None
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        assert isinstance(right, BSTNode) or right is None
        self.__right = right

class BinarySearchTree:

    def __init__(self, *args):
        assert len(args) <= 1
        self.__root = None
        if args:
            container = args[0]
            for x in container:
                self.insert(x)

    def insert(self, x):
        if not self.__root:
            self.__root = BSTNode(x)
            return

        node = self.__root
        while True:

            if x < node.val:
                if node.left is None:
                    node.left = BSTNode(x)
                    return
                else:
                    node = node.left

            elif node.val < x:
                if node.right is None:
                    node.right = BSTNode(x)
                    return
                else:
                    node = node.right

            else:
                return

    def remove(self, x):
        if self.__root.val == x:
            if not self.__root.left and not self.__root.right:
                pass
            elif self.__root.left and not self.__root.right:
                self.__root = self.__root.left
            elif not self.__root.left and self.__root.right:
                self.__root = self.__root.right
            else:
                self.__root = None
                nodes = Queue([self.__root.left, self.__root.right])
                while True:
                    try:
                        node = nodes.pop()
                        if node.left:
                            nodes.push(node.left)
                        if node.right:
                            nodes.push(node.right)
                        self.insert(node.val)
                    except:
                        break

    def __contains__(self, x):

        node = self.__root

        while node is not None:
            if x < node.val:
                node = node.left
            elif node.val < x:
                node = node.right
            else:
                return True

        return False

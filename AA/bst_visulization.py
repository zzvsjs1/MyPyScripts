class TreeNode:

    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.value = None

    def __str__(self):
        return f'<Tree Node> left{self.left_child} ' \
               f'right{self.right_child} ' \
               f'parent{self.parent} ' \
               f'value{self.value}'

    def __bool__(self):
        return self.value is not None

    @staticmethod
    def buy_node(value) -> 'TreeNode':
        temp = TreeNode()
        temp.value = value
        return temp


class BinarySearchTree:

    def __init__(self, iter_obj=None):
        self.root = None
        if iter_obj is not None:
            for i in iter_obj:
                self.insert(i)

    def insert(self, value):
        pass

    def delete(self, obj):
        pass

    def has(self, obj):
        pass

    def inorder(self, call):
        pass

    def contain(self, value) -> bool:
        return bool(self.__find_node__(value))

    def __find_node__(self, value):
        next_p: TreeNode = self.root
        while next_p is not None:
            if next_p.value == value:
                return next_p

            next_p = next_p.right_child if next_p.value < value else next_p.left_child

        return None

    def __transplant__(self, to_delete: TreeNode, left_or_right_child: TreeNode):
        if left_or_right_child is not None:
            left_or_right_child.parent = to_delete.parent

        if to_delete.parent is not None:
            self.root = left_or_right_child
            return

        if to_delete == to_delete.parent:
            to_delete.parent.left_child = left_or_right_child
            return

        to_delete.parent.right_child = left_or_right_child



if __name__ == '__main__':
    tree = BinarySearchTree(range(10))

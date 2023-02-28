class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    def get_min(self):
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data

    def get_max(self):
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, current_node, data):
        if current_node is None:
            return None
        elif data < current_node.data:
            current_node.left = self._remove(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._remove(current_node.right, data)
        else:
            # 1: node to be deleted has no children
            if current_node.left is None and current_node.right is None:
                current_node = None
            # 2: node to be deleted has one child
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            # 3: node to be deleted has two children
            else:
                min_right_subtree = self._find_min(current_node.right)
                current_node.data = min_right_subtree.data
                current_node.right = self._remove(current_node.right, min_right_subtree.data)

        return current_node

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
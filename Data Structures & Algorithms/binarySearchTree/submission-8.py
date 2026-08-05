class TreeNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        """
        map the key to the value and insert it into the tree
        """
        new_node = TreeNode(key, val)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while current:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return

                current = current.left
            elif current.key < key:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        """
        return the value mapped with the key

        if the key DNE, return -1
        """
        if self.root is None:
            return -1

        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif current.key < key:
                current = current.right
            else:
                return current.val

        return -1

    def getMin(self) -> int:
        """
        return the value mapped to the smallest key in the tree
        """
        if self.root is None:
            return -1

        current = self.root
        while current and current.left:
            current = current.left

        return current.val

    def getMax(self) -> int:
        """
        return the value mapped to the largest key in the tree
        """
        if self.root is None:
            return -1

        current = self.root
        while current and current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        """
        remove the key value pair with the given key from the tree
        """
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, node, key):
        """
        Helper function to recursively remove a node with a specific key from a
        tree
        """
        if node is None:
            return None

        if key < node.key:
            node.left = self.removeHelper(node.left, key)
            return node
        elif node.key < key:
            node.right = self.removeHelper(node.right, key)
            return node
        else:
            # case 1: 0 or 1 nodes
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # case 2: 2 nodes
                min_node = self.getMinNode(node.right)

                node.val = min_node.val
                node.key = min_node.key

                node.right = self.removeHelper(node.right, min_node.key)

                return node

    def getMinNode(self, node):
        """
        Helper function to get the node with the minimum key in the tree
        """
        current = node

        while current and current.left:
            current = current.left

        return current

    def getInorderKeys(self) -> List[int]:
        """
        return an array of the keys in the tree in ascending order
        """
        result = []
        self.inorder(result, self.root)
        return result

    def inorder(self, result, node) -> None:
        """
        Helper function to recursively perform an inorder traversal
        """
        if not node:
            return

        self.inorder(result, node.left)
        result.append(node.key)
        self.inorder(result, node.right)


# time complexity: O(n)
# space complexity: O(n)

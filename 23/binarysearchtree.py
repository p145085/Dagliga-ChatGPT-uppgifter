#23. Bygg ett binärt sökträd och lägg till funktioner för insättning och borttagning.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Infogar en ny nyckel i trädet."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        """Tar bort en nyckel från trädet."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        # Hitta noden att ta bort
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Noden har högst ett barn
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Noden har två barn: Hitta minsta nyckeln i högra subträdet
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_recursive(node.right, min_larger_node.key)

        return node

    def _min_value_node(self, node):
        """Hjälpfunktion för att hitta noden med det minsta värdet."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Returnerar en inorder-traversering av trädet."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

#############

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Infoga noder
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder-traversering före borttagning:", bst.inorder())
    # Output: [20, 30, 40, 50, 60, 70, 80]

    # Ta bort en nod
    bst.delete(50)
    print("Inorder-traversering efter borttagning:", bst.inorder())
    # Output: [20, 30, 40, 60, 70, 80]

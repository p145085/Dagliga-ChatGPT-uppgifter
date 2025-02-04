#21. **Implementera ett AVL-träd med insättnings- och borttagningsfunktioner.**
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Höjden på en ny nod är alltid 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Uppdatera höjder
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x  # Ny rot

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Uppdatera höjder
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y  # Ny rot

    def insert(self, root, key):
        if not root:
            return Node(key)

        # Vanlig BST-insertion
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicerade värden stöds ej

        # Uppdatera höjd
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Hämta balansfaktorn
        balance = self.get_balance(root)

        # Fyra fall av obalans
        # Vänster Vänster
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Höger Höger
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Vänster Höger
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Höger Vänster
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        # Vanlig BST-borttagning
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Nod med en eller ingen barn
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Nod med två barn: hämta minsta i höger subträd
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Om trädet bara hade en nod
        if not root:
            return root

        # Uppdatera höjd
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Hämta balansfaktor
        balance = self.get_balance(root)

        # Fyra fall av obalans
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        if root:
            print(f"{root.key} ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)


# Exempel på användning
avl = AVLTree()
root = None

# Insättning
values = [10, 20, 30, 40, 50, 25]
for v in values:
    root = avl.insert(root, v)

print("Pre-order traversal efter insättning:")
avl.pre_order(root)
print()

# Borttagning
root = avl.delete(root, 30)

print("Pre-order traversal efter borttagning av 30:")
avl.pre_order(root)
print()

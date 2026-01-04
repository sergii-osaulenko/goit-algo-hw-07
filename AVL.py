# Реалізація AVL-дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

## Завдання 1: Функція для знаходження найбільшого значення
def find_max(root):
    if not root:
        return None
    current = root
    while current.right:
        current = current.right
    return current.value

## Завдання 2: Функція для знаходження найменшого значення
def find_min(root):
    if not root:
        return None
    current = root
    while current.left:
        current = current.left
    return current.value

## Завдання 3: Функція для обчислення суми всіх значень
def tree_sum(root):
    if not root:
        return 0
    return tree_sum(root.left) + root.value + tree_sum(root.right)

# Тестування
if __name__ == "__main__":
    tree = AVLTree()
    values = [10, 20, 30, 5, 15, 25, 35]
    for val in values:
        tree.insert_value(val)

    print("Найбільше значення:", find_max(tree.root))  # 35
    print("Найменше значення:", find_min(tree.root))  # 5
    print("Сума всіх значень:", tree_sum(tree.root))  # 140
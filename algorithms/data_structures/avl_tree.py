"""
AVL Tree / Pohon AVL

English Description:
An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes. This ensures O(log n) time complexity for search, insert, and delete operations.

Indonesian Description:
Pohon AVL adalah Binary Search Tree (BST) yang menyeimbangkan diri di mana perbedaan tinggi antara sub-pohon kiri dan kanan tidak boleh lebih dari satu untuk semua simpul. Ini memastikan kompleksitas waktu O(log n) untuk operasi pencarian, penyisipan, dan penghapusan.

Implementation Details:
- Balance Factor / Faktor Keseimbangan:
  [EN] Maintained for each node as `height(left) - height(right)`. Must be -1, 0, or 1.
  [ID] Dipertahankan untuk setiap simpul sebagai `tinggi(kiri) - tinggi(kanan)`. Harus -1, 0, atau 1.

- Rotations / Rotasi:
  [EN] Four types of rotations (Left, Right, Left-Right, Right-Left) are used to rebalance the tree after insertion.
  [ID] Empat jenis rotasi (Kiri, Kanan, Kiri-Kanan, Kanan-Kiri) digunakan untuk menyeimbangkan kembali pohon setelah penyisipan.

- Time Complexity / Kompleksitas Waktu:
  [EN] O(log n) for insert, delete, and search.
  [ID] O(log n) untuk penyisipan, penghapusan, dan pencarian.

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the nodes.
  [ID] O(n) untuk menyimpan simpul.

Usage Documentation:
  [EN] Create an `AVLTree` instance and use `insert(root, key)` to add nodes. Note: The insert method returns the new root of the subtree.
  [ID] Buat instance `AVLTree` dan gunakan `insert(root, key)` untuk menambahkan simpul. Catatan: Metode insert mengembalikan root baru dari sub-pohon.

  >>> tree = AVLTree()
  >>> root = None
  >>> root = tree.insert(root, 10)
  >>> root = tree.insert(root, 20)
  >>> root = tree.insert(root, 30)
  >>> tree.get_balance(root)
  0
  >>> root.key
  20
"""

from typing import Optional, Any, List

class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def get_height(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root: Optional[AVLNode], key: int) -> AVLNode:
        # 1. Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor
        balance = self.get_balance(root)

        # 4. If unbalanced, then try out 4 cases
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

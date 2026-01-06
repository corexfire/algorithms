"""
Binary Search Tree (BST) / Pohon Pencarian Biner

English Description:
A Binary Search Tree (BST) is a tree data structure where each node has at most two children, referred to as the left child and the right child. For any given node, the left child's value is less than the parent's value, and the right child's value is greater than the parent's value.

Indonesian Description:
Binary Search Tree (BST) adalah struktur data pohon di mana setiap simpul memiliki paling banyak dua anak, yang disebut sebagai anak kiri dan anak kanan. Untuk setiap simpul yang diberikan, nilai anak kiri lebih kecil dari nilai induknya, dan nilai anak kanan lebih besar dari nilai induknya.

Implementation Details:
- Properties / Properti:
  [EN] Left subtree of a node contains only nodes with keys lesser than the node's key. Right subtree contains only nodes with keys greater than the node's key.
  [ID] Sub-pohon kiri dari sebuah simpul hanya berisi simpul dengan kunci yang lebih kecil dari kunci simpul tersebut. Sub-pohon kanan hanya berisi simpul dengan kunci yang lebih besar dari kunci simpul tersebut.

- Operations / Operasi:
  [EN] Insert, Search, and Inorder Traversal (which gives sorted output).
  [ID] Penyisipan, Pencarian, dan Penelusuran Inorder (yang memberikan output terurut).

- Time Complexity / Kompleksitas Waktu:
  [EN] Average: O(log n), Worst case (unbalanced): O(n).
  [ID] Rata-rata: O(log n), Kasus terburuk (tidak seimbang): O(n).

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the nodes.
  [ID] O(n) untuk menyimpan simpul.

Usage Documentation:
  [EN] Use `BST()` to create a tree, `insert(key)` to add elements, and `search(key)` to find them.
  [ID] Gunakan `BST()` untuk membuat pohon, `insert(key)` untuk menambahkan elemen, dan `search(key)` untuk menemukannya.

  >>> bst = BST()
  >>> bst.insert(50)
  >>> bst.insert(30)
  >>> bst.insert(70)
  >>> bst.search(30)
  True
  >>> bst.search(90)
  False
  >>> bst.inorder_traversal()
  [30, 50, 70]
"""

from typing import Optional, List, Any

class Node:
    """Representasi Node dalam BST."""
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    """Implementasi Binary Search Tree."""
    
    def __init__(self):
        self.root: Optional[Node] = None
        
    def insert(self, key: int) -> None:
        """Menyisipkan key baru ke dalam BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
            
    def _insert_recursive(self, node: Node, key: int) -> None:
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
        # Jika key == node.key, abaikan (tidak ada duplikat dalam implementasi ini)
        
    def search(self, key: int) -> bool:
        """Mencari apakah key ada dalam BST."""
        return self._search_recursive(self.root, key)
        
    def _search_recursive(self, node: Optional[Node], key: int) -> bool:
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
            
    def inorder_traversal(self) -> List[int]:
        """Mengembalikan list elemen urut (Inorder: Left -> Root -> Right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
        
    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    # Test cases
    print("Running BST Tests...")
    
    bst = BST()
    
    # Insert data: 50, 30, 20, 40, 70, 60, 80
    data = [50, 30, 20, 40, 70, 60, 80]
    for x in data:
        bst.insert(x)
        
    # Search
    print(f"Searching for 40: {bst.search(40)}")
    assert bst.search(40) == True, "Search found failed"
    
    print(f"Searching for 90: {bst.search(90)}")
    assert bst.search(90) == False, "Search not found failed"
    
    # Inorder Traversal (Harus terurut ascending)
    inorder = bst.inorder_traversal()
    print(f"Inorder Traversal: {inorder}")
    assert inorder == sorted(data), "Inorder traversal failed"
    
    print("All BST tests passed!")

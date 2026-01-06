"""
Singly Linked List / Linked List Tunggal

English Description:
A Singly Linked List is a linear data structure where elements are stored in nodes. Each node contains a data field and a reference (link) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations.

Indonesian Description:
Singly Linked List adalah struktur data linier di mana elemen disimpan dalam simpul. Setiap simpul berisi bidang data dan referensi (tautan) ke simpul berikutnya dalam urutan. Tidak seperti array, linked list tidak menyimpan elemen di lokasi memori yang bersebelahan.

Implementation Details:
- Node Structure / Struktur Simpul:
  [EN] Each node holds `data` and a `next` pointer.
  [ID] Setiap simpul menyimpan `data` dan penunjuk `next`.

- Operations / Operasi:
  [EN] Insertion (at beginning/end), Deletion (by value), Searching, and Traversal.
  [ID] Penyisipan (di awal/akhir), Penghapusan (berdasarkan nilai), Pencarian, dan Penelusuran.

- Time Complexity / Kompleksitas Waktu:
  [EN] Insert at beginning: O(1). Insert at end: O(n) (or O(1) with tail pointer). Search/Delete: O(n).
  [ID] Sisipkan di awal: O(1). Sisipkan di akhir: O(n) (atau O(1) dengan penunjuk ekor). Cari/Hapus: O(n).

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the nodes.
  [ID] O(n) untuk menyimpan simpul.

Usage Documentation:
  [EN] Use `LinkedList()` to create a list. Use `insert_at_beginning(data)` or `insert_at_end(data)` to add items.
  [ID] Gunakan `LinkedList()` untuk membuat daftar. Gunakan `insert_at_beginning(data)` atau `insert_at_end(data)` untuk menambahkan item.

  >>> ll = LinkedList()
  >>> ll.insert_at_end(10)
  >>> ll.insert_at_end(20)
  >>> ll.insert_at_beginning(5)
  >>> print(ll)
  5 -> 10 -> 20 -> None
"""

from typing import Optional, Any, List

class Node:
    """A node in the singly linked list."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None

class LinkedList:
    """Singly Linked List implementation."""
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0
        
    def insert_at_beginning(self, data: Any) -> None:
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def insert_at_end(self, data: Any) -> None:
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
        
    def delete(self, data: Any) -> bool:
        """
        Deletes the first occurrence of data in the list.
        Returns True if deleted, False if not found.
        """
        if not self.head:
            return False
            
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
            
        return False
        
    def search(self, data: Any) -> bool:
        """Searches for data in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
        
    def to_list(self) -> List[Any]:
        """Converts linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
        
    def __len__(self) -> int:
        return self.size
        
    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_list())) + " -> None"

if __name__ == "__main__":
    # Test cases
    ll = LinkedList()
    
    # Insertions
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(0)
    
    print(f"List: {ll}")
    assert ll.to_list() == [0, 1, 2, 3]
    
    # Search
    assert ll.search(2) == True
    assert ll.search(10) == False
    
    # Deletion
    assert ll.delete(2) == True
    print(f"After deleting 2: {ll}")
    assert ll.to_list() == [0, 1, 3]
    
    assert ll.delete(0) == True
    print(f"After deleting 0: {ll}")
    assert ll.to_list() == [1, 3]
    
    print("All Linked List tests passed!")

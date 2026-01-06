"""
Description:
    [EN] A stack is a linear data structure that follows the Last In First Out (LIFO) principle. Elements are added and removed from the same end, called the "top". It is fundamental for function call management, expression evaluation, and backtracking algorithms.
    [ID] Tumpukan (stack) adalah struktur data linear yang mengikuti prinsip Last In First Out (LIFO). Elemen ditambahkan dan dihapus dari ujung yang sama, yang disebut "atas" (top). Ini mendasar untuk manajemen pemanggilan fungsi, evaluasi ekspresi, dan algoritma backtracking.

Implementation Details:
    [EN]
    - The `Stack` class is implemented using a Python list, where the end of the list represents the top of the stack.
    - Operations `push` and `pop` are O(1) amortized.
    - Includes a utility function `is_balanced_parentheses` demonstrating a practical application of the stack.
    [ID]
    - Kelas `Stack` diimplementasikan menggunakan list Python, di mana akhir list mewakili bagian atas tumpukan.
    - Operasi `push` dan `pop` bersifat O(1) teramortisasi.
    - Termasuk fungsi utilitas `is_balanced_parentheses` yang mendemonstrasikan aplikasi praktis dari stack.

Usage Documentation:
    [EN]
    - Instantiate the `Stack` class.
    - Use `push(item)` to add an element to the top.
    - Use `pop()` to remove and return the top element.
    - Use `peek()` to view the top element without removing it.
    - Use `is_empty()` to check if the stack is empty.
    [ID]
    - Buat instansi kelas `Stack`.
    - Gunakan `push(item)` untuk menambahkan elemen ke atas.
    - Gunakan `pop()` untuk menghapus dan mengembalikan elemen teratas.
    - Gunakan `peek()` untuk melihat elemen teratas tanpa menghapusnya.
    - Gunakan `is_empty()` untuk memeriksa apakah tumpukan kosong.

Examples:
    >>> s = Stack()
    >>> s.push(10)
    >>> s.push(20)
    >>> s.peek()
    20
    >>> s.pop()
    20
    >>> s.is_empty()
    False
"""

from typing import List, Any, Optional

class Stack:
    """Implementasi Stack menggunakan List Python."""
    
    def __init__(self):
        self._items: List[Any] = []
        
    def push(self, item: Any) -> None:
        """Menambahkan item ke atas stack."""
        self._items.append(item)
        
    def pop(self) -> Optional[Any]:
        """
        Menghapus dan mengembalikan item teratas stack.
        Returns None jika stack kosong.
        """
        if self.is_empty():
            return None
        return self._items.pop()
        
    def peek(self) -> Optional[Any]:
        """
        Melihat item teratas tanpa menghapusnya.
        Returns None jika stack kosong.
        """
        if self.is_empty():
            return None
        return self._items[-1]
        
    def is_empty(self) -> bool:
        """Memeriksa apakah stack kosong."""
        return len(self._items) == 0
        
    def size(self) -> int:
        """Mengembalikan jumlah item dalam stack."""
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)

# Contoh penggunaan Stack: Balanced Parentheses Checker
def is_balanced_parentheses(expression: str) -> bool:
    """
    Memeriksa apakah tanda kurung dalam ekspresi seimbang menggunakan Stack.
    Mendukung (), [], {}.
    """
    stack = Stack()
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in mapping.values(): # Opening bracket
            stack.push(char)
        elif char in mapping.keys(): # Closing bracket
            if stack.is_empty() or mapping[char] != stack.pop():
                return False
                
    return stack.is_empty()

if __name__ == "__main__":
    # Test cases Stack
    print("Running Stack Tests...")
    
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    print(f"Stack: {s}")
    assert s.peek() == 3, "Peek failed"
    assert s.pop() == 3, "Pop failed"
    assert s.size() == 2, "Size failed"
    
    # Test cases Balanced Parentheses
    print("Running Balanced Parentheses Tests...")
    
    expr1 = "{[()]}"
    assert is_balanced_parentheses(expr1) == True, "Failed expr1"
    
    expr2 = "{[(])}"
    assert is_balanced_parentheses(expr2) == False, "Failed expr2"
    
    expr3 = "((()"
    assert is_balanced_parentheses(expr3) == False, "Failed expr3"
    
    print("All Stack tests passed!")

"""
Trie (Prefix Tree)
------------------

1. English Description
----------------------
A Trie (pronounced "try") or Prefix Tree is a tree-based data structure used for efficiently storing and retrieving keys in a dataset of strings.
It is commonly used for autocomplete, spell checking, and IP routing.
Unlike a binary search tree, nodes in the tree do not store the key associated with that node; instead, its position in the tree defines the key.

Time Complexity: O(L) for insert, search, and starts_with, where L is the length of the string.
Space Complexity: O(N * L * Sigma) where N is number of keys, L is average length, Sigma is alphabet size.

2. Indonesian Description
-------------------------
Trie (diucapkan "try") atau Prefix Tree adalah struktur data berbasis pohon yang digunakan untuk menyimpan dan mengambil kunci secara efisien dalam kumpulan data string.
Ini biasanya digunakan untuk pelengkapan otomatis (autocomplete), pemeriksaan ejaan, dan perutean IP.
Tidak seperti pohon pencarian biner, simpul di pohon tidak menyimpan kunci yang terkait dengan simpul tersebut; sebaliknya, posisinya di pohon mendefinisikan kuncinya.

Kompleksitas Waktu: O(L) untuk insert, search, dan starts_with, di mana L adalah panjang string.
Kompleksitas Ruang: O(N * L * Sigma) di mana N adalah jumlah kunci, L adalah panjang rata-rata, Sigma adalah ukuran alfabet.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Node Structure / Struktur Node**:
  - [EN] Each node contains a dictionary of children and a boolean flag `is_end_of_word`.
  - [ID] Setiap node berisi kamus anak (children) dan flag boolean `is_end_of_word`.
- **Operations / Operasi**:
  - [EN] **Insert**: Traverses/creates nodes for each character. Marks end.
  - [ID] **Insert**: Melintasi/membuat node untuk setiap karakter. Menandai akhir.
  - [EN] **Search**: Traverses nodes. Returns true if path exists and is marked as end.
  - [ID] **Search**: Melintasi node. Mengembalikan true jika jalur ada dan ditandai sebagai akhir.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Class Usage / Penggunaan Kelas**:
  - [EN] Instantiate `Trie()`, then call `.insert(word)`, `.search(word)`, or `.starts_with(prefix)`.
  - [ID] Instansiasi `Trie()`, lalu panggil `.insert(word)`, `.search(word)`, atau `.starts_with(prefix)`.
"""

from typing import Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """Menyisipkan kata ke dalam Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        """Mencari apakah kata ada dalam Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
        
    def starts_with(self, prefix: str) -> bool:
        """Mengecek apakah ada kata dalam Trie yang dimulai dengan prefix tertentu."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Test Cases
    print("Running Trie Tests...")
    
    trie = Trie()
    
    # Insert
    trie.insert("apple")
    trie.insert("app")
    trie.insert("beer")
    
    # Search
    assert trie.search("apple") == True
    assert trie.search("app") == True
    assert trie.search("beer") == True
    assert trie.search("appl") == False # Prefix ada, tapi bukan end of word
    assert trie.search("orange") == False
    
    # StartsWith
    assert trie.starts_with("app") == True
    assert trie.starts_with("bee") == True
    assert trie.starts_with("ora") == False
    
    print("All Trie tests passed!")

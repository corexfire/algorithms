"""
Huffman Coding / Kode Huffman

English Description:
Huffman coding is a popular algorithm used for lossless data compression. It assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

Indonesian Description:
Kode Huffman adalah algoritma populer yang digunakan untuk kompresi data lossless. Ini memberikan kode dengan panjang variabel ke karakter input, dengan kode yang lebih pendek diberikan ke karakter yang lebih sering muncul.

Implementation Details:
- Priority Queue (Min-Heap) / Antrian Prioritas (Min-Heap):
  [EN] Used to build the Huffman tree by repeatedly extracting the two nodes with the lowest frequencies.
  [ID] Digunakan untuk membangun pohon Huffman dengan mengekstrak dua simpul dengan frekuensi terendah secara berulang.

- Tree Structure / Struktur Pohon:
  [EN] A binary tree where leaves are characters and internal nodes represent combined frequencies.
  [ID] Pohon biner di mana daun adalah karakter dan simpul internal mewakili frekuensi gabungan.

- Time Complexity / Kompleksitas Waktu:
  [EN] O(n log n) where n is the number of unique characters.
  [ID] O(n log n) di mana n adalah jumlah karakter unik.

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the tree and codes.
  [ID] O(n) untuk menyimpan pohon dan kode.

Usage Documentation:
  [EN] Use `huffman_encoding(text)` to compress and `huffman_decoding(encoded, tree)` to decompress.
  [ID] Gunakan `huffman_encoding(text)` untuk mengompresi dan `huffman_decoding(encoded, tree)` untuk mendekompresi.

  >>> text = "BCAADDDCCACACAC"
  >>> encoded, codes = huffman_encoding(text)
  >>> isinstance(encoded, str)
  True
  >>> isinstance(codes, dict)
  True
"""
import heapq
from collections import Counter
from typing import Dict, Tuple, Optional

class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text: str) -> Optional[HuffmanNode]:
    """Membangun Huffman Tree dari teks input."""
    if not text:
        return None
        
    freq_map = Counter(text)
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
        
    return priority_queue[0]

def build_codes(node: Optional[HuffmanNode], current_code: str, codes: Dict[str, str]):
    """Membuat mapping karakter ke kode Huffman."""
    if node is None:
        return
        
    if node.char is not None:
        codes[node.char] = current_code
        return
        
    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)

def huffman_encoding(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Mengompresi teks menggunakan Huffman Coding.
    
    Returns:
        encoded_text: String biner hasil kompresi.
        codes: Dictionary mapping karakter ke kode biner.
    """
    if not text:
        return "", {}
        
    root = build_huffman_tree(text)
    codes: Dict[str, str] = {}
    build_codes(root, "", codes)
    
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decoding(encoded_text: str, root: HuffmanNode) -> str:
    """Mendekode string biner kembali ke teks asli."""
    if not encoded_text or root is None:
        return ""
        
    decoded_text = []
    current_node = root
    
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
            
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root
            
    return "".join(decoded_text)

if __name__ == "__main__":
    # Test Cases
    print("Running Huffman Coding Tests...")
    
    text = "BCAADDDCCACACAC"
    encoded_text, codes = huffman_encoding(text)


"""
Disjoint Set Union (DSU) / Struktur Data Gabung-Cari

English Description:
Disjoint Set Union (DSU), also known as Union-Find, is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
It provides near-constant-time operations to add new sets, merge existing sets, and determine whether elements are in the same set.
This implementation uses Path Compression and Union by Rank optimizations.

Indonesian Description:
Disjoint Set Union (DSU), juga dikenal sebagai Union-Find, adalah struktur data yang melacak sekumpulan elemen yang dipartisi menjadi sejumlah subset yang terpisah (tidak tumpang tindih).
Ini menyediakan operasi waktu hampir konstan untuk menambah set baru, menggabungkan set yang ada, dan menentukan apakah elemen berada dalam set yang sama.
Implementasi ini menggunakan optimasi Kompresi Jalur (Path Compression) dan Penyatuan Berdasarkan Peringkat (Union by Rank).

Implementation Details:
- Find with Path Compression / Cari dengan Kompresi Jalur:
  [EN] Flattens the structure of the tree whenever `find` is used on it. Every node visited on the way to the root points directly to the root.
  [ID] Meratakan struktur pohon setiap kali `find` digunakan padanya. Setiap node yang dikunjungi dalam perjalanan ke root menunjuk langsung ke root.
  
- Union by Rank / Penyatuan Berdasarkan Peringkat:
  [EN] Attaches the shorter tree to the root of the taller tree to keep the tree height small.
  [ID] Menempelkan pohon yang lebih pendek ke akar pohon yang lebih tinggi untuk menjaga ketinggian pohon tetap kecil.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(alpha(n)) where alpha is the Inverse Ackermann function (nearly constant).
  [ID] O(alpha(n)) di mana alpha adalah fungsi Inverse Ackermann (hampir konstan).

Usage Documentation:
  [EN] Initialize DSU with size n. Use `union(i, j)` to merge sets and `find(i)` to get the representative.
  [ID] Inisialisasi DSU dengan ukuran n. Gunakan `union(i, j)` untuk menggabungkan set dan `find(i)` untuk mendapatkan perwakilan.
  
  >>> dsu = DSU(5)
  >>> dsu.union(0, 1)
  True
  >>> dsu.find(0) == dsu.find(1)
  True
"""
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, i: int) -> int:
        """Mencari representative (root) dari elemen i dengan Path Compression."""
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i: int, j: int) -> bool:
        """
        Menggabungkan set yang mengandung i dan j.
        Returns True jika berhasil digabung (sebelumnya terpisah), False jika sudah satu set.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by Rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False
        
    def connected(self, i: int, j: int) -> bool:
        """Mengecek apakah i dan j berada dalam set yang sama."""
        return self.find(i) == self.find(j)

if __name__ == "__main__":
    # Test Cases
    print("Running DSU Tests...")
    
    dsu = DSU(5) # 0, 1, 2, 3, 4
    
    # Awalnya semua terpisah
    assert dsu.connected(0, 1) == False
    
    # Union 0-1
    dsu.union(0, 1)
    assert dsu.connected(0, 1) == True
    
    # Union 2-3
    dsu.union(2, 3)
    assert dsu.connected(2, 3) == True
    assert dsu.connected(0, 2) == False
    
    # Union 1-2 (Menghubungkan set 0-1 dan 2-3)
    dsu.union(1, 2)
    assert dsu.connected(0, 3) == True # 0-1-2-3 connected
    assert dsu.connected(0, 4) == False
    
    # Cek representative
    root = dsu.find(0)
    assert dsu.find(3) == root
    
    print("All DSU tests passed!")

"""
Burrows-Wheeler Transform (BWT)
-------------------------------

1. English Description
----------------------
The Burrows-Wheeler Transform rearranges a string into runs of similar characters.
It is primarily used in data compression (e.g., bzip2) and in indexing (FM-index).
This implementation provides both the forward transform and the inverse transform.

Time Complexity: O(n^2 log n) or O(n^2) due to sorting rotations (naive implementation).
Space Complexity: O(n^2) to store rotations.

2. Indonesian Description
-------------------------
Burrows-Wheeler Transform mengatur ulang string menjadi urutan karakter yang serupa.
Ini terutama digunakan dalam kompresi data (misalnya, bzip2) dan dalam pengindeksan (FM-index).
Implementasi ini menyediakan transformasi maju dan transformasi balik (invers).

Kompleksitas Waktu: O(n^2 log n) atau O(n^2) karena pengurutan rotasi (implementasi naif).
Kompleksitas Ruang: O(n^2) untuk menyimpan rotasi.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Transform / Transformasi**:
  - [EN] Generate all cyclic rotations, sort them, and take the last column.
  - [ID] Hasilkan semua rotasi siklik, urutkan, dan ambil kolom terakhir.
- **Inverse / Invers**:
  - [EN] Reconstructs the string using the property that the first column is the sorted version of the last column.
  - [ID] Merekonstruksi string menggunakan properti bahwa kolom pertama adalah versi terurut dari kolom terakhir.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Functions / Fungsi**:
  - [EN] `bwt_transform(s)`: Returns `(transformed_string, original_index)`.
  - [ID] `bwt_transform(s)`: Mengembalikan `(transformed_string, original_index)`.
  - [EN] `bwt_inverse(last_col, idx)`: Returns the original string.
  - [ID] `bwt_inverse(last_col, idx)`: Mengembalikan string asli.
"""

def bwt_transform(s: str) -> tuple[str, int]:
    s = s + "\x00"
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations.sort()
    last_col = "".join(r[-1] for r in rotations)
    idx = rotations.index(s)
    return last_col, idx

def bwt_inverse(last_col: str, idx: int) -> str:
    n = len(last_col)
    table = [""] * n
    for _ in range(n):
        table = sorted(last_col[i] + table[i] for i in range(n))
    res = table[idx]
    return res.replace("\x00", "")

if __name__ == "__main__":
    s = "banana"
    t, i = bwt_transform(s)
    orig = bwt_inverse(t, i)
    assert orig == s
    s2 = "abracadabra"
    t2, i2 = bwt_transform(s2)
    assert bwt_inverse(t2, i2) == s2
    print("All BWT tests passed!")

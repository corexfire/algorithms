"""
Boyer-Moore String Search Algorithm (Full)
------------------------------------------

1. English Description
----------------------
The Boyer-Moore algorithm searches for occurrences of a pattern `P` in a text `T`.
It is known for its efficiency, often skipping multiple characters at a time.
This implementation includes both the Bad Character Rule and the Good Suffix Rule for maximum performance.

Time Complexity: Average O(n/m), Worst case O(nm) (though usually O(n) with Galil rule optimization, not fully present here).
Space Complexity: O(m + sigma) where sigma is alphabet size.

2. Indonesian Description
-------------------------
Algoritma Boyer-Moore mencari kemunculan pola `P` dalam teks `T`.
Dikenal karena efisiensinya, seringkali melompati beberapa karakter sekaligus.
Implementasi ini mencakup Aturan Karakter Buruk (Bad Character Rule) dan Aturan Sufiks Baik (Good Suffix Rule) untuk performa maksimal.

Kompleksitas Waktu: Rata-rata O(n/m), Kasus terburuk O(nm).
Kompleksitas Ruang: O(m + sigma) di mana sigma adalah ukuran alfabet.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Heuristics / Heuristik**:
  - [EN] **Bad Character Rule**: Shifts pattern to align the mismatching text character with its rightmost occurrence in the pattern.
  - [ID] **Aturan Karakter Buruk**: Menggeser pola untuk menyelaraskan karakter teks yang tidak cocok dengan kemunculan paling kanannya dalam pola.
  - [EN] **Good Suffix Rule**: Shifts pattern to align a matching suffix with its another occurrence in the pattern.
  - [ID] **Aturan Sufiks Baik**: Menggeser pola untuk menyelaraskan sufiks yang cocok dengan kemunculan lainnya dalam pola.
- **Preprocessing / Pra-pemrosesan**:
  - [EN] Builds lookup tables for both rules before searching.
  - [ID] Membangun tabel pencarian untuk kedua aturan sebelum pencarian.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Arguments / Argumen**:
  - [EN] `text`: Source string. `pattern`: String to search for.
  - [ID] `text`: String sumber. `pattern`: String yang dicari.
- **Return Value / Nilai Kembalian**:
  - [EN] A list of starting indices (0-based) where pattern is found.
  - [ID] Daftar indeks awal (berbasis 0) di mana pola ditemukan.
"""

from typing import List

def _build_bad_char(p: str) -> List[int]:
    m = len(p)
    table = [-1] * 256
    for i, ch in enumerate(p):
        table[ord(ch)] = i
    return table

def _build_good_suffix(p: str) -> List[int]:
    m = len(p)
    shift = [0] * (m + 1)
    bpos = [0] * (m + 1)
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and (i < m and p[i - 1] != p[j - 1]):
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]
    return shift

def boyer_moore(text: str, pattern: str) -> List[int]:
    n = len(text)
    m = len(pattern)
    if m == 0 or n < m:
        return []
    bad = _build_bad_char(pattern)
    good = _build_good_suffix(pattern)
    res: List[int] = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            res.append(s)
            s += good[0]
        else:
            bc = j - bad[ord(text[s + j])]
            gs = good[j + 1]
            s += max(1, max(bc, gs))
    return res

if __name__ == "__main__":
    t = "abacaabadcabacabaabb"
    p = "abacab"
    idxs = boyer_moore(t, p)
    for i in idxs:
        assert t[i:i+len(p)] == p
    assert idxs == [10]
    t2 = "aaaaaa"
    p2 = "aaa"
    idxs2 = boyer_moore(t2, p2)
    assert idxs2 == [0, 1, 2, 3]
    print("All Boyer-Moore full tests passed!")

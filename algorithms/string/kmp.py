"""
Knuth-Morris-Pratt (KMP) Algorithm
==================================

1. English Description
----------------------
The Knuth-Morris-Pratt (KMP) algorithm efficiently searches for occurrences of a "pattern" string within a "text" string. It avoids redundant comparisons by utilizing a precomputed Longest Prefix Suffix (LPS) array (also known as the "fail" or "next" array).

- **Logic**:
  - Preprocessing: Construct the LPS array for the pattern. `LPS[i]` stores the length of the longest proper prefix of `pattern[0...i]` that is also a suffix of `pattern[0...i]`.
  - Searching: Iterate through the text. If a mismatch occurs after `j` matches, use `LPS[j-1]` to skip unnecessary comparisons in the pattern, rather than resetting `j` to 0 or backtracking the text pointer.
- **Time Complexity**: O(N + M), where N is the length of the text and M is the length of the pattern.
- **Space Complexity**: O(M) for the LPS array.

2. Indonesian Description (Deskripsi Bahasa Indonesia)
------------------------------------------------------
Algoritma Knuth-Morris-Pratt (KMP) mencari kemunculan string "pola" (pattern) di dalam string "teks" secara efisien. Algoritma ini menghindari perbandingan yang berlebihan dengan memanfaatkan array Longest Prefix Suffix (LPS) yang dihitung sebelumnya (juga dikenal sebagai array "fail" atau "next").

- **Logika**:
  - Pra-pemrosesan: Bangun array LPS untuk pola. `LPS[i]` menyimpan panjang prefix proper terpanjang dari `pattern[0...i]` yang juga merupakan suffix dari `pattern[0...i]`.
  - Pencarian: Iterasi melalui teks. Jika ketidakcocokan terjadi setelah `j` kecocokan, gunakan `LPS[j-1]` untuk melewati perbandingan yang tidak perlu dalam pola, daripada mereset `j` ke 0 atau memundurkan pointer teks.
- **Kompleksitas Waktu**: O(N + M), di mana N adalah panjang teks dan M adalah panjang pola.
- **Kompleksitas Ruang**: O(M) untuk array LPS.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Use Cases / Kasus Penggunaan**:
  - [EN] Text editors (Search/Find feature).
  - [ID] Editor teks (Fitur Cari/Temukan).
  - [EN] DNA sequence analysis (finding gene motifs).
  - [ID] Analisis urutan DNA (mencari motif gen).
  - [EN] Spam filters and plagiarism detection.
  - [ID] Filter spam dan deteksi plagiarisme.
- **Performance / Performa**:
  - [EN] Linear time complexity makes it suitable for large texts and streams.
  - [ID] Kompleksitas waktu linear membuatnya cocok untuk teks besar dan aliran data (stream).
- **Limitations / Batasan**:
  - [EN] Slightly more complex to implement than naive search or Rabin-Karp.
  - [ID] Sedikit lebih rumit untuk diimplementasikan daripada pencarian naif atau Rabin-Karp.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **How to Use / Cara Menggunakan**:
  1. [EN] Import `kmp_search` or `kmp_search_all`.
     [ID] Impor `kmp_search` atau `kmp_search_all`.
  2. [EN] Call with text and pattern: `kmp_search(text, pattern)`.
     [ID] Panggil dengan teks dan pola: `kmp_search(text, pattern)`.
- **Dependencies / Ketergantungan**:
  - [EN] None. Pure Python.
  - [ID] Tidak ada. Python murni.
- **Testing / Pengujian**:
  - [EN] Run the file to execute built-in tests covering found/not found scenarios.
  - [ID] Jalankan file untuk mengeksekusi tes bawaan yang mencakup skenario ditemukan/tidak ditemukan.
"""

from typing import List

def compute_lps_array(pattern: str) -> List[int]:
    """
    Computes the Longest Prefix Suffix (LPS) array for the pattern.
    LPS[i] stores the length of the longest proper prefix of pattern[0...i]
    that is also a suffix of pattern[0...i].
    """
    m = len(pattern)
    lps = [0] * m
    length = 0 # Length of the previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
                # Do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> int:
    """
    KMP Search Implementation.
    
    Args:
        text: Main text string.
        pattern: Pattern string to search for.
        
    Returns:
        int: Starting index of the first occurrence, or -1 if not found.
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0
        
    lps = compute_lps_array(pattern)
    i = 0 # Index for text
    j = 0 # Index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            return i - j # Pattern found
            # j = lps[j-1] # If looking for next occurrence
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
    return -1

def kmp_search_all(text: str, pattern: str) -> List[int]:
    """
    Finds ALL occurrences of the pattern in the text.
    
    Returns:
        List[int]: List of starting indices.
    """
    n = len(text)
    m = len(pattern)
    matches = []
    
    if m == 0:
        return []
        
    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            matches.append(i - j)
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return matches

if __name__ == "__main__":
    print("KMP Algorithm Tests...")
    
    # Test 1: Standard match
    text1 = "ABABDABACDABABCABAB"
    pat1 = "ABABCABAB"
    idx1 = kmp_search(text1, pat1)
    print(f"Text: {text1}, Pattern: {pat1}, Found at: {idx1}")
    assert idx1 == 10
    
    # Test 2: Multiple occurrences
    text2 = "AABAACAADAABAABA"
    pat2 = "AABA"
    matches = kmp_search_all(text2, pat2)
    print(f"Text: {text2}, Pattern: {pat2}, All matches: {matches}")
    assert matches == [0, 9, 12]
    
    # Test 3: No match
    text3 = "ABCDE"
    pat3 = "FG"
    idx3 = kmp_search(text3, pat3)
    assert idx3 == -1
    
    print("All KMP tests passed!")

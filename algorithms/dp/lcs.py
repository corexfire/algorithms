"""
Longest Common Subsequence (LCS)
--------------------------------

1. English Description
----------------------
The Longest Common Subsequence (LCS) problem is finding the longest subsequence present in all given sequences.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
This implementation uses Dynamic Programming to solve the problem efficiently.

Time Complexity: O(m * n) where m and n are the lengths of the two strings.
Space Complexity: O(m * n) for the DP table.

2. Indonesian Description
-------------------------
Masalah Longest Common Subsequence (LCS) adalah mencari subsequence terpanjang yang ada di semua urutan yang diberikan.
Subsequence adalah urutan yang muncul dalam urutan relatif yang sama, tetapi tidak harus berurutan (kontigu).
Implementasi ini menggunakan Pemrograman Dinamis untuk menyelesaikan masalah secara efisien.

Kompleksitas Waktu: O(m * n) di mana m dan n adalah panjang dari kedua string.
Kompleksitas Ruang: O(m * n) untuk tabel DP.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **DP Table Construction / Konstruksi Tabel DP**:
  - [EN] `L[i][j]` stores the length of LCS of `X[0..i-1]` and `Y[0..j-1]`.
  - [ID] `L[i][j]` menyimpan panjang LCS dari `X[0..i-1]` dan `Y[0..j-1]`.
- **Recurrence Relation / Relasi Rekurensi**:
  - [EN] If `X[i-1] == Y[j-1]`, then `L[i][j] = 1 + L[i-1][j-1]`.
  - [ID] Jika `X[i-1] == Y[j-1]`, maka `L[i][j] = 1 + L[i-1][j-1]`.
  - [EN] Else, `L[i][j] = max(L[i-1][j], L[i][j-1])`.
  - [ID] Jika tidak, `L[i][j] = max(L[i-1][j], L[i][j-1])`.
- **Backtracking / Pelacakan Balik**:
  - [EN] To reconstruct the LCS string, we backtrack from `L[m][n]`.
  - [ID] Untuk merekonstruksi string LCS, kita melacak balik dari `L[m][n]`.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Function / Fungsi**:
  - [EN] `lcs(X, Y)` returns a tuple `(length, lcs_string)`.
  - [ID] `lcs(X, Y)` mengembalikan tuple `(panjang, string_lcs)`.
- **Input / Input**:
  - [EN] `X`: First string. `Y`: Second string.
  - [ID] `X`: String pertama. `Y`: String kedua.
"""

def lcs(X: str, Y: str) -> tuple[int, str]:
    """
    Menghitung LCS dari dua string X dan Y.
    
    Args:
        X: String pertama
        Y: String kedua
        
    Returns:
        tuple[int, str]: (Panjang LCS, String LCS)
    """
    m = len(X)
    n = len(Y)
    
    # Buat tabel DP (m+1) x (n+1)
    # L[i][j] menyimpan panjang LCS dari X[0..i-1] dan Y[0..j-1]
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Membangun tabel L secara bottom-up
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    # Panjang LCS adalah nilai di pojok kanan bawah
    length = L[m][n]
    
    # Rekonstruksi string LCS dari tabel DP
    index = length
    lcs_str_list = [""] * (index + 1)
    lcs_str_list[index] = "" # Terminator
    
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str_list[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return length, "".join(lcs_str_list)

if __name__ == "__main__":
    # Test Cases
    print("Running LCS Tests...")
    
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    length, lcs_str = lcs(X, Y)
    
    print(f"String 1: {X}")
    print(f"String 2: {Y}")
    print(f"Length of LCS: {length}")
    print(f"LCS: {lcs_str}")
    
    # Verifikasi
    # LCS dari "AGGTAB" dan "GXTXAYB" adalah "GTAB"
    # Panjang: 4
    
    assert length == 4
    assert lcs_str == "GTAB"
    
    # Test case 2
    A = "ABCBDAB"
    B = "BDCABA"
    # LCS: BCBA atau BDAB atau BCAB (Panjang 4)
    # Algoritma kita akan menghasilkan salah satu dari itu (biasanya BCBA atau BDAB tergantung arah backtrack)
    
    l_len, l_str = lcs(A, B)
    assert l_len == 4
    # Validasi bahwa string hasil adalah subsequence dari kedua string
    
    def is_subsequence(sub, main):
        it = iter(main)
        return all(c in it for c in sub)
        
    assert is_subsequence(l_str, A)
    assert is_subsequence(l_str, B)
    
    print("All LCS tests passed!")

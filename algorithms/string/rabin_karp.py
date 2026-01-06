"""
Rabin-Karp Algorithm
--------------------

1. English Description
----------------------
The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find any one of a set of pattern strings in a text.
It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions.
It is particularly effective for multiple pattern search.

Time Complexity: Average O(n + m), Worst Case O(nm) (due to hash collisions).
Space Complexity: O(1) auxiliary space.

2. Indonesian Description
-------------------------
Algoritma Rabin-Karp adalah algoritma pencarian string yang menggunakan hashing untuk menemukan salah satu dari sekumpulan string pola dalam teks.
Ini menggunakan rolling hash untuk memfilter dengan cepat posisi teks yang tidak mungkin cocok dengan pola, dan kemudian memeriksa kecocokan pada posisi yang tersisa.
Ini sangat efektif untuk pencarian banyak pola.

Kompleksitas Waktu: Rata-rata O(n + m), Kasus Terburuk O(nm) (karena tabrakan hash).
Kompleksitas Ruang: O(1) ruang tambahan.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Rolling Hash / Rolling Hash**:
  - [EN] Updates the hash value in O(1) time when sliding the window by one character.
  - [ID] Memperbarui nilai hash dalam waktu O(1) saat menggeser jendela satu karakter.
  - [EN] Formula: `new_hash = (d * (old_hash - text[old] * h) + text[new]) % q`.
  - [ID] Rumus: `new_hash = (d * (old_hash - text[old] * h) + text[new]) % q`.
- **Spurious Hits / Hit Palsu**:
  - [EN] When hash values match, actual characters are compared to verify the match.
  - [ID] Ketika nilai hash cocok, karakter sebenarnya dibandingkan untuk memverifikasi kecocokan.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Function / Fungsi**:
  - [EN] `rabin_karp(text, pattern)` returns a list of starting indices where the pattern occurs.
  - [ID] `rabin_karp(text, pattern)` mengembalikan daftar indeks awal di mana pola muncul.
- **Parameters / Parameter**:
  - [EN] `d`: Number of characters in alphabet (usually 256). `q`: A prime number (to minimize collisions).
  - [ID] `d`: Jumlah karakter dalam alfabet (biasanya 256). `q`: Bilangan prima (untuk meminimalkan tabrakan).
"""

from typing import List

def rabin_karp(text: str, pattern: str) -> List[int]:
    """
    Mencari semua kemunculan pattern dalam text.
    
    Args:
        text: String teks utama.
        pattern: String pola yang dicari.
        
    Returns:
        List[int]: List index awal kemunculan pattern (0-indexed).
    """
    d = 256 # Jumlah karakter dalam alfabet input
    q = 101 # Bilangan prima untuk modulus
    
    M = len(pattern)
    N = len(text)
    p = 0 # Hash value untuk pattern
    t = 0 # Hash value untuk text
    h = 1
    
    result = []
    
    if M > N:
        return result
        
    # Nilai h akan menjadi pow(d, M-1) % q
    for i in range(M - 1):
        h = (h * d) % q
        
    # Hitung hash value awal untuk pattern dan window pertama text
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        
    # Slide pattern over text
    for i in range(N - M + 1):
        # Jika hash match, cek karakter per karakter
        if p == t:
            match = True
            for j in range(M):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)
                
        # Hitung hash value untuk window selanjutnya
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            
            # Konversi t menjadi positif jika negatif
            if t < 0:
                t = t + q
                
    return result

if __name__ == "__main__":
    # Test Cases
    print("Running Rabin-Karp Tests...")
    
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    
    # "GEEK" muncul di index 0 dan 10
    indices = rabin_karp(txt, pat)
    print(f"Text: {txt}")
    print(f"Pattern: {pat}")
    print(f"Found indices: {indices}")
    
    assert indices == [0, 10]
    
    # Test Case 2
    txt2 = "AABAACAADAABAABA"
    pat2 = "AABA"
    # AABA di index 0, 9, 12
    indices2 = rabin_karp(txt2, pat2)
    print(f"Found indices: {indices2}")
    
    assert indices2 == [0, 9, 12]
    
    # Test Case 3 (Not found)
    assert rabin_karp("ABCDE", "XYZ") == []
    
    print("All Rabin-Karp tests passed!")

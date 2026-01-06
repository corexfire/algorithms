"""
Edit Distance (Levenshtein Distance) / Jarak Edit

English Description:
Edit Distance (specifically Levenshtein Distance) measures the minimum number of operations required to transform one string into another.
The allowed operations are: Insert a character, Remove a character, or Replace a character.
It is widely used in spell checking, DNA analysis, and natural language processing.

Indonesian Description:
Jarak Edit (khususnya Jarak Levenshtein) mengukur jumlah minimum operasi yang diperlukan untuk mengubah satu string menjadi string lain.
Operasi yang diizinkan adalah: Sisipkan karakter, Hapus karakter, atau Ganti karakter.
Ini banyak digunakan dalam pemeriksaan ejaan, analisis DNA, dan pemrosesan bahasa alami.

Implementation Details:
- DP Table / Tabel DP:
  [EN] `dp[i][j]` represents the edit distance between the first `i` characters of `str1` and the first `j` characters of `str2`.
  [ID] `dp[i][j]` merepresentasikan jarak edit antara `i` karakter pertama dari `str1` dan `j` karakter pertama dari `str2`.
  
- Transitions / Transisi:
  [EN] If characters match, `dp[i][j] = dp[i-1][j-1]`. Else, take min of insert, remove, replace + 1.
  [ID] Jika karakter cocok, `dp[i][j] = dp[i-1][j-1]`. Jika tidak, ambil min dari sisipkan, hapus, ganti + 1.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(m * n) where m and n are lengths of the two strings.
  [ID] O(m * n) di mana m dan n adalah panjang dari kedua string.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(m * n) to store the DP table.
  [ID] O(m * n) untuk menyimpan tabel DP.

Usage Documentation:
  [EN] Call `edit_distance(str1, str2)` to get the minimum number of edits.
  [ID] Panggil `edit_distance(str1, str2)` untuk mendapatkan jumlah minimum edit.
  
  >>> edit_distance("kitten", "sitting")
  3
  >>> edit_distance("sunday", "saturday")
  3
"""
def edit_distance(str1: str, str2: str) -> int:
    """
    Calculates the minimum number of operations to convert str1 to str2.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        Minimum edit distance
    """
    m = len(str1)
    n = len(str2)
    
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j
                
            # If second string is empty, only option is to
            # remove all characters of first string
            elif j == 0:
                dp[i][j] = i
                
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                 dp[i-1][j],      # Remove
                                 dp[i-1][j-1])    # Replace
                                 
    return dp[m][n]

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("sunday", "saturday", 3),
        ("kitten", "sitting", 3),
        ("horse", "ros", 3),
        ("", "abc", 3),
        ("abc", "", 3),
        ("same", "same", 0)
    ]
    
    for s1, s2, expected in test_cases:
        result = edit_distance(s1, s2)
        print(f"Edit Distance ('{s1}', '{s2}') = {result}, Expected: {expected}")
        assert result == expected
        
    print("All test cases passed!")

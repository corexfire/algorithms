"""
Longest Palindromic Subsequence (LPS) / Subsekuens Palindrom Terpanjang

English Description:
The Longest Palindromic Subsequence (LPS) problem is to find the length of the longest subsequence of a string that is also a palindrome.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a string that reads the same backward as forward.

Indonesian Description:
Masalah Subsekuens Palindrom Terpanjang (LPS) adalah mencari panjang subsekuens terpanjang dari sebuah string yang juga merupakan palindrom.
Subsekuens adalah urutan yang dapat diturunkan dari urutan lain dengan menghapus beberapa atau tidak ada elemen tanpa mengubah urutan elemen yang tersisa.
Palindrom adalah string yang dibaca sama dari belakang maupun depan.

Implementation Details:
- DP Table / Tabel DP:
  [EN] `dp[i][j]` stores the length of LPS in the substring `s[i..j]`.
  [ID] `dp[i][j]` menyimpan panjang LPS dalam substring `s[i..j]`.
  
- Recurrence / Rekurensi:
  [EN] If `s[i] == s[j]`, `dp[i][j] = 2 + dp[i+1][j-1]`. Else, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.
  [ID] Jika `s[i] == s[j]`, `dp[i][j] = 2 + dp[i+1][j-1]`. Jika tidak, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n^2) where n is the length of the string.
  [ID] O(n^2) di mana n adalah panjang string.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n^2) to store the DP table.
  [ID] O(n^2) untuk menyimpan tabel DP.

Usage Documentation:
  [EN] Call `lps_length(s)` with a string.
  [ID] Panggil `lps_length(s)` dengan sebuah string.
  
  >>> lps_length("bbbab")
  4
  >>> lps_length("cbbd")
  2
"""
def lps_length(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if j - i > 1 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

if __name__ == "__main__":
    assert lps_length("bbbab") == 4
    assert lps_length("cbbd") == 2
    assert lps_length("") == 0
    assert lps_length("a") == 1
    print("All LPS tests passed!")

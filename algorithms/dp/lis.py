"""
Longest Increasing Subsequence (LIS) / Subsekuens Naik Terpanjang

English Description:
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Indonesian Description:
Masalah Subsekuens Naik Terpanjang (LIS) adalah mencari panjang subsekuens terpanjang dari urutan yang diberikan sehingga semua elemen subsekuens diurutkan dalam urutan menaik.
Subsekuens adalah urutan yang dapat diturunkan dari urutan lain dengan menghapus beberapa atau tidak ada elemen tanpa mengubah urutan elemen yang tersisa.

Implementation Details:
- DP Approach / Pendekatan DP:
  [EN] `dp[i]` stores the length of LIS ending at index `i`. For each `j < i`, if `nums[i] > nums[j]`, update `dp[i] = max(dp[i], dp[j] + 1)`.
  [ID] `dp[i]` menyimpan panjang LIS yang berakhir pada indeks `i`. Untuk setiap `j < i`, jika `nums[i] > nums[j]`, perbarui `dp[i] = max(dp[i], dp[j] + 1)`.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n^2) for this DP implementation.
  [ID] O(n^2) untuk implementasi DP ini.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the DP array.
  [ID] O(n) untuk menyimpan array DP.

Usage Documentation:
  [EN] Call `longest_increasing_subsequence(nums)` with a list of integers.
  [ID] Panggil `longest_increasing_subsequence(nums)` dengan daftar bilangan bulat.
  
  >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
  4
  >>> longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
  4
"""
from typing import List

def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Finds the length of LIS.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of longest increasing subsequence
    """
    if not nums:
        return 0
        
    n = len(nums)
    # dp[i] = length of LIS ending at index i
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # [2, 3, 7, 101]
        ([0, 1, 0, 3, 2, 3], 4),            # [0, 1, 2, 3]
        ([7, 7, 7, 7, 7, 7, 7], 1),         # [7]
        ([], 0)
    ]
    
    for nums, expected in test_cases:
        result = longest_increasing_subsequence(nums)
        print(f"Input: {nums} -> LIS Length: {result}, Expected: {expected}")
        assert result == expected
        
    print("All test cases passed!")

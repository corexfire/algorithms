"""
Coin Change Problem / Masalah Penukaran Koin

English Description:
The Coin Change problem is a classic dynamic programming problem.
Given a set of coin values and a target amount, find the minimum number of coins needed to make up that amount.
If it is not possible to make up the amount with the given coins, return -1.

Indonesian Description:
Masalah Penukaran Koin (Coin Change Problem) adalah masalah pemrograman dinamis klasik.
Diberikan sekumpulan nilai koin dan jumlah target, temukan jumlah minimum koin yang diperlukan untuk mencapai jumlah tersebut.
Jika tidak mungkin mencapai jumlah tersebut dengan koin yang diberikan, kembalikan -1.

Implementation Details:
- Dynamic Programming / Pemrograman Dinamis:
  [EN] We build a DP table `dp[i]` where `dp[i]` stores the minimum coins needed for amount `i`.
  [ID] Kita membangun tabel DP `dp[i]` di mana `dp[i]` menyimpan jumlah koin minimum yang diperlukan untuk jumlah `i`.
  
- Initialization / Inisialisasi:
  [EN] `dp[0] = 0` (0 coins for 0 amount), others initialized to `amount + 1` (representing infinity).
  [ID] `dp[0] = 0` (0 koin untuk jumlah 0), yang lain diinisialisasi ke `amount + 1` (mewakili tak hingga).
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(amount * n), where n is the number of coin types.
  [ID] O(amount * n), di mana n adalah jumlah jenis koin.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(amount) to store the DP table.
  [ID] O(amount) untuk menyimpan tabel DP.

Usage Documentation:
  [EN] Call `coin_change(coins, amount)` with a list of coin denominations and the target amount.
  [ID] Panggil `coin_change(coins, amount)` dengan daftar denominasi koin dan jumlah target.
  
  >>> coins = [1, 2, 5]
  >>> amount = 11
  >>> coin_change(coins, amount)
  3
  >>> coin_change([2], 3)
  -1
"""
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    """
    Finds minimum coins to make up amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        Minimum number of coins or -1 if impossible
    """
    # dp[i] = min coins to make amount i
    # Initialize with amount + 1 (infinity equivalent for this problem)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 5], 11, 3),   # 5 + 5 + 1
        ([2], 3, -1),         # Impossible
        ([1], 0, 0),          # 0 coins for 0 amount
        ([1, 3, 4, 5], 7, 2)  # 3 + 4
    ]
    
    for coins, amount, expected in test_cases:
        result = coin_change(coins, amount)
        print(f"Coins: {coins}, Amount: {amount} -> Result: {result}, Expected: {expected}")
        assert result == expected
        
    print("All test cases passed!")

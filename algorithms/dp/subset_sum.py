"""
Subset Sum Problem / Masalah Jumlah Subset

English Description:
The Subset Sum Problem is a decision problem in computer science.
Given a set of integers and a target value, determine if there is a non-empty subset of the sum of whose elements is equal to the target value.
This implementation also returns the subset itself if found.

Indonesian Description:
Masalah Jumlah Subset (Subset Sum Problem) adalah masalah keputusan dalam ilmu komputer.
Diberikan sekumpulan bilangan bulat dan nilai target, tentukan apakah ada subset tidak kosong yang jumlah elemennya sama dengan nilai target.
Implementasi ini juga mengembalikan subset itu sendiri jika ditemukan.

Implementation Details:
- DP Table / Tabel DP:
  [EN] `dp[i][s]` is True if sum `s` can be formed using a subset of the first `i` items.
  [ID] `dp[i][s]` adalah True jika jumlah `s` dapat dibentuk menggunakan subset dari `i` item pertama.
  
- Backtracking / Pelacakan Balik:
  [EN] After filling the DP table, we backtrack to find the elements that make up the sum.
  [ID] Setelah mengisi tabel DP, kita melacak balik untuk menemukan elemen yang membentuk jumlah tersebut.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n * target) where n is the number of items.
  [ID] O(n * target) di mana n adalah jumlah item.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n * target) to store the DP table.
  [ID] O(n * target) untuk menyimpan tabel DP.

Usage Documentation:
  [EN] Call `subset_sum(nums, target)` to get `(found, subset)`.
  [ID] Panggil `subset_sum(nums, target)` untuk mendapatkan `(ditemukan, subset)`.
  
  >>> subset_sum([3, 34, 4, 12, 5, 2], 9)
  (True, [4, 5])
  >>> subset_sum([3, 34, 4, 12, 5, 2], 30)
  (False, [])
"""
from typing import List, Tuple

def subset_sum(nums: List[int], target: int) -> Tuple[bool, List[int]]:
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = True
        for s in range(1, target + 1):
            dp[i][s] = dp[i - 1][s] or (s >= nums[i - 1] and dp[i - 1][s - nums[i - 1]])
    if not dp[n][target]:
        return False, []
    res: List[int] = []
    s = target
    i = n
    while i > 0 and s > 0:
        if dp[i - 1][s]:
            i -= 1
        else:
            res.append(nums[i - 1])
            s -= nums[i - 1]
            i -= 1
    res.reverse()
    return True, res

if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    ok, subset = subset_sum(nums, target)
    print(f"Found: {ok}, subset: {subset}")
    assert ok and sum(subset) == target
    ok2, subset2 = subset_sum(nums, 30)
    assert not ok2
    print("All Subset Sum tests passed!")

"""
Egg Dropping Puzzle (Dynamic Programming)
-----------------------------------------

1. English Description
----------------------
The Egg Dropping Puzzle asks for the minimum number of attempts needed in the worst case to determine the highest floor from which an egg will not break.
You are given `k` eggs and `n` floors.
This implementation uses an optimized Dynamic Programming approach based on the number of moves.

Time Complexity: O(k * log n) or O(k * m) where m is the answer.
Space Complexity: O(k)

2. Indonesian Description
-------------------------
Teka-teki Menjatuhkan Telur (Egg Dropping Puzzle) menanyakan jumlah percobaan minimum yang diperlukan dalam kasus terburuk untuk menentukan lantai tertinggi di mana telur tidak akan pecah.
Anda diberikan `k` telur dan `n` lantai.
Implementasi ini menggunakan pendekatan Pemrograman Dinamis yang dioptimalkan berdasarkan jumlah langkah.

Kompleksitas Waktu: O(k * log n) atau O(k * m) di mana m adalah jawabannya.
Kompleksitas Ruang: O(k)

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Concept / Konsep**:
  - [EN] Instead of finding min moves for `n` floors, we find max floors coverable with `m` moves and `k` eggs.
  - [ID] Alih-alih mencari min langkah untuk `n` lantai, kita mencari max lantai yang bisa dicakup dengan `m` langkah dan `k` telur.
- **Recurrence / Rekurensi**:
  - [EN] `dp[e] = dp[e] + dp[e-1] + 1` (current = survived + broken + current_floor).
  - [ID] `dp[e] = dp[e] + dp[e-1] + 1` (saat ini = selamat + pecah + lantai_saat_ini).

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Arguments / Argumen**:
  - [EN] `eggs`: Number of eggs available. `floors`: Total number of floors.
  - [ID] `eggs`: Jumlah telur yang tersedia. `floors`: Total jumlah lantai.
- **Output / Keluaran**:
  - [EN] Minimum number of drops required in the worst case.
  - [ID] Jumlah minimum jatuhan yang diperlukan dalam kasus terburuk.
"""

def egg_drop(eggs: int, floors: int) -> int:
    dp = [0] * (eggs + 1)
    moves = 0
    while dp[eggs] < floors:
        moves += 1
        for e in range(eggs, 0, -1):
            dp[e] = dp[e] + dp[e - 1] + 1
    return moves

if __name__ == "__main__":
    assert egg_drop(1, 10) == 10
    assert egg_drop(2, 100) == 14
    assert egg_drop(3, 100) == 9
    print("All Egg Dropping tests passed!")

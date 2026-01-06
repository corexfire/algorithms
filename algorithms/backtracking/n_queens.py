"""
N-Queens Problem
----------------

1. English Description
----------------------
The N-Queens puzzle is the problem of placing `N` chess queens on an `N×N` chessboard so that no two queens threaten each other.
Thus, a solution requires that no two queens share the same row, column, or diagonal.
This implementation uses backtracking to find all distinct solutions.

Time Complexity: O(N!)
Space Complexity: O(N) for recursion stack and state sets.

2. Indonesian Description
-------------------------
Teka-teki N-Queens adalah masalah menempatkan `N` ratu catur di papan catur `N×N` sehingga tidak ada dua ratu yang saling menyerang.
Jadi, solusi mengharuskan tidak ada dua ratu yang berbagi baris, kolom, atau diagonal yang sama.
Implementasi ini menggunakan backtracking untuk menemukan semua solusi yang berbeda.

Kompleksitas Waktu: O(N!)
Kompleksitas Ruang: O(N) untuk tumpukan rekursi dan set status.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Backtracking / Backtracking**:
  - [EN] Places queens row by row. If a valid position is found, recurse to next row.
  - [ID] Menempatkan ratu baris demi baris. Jika posisi valid ditemukan, rekursi ke baris berikutnya.
- **Safety Check / Cek Keamanan**:
  - [EN] Uses sets (`cols`, `pos_diag`, `neg_diag`) for O(1) lookups of validity.
  - [ID] Menggunakan set (`cols`, `pos_diag`, `neg_diag`) untuk pencarian validitas O(1).
  - [EN] `pos_diag`: `row + col` is constant. `neg_diag`: `row - col` is constant.
  - [ID] `pos_diag`: `row + col` konstan. `neg_diag`: `row - col` konstan.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Function / Fungsi**:
  - [EN] `solve_n_queens(n)` returns a list of solutions, where each solution is a list of strings representing rows.
  - [ID] `solve_n_queens(n)` mengembalikan daftar solusi, di mana setiap solusi adalah daftar string yang mewakili baris.
"""

from typing import List, Set

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Menyelesaikan masalah N-Queens menggunakan backtracking.
    
    Args:
        n: Ukuran papan catur (n x n).
        
    Returns:
        List[List[str]]: Daftar solusi. Setiap solusi adalah representasi papan.
    """
    solutions: List[List[str]] = []
    board: List[str] = ["." * n for _ in range(n)]
    
    # Set untuk melacak kolom dan diagonal yang sudah terisi
    cols: Set[int] = set()
    pos_diag: Set[int] = set() # (r + c) constant
    neg_diag: Set[int] = set() # (r - c) constant
    
    def backtrack(row: int):
        if row == n:
            solutions.append(board[:])
            return
            
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
                
            # Place Queen
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            
            # Modifikasi string board (immutable in Python, so replace row)
            board[row] = board[row][:col] + "Q" + board[row][col+1:]
            
            backtrack(row + 1)
            
            # Remove Queen (Backtrack)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row] = "." * n
            
    backtrack(0)
    return solutions

if __name__ == "__main__":
    # Test cases
    print("Running N-Queens Tests...")
    
    # Test case 1: N=4
    # Solusi untuk N=4 ada 2
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for N={n}: {len(solutions)}")
    
    for i, sol in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in sol:
            print(row)
        print()
        
    assert len(solutions) == 2, "Test case N=4 failed"
    
    # Test case 2: N=1 (Trivial)
    assert len(solve_n_queens(1)) == 1, "Test case N=1 failed"
    
    # Test case 3: N=2, N=3 (No solution)
    assert len(solve_n_queens(2)) == 0, "Test case N=2 failed"
    assert len(solve_n_queens(3)) == 0, "Test case N=3 failed"
    
    print("All N-Queens tests passed!")

"""
Sudoku Solver / Pemecah Sudoku

English Description:
A backtracking algorithm to solve 9x9 Sudoku puzzles. It fills the empty cells (represented by 0) with numbers from 1 to 9, ensuring that each number appears exactly once in each row, column, and 3x3 subgrid.

Indonesian Description:
Algoritma backtracking untuk menyelesaikan teka-teki Sudoku 9x9. Ini mengisi sel-sel kosong (diwakili oleh 0) dengan angka dari 1 hingga 9, memastikan bahwa setiap angka muncul tepat satu kali di setiap baris, kolom, dan subgrid 3x3.

Implementation Details:
- Backtracking / Backtracking:
  [EN] The algorithm tries placing a number, checks validity, and recursively attempts to solve the rest. If it hits a dead end, it backtracks (resets the cell to 0).
  [ID] Algoritma mencoba menempatkan angka, memeriksa validitas, dan secara rekursif mencoba menyelesaikan sisanya. Jika menemui jalan buntu, ia melakukan backtrack (mengatur ulang sel ke 0).

- Validation / Validasi:
  [EN] Checks if a number exists in the current row, current column, or current 3x3 box.
  [ID] Memeriksa apakah angka ada di baris saat ini, kolom saat ini, atau kotak 3x3 saat ini.

- Time Complexity / Kompleksitas Waktu:
  [EN] O(9^m) where m is the number of empty cells (worst case exponential).
  [ID] O(9^m) di mana m adalah jumlah sel kosong (kasus terburuk eksponensial).

- Space Complexity / Kompleksitas Ruang:
  [EN] O(m) for the recursion stack.
  [ID] O(m) untuk tumpukan rekursi.

Usage Documentation:
  [EN] Call `solve_sudoku(board)` to solve the puzzle in-place. Returns True if solvable.
  [ID] Panggil `solve_sudoku(board)` untuk menyelesaikan teka-teki di tempat. Mengembalikan True jika dapat diselesaikan.

  >>> board = [
  ...     [5, 3, 0, 0, 7, 0, 0, 0, 0],
  ...     [6, 0, 0, 1, 9, 5, 0, 0, 0],
  ...     [0, 9, 8, 0, 0, 0, 0, 6, 0],
  ...     [8, 0, 0, 0, 6, 0, 0, 0, 3],
  ...     [4, 0, 0, 8, 0, 3, 0, 0, 1],
  ...     [7, 0, 0, 0, 2, 0, 0, 0, 6],
  ...     [0, 6, 0, 0, 0, 0, 2, 8, 0],
  ...     [0, 0, 0, 4, 1, 9, 0, 0, 5],
  ...     [0, 0, 0, 0, 8, 0, 0, 7, 9]
  ... ]
  >>> solve_sudoku(board)
  True
  >>> board[0][0]
  5
"""
from typing import List

Board = List[List[int]]

def is_valid(board: Board, row: int, col: int, num: int) -> bool:
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty(board: Board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board: Board) -> bool:
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solved = solve_sudoku(puzzle)
    print(f"Solved: {solved}")
    assert solved
    for row in puzzle:
        assert all(1 <= v <= 9 for v in row)
    print("Sudoku solved and validated!")

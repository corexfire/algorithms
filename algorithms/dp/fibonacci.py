"""
Fibonacci Sequence / Deret Fibonacci

English Description:
The Fibonacci sequence is a series of numbers in which each number (Fibonacci number) is the sum of the two preceding ones.
Usually, the sequence starts with 0 and 1.
The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
This module provides multiple implementations ranging from naive recursive to optimized iterative approaches.

Indonesian Description:
Deret Fibonacci adalah serangkaian angka di mana setiap angka (bilangan Fibonacci) adalah jumlah dari dua angka sebelumnya.
Biasanya, deret dimulai dengan 0 dan 1.
Urutannya adalah: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Modul ini menyediakan beberapa implementasi mulai dari rekursif naif hingga pendekatan iteratif yang dioptimalkan.

Implementation Details:
- Recursive Approach / Pendekatan Rekursif:
  [EN] Naive implementation. Very slow O(2^n) due to redundant calculations.
  [ID] Implementasi naif. Sangat lambat O(2^n) karena perhitungan berulang.
  
- Memoization (Top-Down DP) / Memoization (DP Top-Down):
  [EN] Caches results of subproblems. Reduces complexity to O(n).
  [ID] Menyimpan hasil submasalah. Mengurangi kompleksitas menjadi O(n).
  
- Iterative (Bottom-Up DP) / Iteratif (DP Bottom-Up):
  [EN] Builds the solution from base cases up. O(n) time and O(1) space (optimized).
  [ID] Membangun solusi dari kasus dasar ke atas. Waktu O(n) dan ruang O(1) (dioptimalkan).
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n) for DP approaches.
  [ID] O(n) untuk pendekatan DP.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) for memoization (recursion stack + map), O(1) for optimized iterative.
  [ID] O(n) untuk memoization (tumpukan rekursi + map), O(1) untuk iteratif yang dioptimalkan.

Usage Documentation:
  [EN] Call `fibonacci_iterative(n)` for the most efficient calculation of the nth Fibonacci number.
  [ID] Panggil `fibonacci_iterative(n)` untuk perhitungan bilangan Fibonacci ke-n yang paling efisien.
  
  >>> fibonacci_iterative(10)
  55
  >>> fibonacci_iterative(0)
  0
"""
from typing import Dict

def fibonacci_recursive(n: int) -> int:
    """
    Implementasi rekursif naif.
    Sangat lambat untuk n > 30.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n: int, memo: Dict[int, int] = {}) -> int:
    """
    Implementasi menggunakan Memoization (Top-Down DP).
    Menyimpan hasil perhitungan sebelumnya.
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_iterative(n: int) -> int:
    """
    Implementasi iteratif (Space Optimized Bottom-Up DP).
    Paling efisien untuk penggunaan umum.
    Kompleksitas Ruang: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b

if __name__ == "__main__":
    # Test cases
    print("Running Fibonacci Tests...")
    
    # Test case 1: n = 10 -> 55
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    n = 10
    expected = 55
    
    print(f"Fib({n}) Recursive: {fibonacci_recursive(n)}")
    assert fibonacci_recursive(n) == expected, "Recursive failed"
    
    # Reset memo for clean test (though not strictly necessary as logic holds)
    print(f"Fib({n}) Memoization: {fibonacci_memoization(n, {})}")
    assert fibonacci_memoization(n, {}) == expected, "Memoization failed"
    
    print(f"Fib({n}) Iterative: {fibonacci_iterative(n)}")
    assert fibonacci_iterative(n) == expected, "Iterative failed"
    
    # Test case 2: n = 0
    assert fibonacci_iterative(0) == 0, "Test case n=0 failed"
    
    # Test case 3: Performance check (Recursive will hang on large n, so we test Iterative)
    # n = 50 -> 12586269025
    large_n = 50
    large_res = fibonacci_iterative(large_n)
    print(f"Fib({large_n}) Iterative: {large_res}")
    assert large_res == 12586269025, "Large n test failed"

    print("All Fibonacci tests passed!")

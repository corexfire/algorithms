"""
Description:
    [EN] The Euclidean Algorithm is an efficient method for computing the Greatest Common Divisor (GCD) of two numbers, which is the largest number that divides both of them without leaving a remainder.
    [ID] Algoritma Euclidean adalah metode efisien untuk menghitung Faktor Persekutuan Terbesar (FPB) dari dua bilangan, yaitu bilangan terbesar yang dapat membagi kedua bilangan tersebut tanpa sisa.

Implementation Details:
    [EN]
    - The algorithm relies on the principle that the GCD of two numbers also divides their difference.
    - More efficiently, `GCD(a, b) = GCD(b, a % b)`.
    - This process repeats until `b` becomes 0, at which point `a` is the GCD.
    - Time Complexity: O(log(min(a, b))).
    - Space Complexity: O(1) for iterative, O(log(min(a, b))) for recursive due to stack depth.
    [ID]
    - Algoritma ini bergantung pada prinsip bahwa FPB dari dua bilangan juga membagi selisih keduanya.
    - Lebih efisien menggunakan prinsip `GCD(a, b) = GCD(b, a % b)`.
    - Proses ini berulang hingga `b` menjadi 0, di mana `a` adalah FPB-nya.
    - Kompleksitas Waktu: O(log(min(a, b))).
    - Kompleksitas Ruang: O(1) untuk iteratif, O(log(min(a, b))) untuk rekursif karena kedalaman stack.

Usage Documentation:
    [EN]
    - Input: Two non-negative integers `a` and `b`.
    - Functions: `gcd_recursive(a, b)` and `gcd_iterative(a, b)`.
    - Returns: The Greatest Common Divisor (integer).
    [ID]
    - Input: Dua bilangan bulat non-negatif `a` dan `b`.
    - Fungsi: `gcd_recursive(a, b)` dan `gcd_iterative(a, b)`.
    - Mengembalikan: Faktor Persekutuan Terbesar (integer).

Examples:
    >>> gcd_iterative(48, 18)
    6
    >>> gcd_recursive(101, 103)
    1
"""

def gcd_recursive(a: int, b: int) -> int:
    """
    Implementasi Euclidean Algorithm secara rekursif.
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def gcd_iterative(a: int, b: int) -> int:
    """
    Implementasi Euclidean Algorithm secara iteratif.
    Lebih efisien dalam penggunaan memori (menghindari stack overflow).
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Test cases
    print("Running Euclidean Algorithm Tests...")
    
    # Test case 1: FPB dari 48 dan 18 adalah 6
    # 48 = 2^4 * 3
    # 18 = 2 * 3^2
    # FPB = 2 * 3 = 6
    a, b = 48, 18
    print(f"GCD({a}, {b}) -> Recursive: {gcd_recursive(a, b)}, Iterative: {gcd_iterative(a, b)}")
    assert gcd_recursive(a, b) == 6, "Test case 1 recursive failed"
    assert gcd_iterative(a, b) == 6, "Test case 1 iterative failed"
    
    # Test case 2: Salah satu bilangan prima
    a, b = 101, 103
    print(f"GCD({a}, {b}) -> {gcd_iterative(a, b)}")
    assert gcd_iterative(a, b) == 1, "Test case 2 failed"
    
    # Test case 3: Salah satu bilangan 0
    # GCD(a, 0) = a
    a, b = 5, 0
    print(f"GCD({a}, {b}) -> {gcd_iterative(a, b)}")
    assert gcd_iterative(a, b) == 5, "Test case 3 failed"
    
    # Test case 4: Bilangan sama
    a, b = 12, 12
    print(f"GCD({a}, {b}) -> {gcd_iterative(a, b)}")
    assert gcd_iterative(a, b) == 12, "Test case 4 failed"

    print("All Euclidean Algorithm tests passed!")

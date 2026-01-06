"""
Description:
    [EN] Bit Manipulation involves using bitwise operators to perform operations at the bit level. This technique is crucial for low-level programming, optimization, and solving algorithmic problems efficiently. This module provides a collection of common bit manipulation utilities.
    [ID] Manipulasi Bit melibatkan penggunaan operator bitwise untuk melakukan operasi pada tingkat bit. Teknik ini sangat penting untuk pemrograman tingkat rendah, optimasi, dan penyelesaian masalah algoritma secara efisien. Modul ini menyediakan kumpulan utilitas manipulasi bit yang umum.

Implementation Details:
    [EN]
    - `is_even`: Checks the least significant bit (LSB). If LSB is 0, the number is even. O(1).
    - `is_power_of_two`: A power of 2 has exactly one bit set. `n & (n-1)` removes the rightmost set bit. If the result is 0, it was a power of 2. O(1).
    - `count_set_bits`: Uses Brian Kernighan's Algorithm. Iteratively clears the least significant set bit until the number becomes 0. Time complexity is O(k) where k is the number of set bits.
    - Basic operations (Get, Set, Clear, Toggle): Use bitwise shifts (`<<`, `>>`) combined with AND (`&`), OR (`|`), XOR (`^`), and NOT (`~`). O(1).
    - `swap_xor`: Swaps two numbers without a temporary variable using the property `x ^ x = 0`. O(1).
    [ID]
    - `is_even`: Memeriksa Least Significant Bit (LSB). Jika LSB adalah 0, angkanya genap. O(1).
    - `is_power_of_two`: Pangkat 2 memiliki tepat satu bit yang di-set. `n & (n-1)` menghapus bit set paling kanan. Jika hasilnya 0, itu adalah pangkat 2. O(1).
    - `count_set_bits`: Menggunakan Algoritma Brian Kernighan. Secara iteratif menghapus bit set paling kanan hingga angka menjadi 0. Kompleksitas waktu adalah O(k) di mana k adalah jumlah bit yang di-set.
    - Operasi dasar (Get, Set, Clear, Toggle): Menggunakan geseran bit (`<<`, `>>`) dikombinasikan dengan AND (`&`), OR (`|`), XOR (`^`), dan NOT (`~`). O(1).
    - `swap_xor`: Menukar dua angka tanpa variabel sementara menggunakan sifat `x ^ x = 0`. O(1).

Usage Documentation:
    [EN]
    - Functions available: `is_even(n)`, `is_power_of_two(n)`, `count_set_bits(n)`, `get_bit(n, k)`, `set_bit(n, k)`, `clear_bit(n, k)`, `toggle_bit(n, k)`, `swap_xor(a, b)`.
    - Input: Integers. `k` represents the 0-indexed bit position.
    [ID]
    - Fungsi yang tersedia: `is_even(n)`, `is_power_of_two(n)`, `count_set_bits(n)`, `get_bit(n, k)`, `set_bit(n, k)`, `clear_bit(n, k)`, `toggle_bit(n, k)`, `swap_xor(a, b)`.
    - Input: Integer. `k` merepresentasikan posisi bit (0-indexed).

Examples:
    >>> is_even(4)
    True
    >>> count_set_bits(7) # 111 in binary
    3
    >>> set_bit(5, 1) # 101 -> 111 (7)
    7
"""

def is_even(n: int) -> bool:
    """Mengecek apakah angka genap."""
    return (n & 1) == 0

def is_power_of_two(n: int) -> bool:
    """Mengecek apakah angka adalah pangkat 2."""
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n: int) -> int:
    """Menghitung jumlah bit 1 (Brian Kernighan's Algorithm)."""
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

def get_bit(n: int, k: int) -> int:
    """Mengambil nilai bit ke-k (0-indexed)."""
    return (n >> k) & 1

def set_bit(n: int, k: int) -> int:
    """Mengatur bit ke-k menjadi 1."""
    return n | (1 << k)

def clear_bit(n: int, k: int) -> int:
    """Mengatur bit ke-k menjadi 0."""
    return n & ~(1 << k)

def toggle_bit(n: int, k: int) -> int:
    """Mengubah nilai bit ke-k (0 jadi 1, 1 jadi 0)."""
    return n ^ (1 << k)

def swap_xor(a: int, b: int) -> tuple[int, int]:
    """Menukar dua nilai menggunakan XOR (tanpa variabel temp)."""
    if a == b:
        return a, b
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    # Test Cases
    print("Running Bit Manipulation Tests...")
    
    # Test is_even
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    
    # Test is_power_of_two
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(4) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(0) == False
    
    # Test count_set_bits
    # 5 = 101 (2 set bits)
    # 7 = 111 (3 set bits)
    # 8 = 1000 (1 set bit)
    assert count_set_bits(5) == 2
    assert count_set_bits(7) == 3
    assert count_set_bits(8) == 1
    
    # Test bit operations
    n = 5 # 101
    
    # Get bit
    assert get_bit(n, 0) == 1
    assert get_bit(n, 1) == 0
    assert get_bit(n, 2) == 1
    
    # Set bit
    # 5 (101) set bit 1 -> 111 (7)
    assert set_bit(n, 1) == 7
    
    # Clear bit
    # 5 (101) clear bit 0 -> 100 (4)
    assert clear_bit(n, 0) == 4
    
    # Toggle bit
    # 5 (101) toggle bit 0 -> 100 (4)
    # 5 (101) toggle bit 1 -> 111 (7)
    assert toggle_bit(n, 0) == 4
    assert toggle_bit(n, 1) == 7
    
    # Swap XOR
    x, y = 10, 20
    nx, ny = swap_xor(x, y)
    assert nx == 20
    assert ny == 10
    
    print("All Bit Manipulation tests passed!")

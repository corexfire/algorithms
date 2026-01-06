"""
Description:
    [EN] Modular Exponentiation is an algorithm for efficiently computing the remainder of a large number raised to a power, i.e., `(base^exponent) % modulus`. It is fundamental in public-key cryptography (like RSA and Diffie-Hellman).
    [ID] Modular Exponentiation adalah algoritma untuk menghitung sisa bagi dari bilangan besar yang dipangkatkan secara efisien, yaitu `(base^exponent) % modulus`. Ini adalah dasar dalam kriptografi kunci publik (seperti RSA dan Diffie-Hellman).

Implementation Details:
    [EN]
    - Uses "Exponentiation by Squaring" to reduce time complexity.
    - If the exponent is odd, multiply the result by the current base.
    - If the exponent is even, square the base and halve the exponent.
    - All operations are performed modulo `m` to keep numbers manageable.
    - Time Complexity: O(log exponent).
    - Space Complexity: O(1).
    [ID]
    - Menggunakan "Exponentiation by Squaring" untuk mengurangi kompleksitas waktu.
    - Jika eksponen ganjil, kalikan hasil dengan basis saat ini.
    - Jika eksponen genap, kuadratkan basis dan bagi dua eksponennya.
    - Semua operasi dilakukan modulo `m` untuk menjaga angka tetap terkendali.
    - Kompleksitas Waktu: O(log exponent).
    - Kompleksitas Ruang: O(1).

Usage Documentation:
    [EN]
    - Input: `base`, `exponent` (non-negative), and `modulus` (positive).
    - Call `modular_exponentiation(base, exponent, modulus)` to compute the result.
    [ID]
    - Input: `base`, `exponent` (non-negatif), dan `modulus` (positif).
    - Panggil `modular_exponentiation(base, exponent, modulus)` untuk menghitung hasil.

Examples:
    >>> modular_exponentiation(2, 10, 1000)
    24
    >>> modular_exponentiation(5, 0, 10)
    1
"""

def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Calculates (base^exponent) % modulus efficiently.
    
    Args:
        base: The base integer
        exponent: The exponent integer (must be non-negative)
        modulus: The modulus integer (must be positive)
        
    Returns:
        The result of (base^exponent) % modulus
    """
    if modulus == 1:
        return 0
        
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus
            
        # Exponent must be even now
        exponent = exponent // 2
        base = (base * base) % modulus
        
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (2, 10, 1000, 24),     # 1024 % 1000 = 24
        (2, 3, 5, 3),          # 8 % 5 = 3
        (5, 0, 10, 1),         # 1 % 10 = 1
        (2312, 3434, 13, 2312**3434 % 13), # Large numbers
        (10, 10, 1, 0)         # Mod 1 is always 0
    ]
    
    for base, exp, mod, expected in test_cases:
        result = modular_exponentiation(base, exp, mod)
        print(f"({base}^{exp}) % {mod} = {result}, Expected: {expected}")
        assert result == expected
        
    print("All test cases passed!")

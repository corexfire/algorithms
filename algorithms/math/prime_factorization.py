"""
Description:
    [EN] Prime Factorization decomposes a composite number into a product of prime numbers. According to the Fundamental Theorem of Arithmetic, every integer greater than 1 is either a prime itself or can be represented as the product of prime numbers in a unique way (ignoring order).
    [ID] Faktorisasi Prima menguraikan bilangan komposit menjadi hasil kali bilangan prima. Menurut Teorema Dasar Aritmatika, setiap bilangan bulat lebih besar dari 1 adalah bilangan prima atau dapat direpresentasikan sebagai hasil kali bilangan prima dengan cara yang unik (mengabaikan urutan).

Implementation Details:
    [EN]
    - First, divide by 2 repeatedly to remove all factors of 2.
    - Then, iterate from 3 up to `sqrt(n)`, skipping even numbers (step=2).
    - If `n` is divisible by the current number `i`, add `i` to the list and divide `n` by `i`.
    - If `n` remains greater than 2 after the loop, the remaining `n` is a prime factor.
    - Time Complexity: O(sqrt(n)).
    - Space Complexity: O(log n) to store the factors.
    [ID]
    - Pertama, bagi dengan 2 berulang kali untuk menghapus semua faktor 2.
    - Kemudian, iterasi dari 3 hingga `sqrt(n)`, lewati bilangan genap (step=2).
    - Jika `n` habis dibagi oleh bilangan saat ini `i`, tambahkan `i` ke daftar dan bagi `n` dengan `i`.
    - Jika `n` tetap lebih besar dari 2 setelah loop, sisa `n` adalah faktor prima.
    - Kompleksitas Waktu: O(sqrt(n)).
    - Kompleksitas Ruang: O(log n) untuk menyimpan faktor-faktor.

Usage Documentation:
    [EN]
    - Input: Integer `n`.
    - Function: `prime_factorization(n)` returns a list of factors.
    - Function: `get_prime_factors_map(n)` returns a dictionary `{factor: count}`.
    [ID]
    - Input: Integer `n`.
    - Fungsi: `prime_factorization(n)` mengembalikan daftar faktor.
    - Fungsi: `get_prime_factors_map(n)` mengembalikan dictionary `{faktor: jumlah}`.

Examples:
    >>> prime_factorization(315)
    [3, 3, 5, 7]
    >>> get_prime_factors_map(100)
    {2: 2, 5: 2}
"""

from typing import List, Dict

def prime_factorization(n: int) -> List[int]:
    """
    Returns a list of prime factors of n.
    
    Args:
        n: The number to factorize
        
    Returns:
        List of prime factors (including duplicates)
    """
    factors = []
    
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
        
    # n must be odd at this point. So we can skip one element
    # (Note i = i + 2)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
            
    # This condition is to handle the case when n is a prime number
    # greater than 2
    if n > 2:
        factors.append(n)
        
    return factors

def get_prime_factors_map(n: int) -> Dict[int, int]:
    """Returns a dictionary of prime factors and their exponents."""
    factors = prime_factorization(n)
    factors_map = {}
    for factor in factors:
        factors_map[factor] = factors_map.get(factor, 0) + 1
    return factors_map

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (315, [3, 3, 5, 7]),  # 315 = 3*3*5*7
        (12, [2, 2, 3]),      # 12 = 2*2*3
        (13, [13]),           # Prime number
        (1, []),              # 1 has no prime factors
        (100, [2, 2, 5, 5])   # 100 = 2*2*5*5
    ]
    
    for n, expected in test_cases:
        result = prime_factorization(n)
        print(f"Prime Factors of {n}: {result}, Expected: {expected}")
        assert sorted(result) == sorted(expected)
        
    print("All test cases passed!")

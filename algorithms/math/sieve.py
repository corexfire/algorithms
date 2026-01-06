
"""
Sieve of Eratosthenes / Saringan Eratosthenes

English Description:
The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2.
The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime.

Indonesian Description:
Saringan Eratosthenes adalah algoritma kuno untuk menemukan semua bilangan prima hingga batas tertentu.
Ia melakukannya dengan secara iteratif menandai sebagai komposit (yaitu, bukan prima) kelipatan setiap bilangan prima, dimulai dengan bilangan prima pertama, 2.
Kelipatan bilangan prima tertentu dihasilkan sebagai urutan angka yang dimulai dari bilangan prima tersebut, dengan perbedaan konstan di antara mereka yang sama dengan bilangan prima tersebut.

Implementation Details:
- Algorithm Steps / Langkah Algoritma:
  [EN] Create a list of booleans up to n. Iterate from p=2. If p is prime, mark all multiples of p as non-prime.
  [ID] Buat daftar boolean hingga n. Ulangi dari p=2. Jika p adalah prima, tandai semua kelipatan p sebagai bukan prima.
  
- Optimization / Optimasi:
  [EN] We can start marking multiples from `p*p` because smaller multiples would have been already marked by smaller primes.
  [ID] Kita dapat mulai menandai kelipatan dari `p*p` karena kelipatan yang lebih kecil pasti sudah ditandai oleh bilangan prima yang lebih kecil.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n log log n).
  [ID] O(n log log n).
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the boolean array.
  [ID] O(n) untuk menyimpan array boolean.

Usage Documentation:
  [EN] Call `sieve_of_eratosthenes(n)` to get a list of primes up to n.
  [ID] Panggil `sieve_of_eratosthenes(n)` untuk mendapatkan daftar bilangan prima hingga n.
  
  >>> sieve_of_eratosthenes(10)
  [2, 3, 5, 7]
  >>> sieve_of_eratosthenes(1)
  []
"""
from typing import List

def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Mengimplementasikan Sieve of Eratosthenes untuk mencari bilangan prima.
    
    Args:
        n: Batas atas pencarian bilangan prima (inklusif).
        
    Returns:
        List[int]: Daftar bilangan prima hingga n.
    """
    if n < 2:
        return []
        
    # Inisialisasi array boolean (True berarti prima)
    # Index i merepresentasikan bilangan i
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while (p * p <= n):
        # Jika is_prime[p] tidak berubah, maka itu prima
        if is_prime[p]:
            # Update semua kelipatan p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    # Kumpulkan bilangan prima
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

if __name__ == "__main__":
    # Test cases
    print("Running Sieve of Eratosthenes Tests...")
    
    # Test case 1: Primes up to 10 -> 2, 3, 5, 7
    n = 10
    primes = sieve_of_eratosthenes(n)
    print(f"Primes up to {n}: {primes}")
    assert primes == [2, 3, 5, 7], "Test case 1 failed"
    
    # Test case 2: Primes up to 30
    n = 30
    primes = sieve_of_eratosthenes(n)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print(f"Primes up to {n}: {primes}")
    assert primes == expected, "Test case 2 failed"
    
    # Test case 3: n < 2
    assert sieve_of_eratosthenes(1) == [], "Test case n=1 failed"
    
    print("All Sieve of Eratosthenes tests passed!")

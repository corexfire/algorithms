"""
RSA Encryption / Enkripsi RSA

English Description:
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem widely used for secure data transmission. It relies on the computational difficulty of factoring the product of two large prime numbers.

Indonesian Description:
RSA (Rivest–Shamir–Adleman) adalah sistem kriptografi kunci publik yang digunakan secara luas untuk transmisi data yang aman. Ini bergantung pada kesulitan komputasi untuk memfaktorkan hasil kali dua bilangan prima besar.

Implementation Details:
- Key Generation / Pembuatan Kunci:
  [EN] Selects two primes `p` and `q`, computes `n = p*q` and `phi = (p-1)*(q-1)`. Chooses `e` coprime to `phi`, then calculates `d` such that `d*e ≡ 1 (mod phi)`.
  [ID] Memilih dua bilangan prima `p` dan `q`, menghitung `n = p*q` dan `phi = (p-1)*(q-1)`. Memilih `e` yang relatif prima terhadap `phi`, lalu menghitung `d` sedemikian sehingga `d*e ≡ 1 (mod phi)`.

- Encryption and Decryption / Enkripsi dan Dekripsi:
  [EN] Encryption: `c = m^e mod n`. Decryption: `m = c^d mod n`.
  [ID] Enkripsi: `c = m^e mod n`. Dekripsi: `m = c^d mod n`.

- Time Complexity / Kompleksitas Waktu:
  [EN] Key generation: O(log(n)^4). Encryption/Decryption: O(log(n)^3).
  [ID] Pembuatan kunci: O(log(n)^4). Enkripsi/Dekripsi: O(log(n)^3).

- Space Complexity / Kompleksitas Ruang:
  [EN] O(1) auxiliary space (numbers are large but constant count).
  [ID] O(1) ruang tambahan (angka besar tetapi jumlah konstan).

Usage Documentation:
  [EN] Use `generate_keypair(p, q)` to create keys. Note: In this educational implementation, encryption/decryption functions are not provided as standalone but implied by modular exponentiation.
  [ID] Gunakan `generate_keypair(p, q)` untuk membuat kunci. Catatan: Dalam implementasi pendidikan ini, fungsi enkripsi/dekripsi tidak disediakan secara mandiri tetapi tersirat oleh eksponensiasi modular.

  >>> p, q = 61, 53
  >>> public, private = generate_keypair(p, q)
  >>> n = public[1]
  >>> n
  3233
"""
import random
from typing import Tuple, List

# --- Helper Functions ---

def gcd(a: int, b: int) -> int:
    """Calculates the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a: int, m: int) -> int:
    """
    Calculates the modular multiplicative inverse of a under modulo m.
    Returns x such that (a * x) % m == 1.
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def is_prime(n: int) -> bool:
    """
    Simple primality test using trial division.
    For production, use Miller-Rabin or similar.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# --- RSA Functions ---

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Generates RSA keypair based on two prime numbers p and q.
    
    Args:
        p: First prime number
        q: Second prime number
        
    Returns:
        Tuple of ((e, n), (d, n)) where:
        - (e, n) is the public key
        - (d, n) is the private key
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal.")
        
    # n = pq
    n = p * q
    
    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    
    # Use standard common value for e if possible for efficiency, usually 65537
    # But here we just find a random valid one
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        
    # Use Extended Euclid's Algorithm to generate the private key
    d = mod_inverse(e, phi)
    
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

if __name__ == '__main__':
    print("RSA Key Generation Test")
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print(f"Public Key: {public}")
    print(f"Private Key: {private}")
    
    # Simple test with a message (number)
    msg = 42
    print(f"Original message: {msg}")
    
    # Encrypt: c = m^e mod n
    e, n = public
    encrypted_msg = pow(msg, e, n)
    print(f"Encrypted message: {encrypted_msg}")
    
    # Decrypt: m = c^d mod n
    d, n = private
    decrypted_msg = pow(encrypted_msg, d, n)
    print(f"Decrypted message: {decrypted_msg}")
    
    assert msg == decrypted_msg

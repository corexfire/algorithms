"""
Caesar Cipher / Sandi Caesar

English Description:
The Caesar Cipher is a simple substitution cipher that replaces each letter in the plaintext by a letter a fixed number of positions down the alphabet.

Indonesian Description:
Sandi Caesar adalah sandi substitusi sederhana yang menggantikan setiap huruf dalam teks asli dengan huruf sejumlah posisi tetap di bawah alfabet.

Implementation Details:
- Shift Operation / Operasi Geser:
  [EN] Characters are shifted using modular arithmetic: `(x + shift) % 26`. Case is preserved.
  [ID] Karakter digeser menggunakan aritmatika modular: `(x + shift) % 26`. Kapitalisasi dipertahankan.

- Non-alphabetic Characters / Karakter Non-alfabet:
  [EN] Non-alphabetic characters (numbers, punctuation) remain unchanged.
  [ID] Karakter non-alfabet (angka, tanda baca) tetap tidak berubah.

- Time Complexity / Kompleksitas Waktu:
  [EN] O(n) where n is the length of the text.
  [ID] O(n) di mana n adalah panjang teks.

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the result string.
  [ID] O(n) untuk menyimpan string hasil.

Usage Documentation:
  [EN] Use `caesar_cipher_encrypt(text, shift)` to encrypt and `caesar_cipher_decrypt(text, shift)` to decrypt.
  [ID] Gunakan `caesar_cipher_encrypt(text, shift)` untuk mengenkripsi dan `caesar_cipher_decrypt(text, shift)` untuk mendekripsi.

  >>> text = "Hello, World!"
  >>> shift = 3
  >>> encrypted = caesar_cipher_encrypt(text, shift)
  >>> encrypted
  'Khoor, Zruog!'
  >>> caesar_cipher_decrypt(encrypted, shift)
  'Hello, World!'
"""

def caesar_cipher_encrypt(text: str, shift: int) -> str:
    """
    Mengenkripsi teks menggunakan Caesar Cipher.
    
    Args:
        text: Teks yang akan dienkripsi.
        shift: Jumlah pergeseran (kunci).
        
    Returns:
        str: Teks terenkripsi.
    """
    result = ""
    
    # Normalisasi shift agar berada dalam range 0-25
    shift = shift % 26
    
    for char in text:
        if char.isupper():
            # A = 65
            # (char_code - 65 + shift) % 26 + 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            # a = 97
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Karakter non-alfabet tidak diubah
            result += char
            
    return result

def caesar_cipher_decrypt(text: str, shift: int) -> str:
    """
    Mendekripsi teks Caesar Cipher.
    Sama dengan enkripsi tapi dengan shift negatif.
    """
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    # Test cases
    print("Running Caesar Cipher Tests...")
    
    # Test case 1: Enkripsi dasar
    text = "Hello, World!"
    shift = 3
    # H -> K, e -> h, l -> o, o -> r
    expected_cipher = "Khoor, Zruog!"
    
    encrypted = caesar_cipher_encrypt(text, shift)
    print(f"Original: {text}, Encrypted: {encrypted}")
    assert encrypted == expected_cipher, "Encryption failed"
    
    # Test case 2: Dekripsi
    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")
    assert decrypted == text, "Decryption failed"
    
    # Test case 3: Shift besar
    shift_large = 29 # Sama dengan shift 3
    assert caesar_cipher_encrypt(text, shift_large) == expected_cipher, "Large shift failed"
    
    # Test case 4: Wrap around (Z -> A)
    text_wrap = "XYZ"
    shift_wrap = 1
    assert caesar_cipher_encrypt(text_wrap, shift_wrap) == "YZA", "Wrap around failed"
    
    print("All Caesar Cipher tests passed!")

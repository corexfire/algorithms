from typing import List

def get_z_array(s: str) -> List[int]:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    Computes the Z-array for a given string `s`. The Z-array is an array of the same length as the string, where
    the `i-th` element `Z[i]` represents the length of the longest substring starting from `s[i]` that is also a
    prefix of `s`. This fundamental component is used in the Z-algorithm for efficient pattern matching.

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Menghitung array-Z untuk string `s` yang diberikan. Array-Z adalah array dengan panjang yang sama dengan string,
    di mana elemen ke-`i` `Z[i]` mewakili panjang substring terpanjang yang dimulai dari `s[i]` yang juga merupakan
    awalan (prefix) dari `s`. Komponen fundamental ini digunakan dalam algoritma Z untuk pencocokan pola yang efisien.

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Z-Box**: The algorithm maintains a window `[l, r]` (called a Z-box) which is the interval with the largest
        right end `r` such that `s[l...r]` is a prefix of `s`.
    2.  **Case 1 (i > r)**: If the current index `i` is outside the current Z-box, we simply calculate `Z[i]`
        naively and update the Z-box if a match is found.
    3.  **Case 2 (i <= r)**: If `i` is inside the current Z-box, we can use the previously computed values.
        Let `k = i - l`. If `Z[k] < r - i + 1`, then `Z[i] = Z[k]`. Otherwise, we need to extend the search
        starting from `r + 1` and update the Z-box.

    Time Complexity: O(N) where N is the length of the string.
    Space Complexity: O(N) for the Z-array.

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        s (str): Input string.

    Returns:
        List[int]: List of integers representing the Z-array.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> get_z_array("AAAAAA")
    [0, 5, 4, 3, 2, 1]
    >>> get_z_array("AAABAA")
    [0, 2, 1, 0, 2, 1]
    >>> get_z_array("abacaba")
    [0, 0, 1, 0, 3, 0, 1]
    """
    n = len(s)
    z = [0] * n
    
    # [l, r] is the Z-box
    l, r = 0, 0
    
    for i in range(1, n):
        if i > r:
            # Outside the current Z-box
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # Inside the current Z-box
            k = i - l
            if z[k] < r - i + 1:
                # Value is known from previous computation
                z[i] = z[k]
            else:
                # Need to extend the search
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

def search_pattern(text: str, pattern: str) -> List[int]:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    Searches for all occurrences of a pattern in a text using the Z-algorithm. It works by constructing a new
    string `P + "$" + T` (where `$` is a special character not present in P or T) and computing the Z-array for
    this concatenated string. Matches are found where the Z-value equals the length of the pattern.

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Mencari semua kemunculan pola dalam teks menggunakan algoritma Z. Ini bekerja dengan membangun string baru
    `P + "$" + T` (di mana `$` adalah karakter khusus yang tidak ada dalam P atau T) dan menghitung array-Z untuk
    string gabungan ini. Kecocokan ditemukan di mana nilai Z sama dengan panjang pola.

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Concatenation**: Create `concat = pattern + "$" + text`.
    2.  **Z-Array Computation**: Compute the Z-array for `concat`.
    3.  **Scan**: Iterate through the Z-array starting from index `len(pattern) + 1`. If `Z[i]` equals the
        length of the pattern, it means the pattern matches the text starting at the corresponding position.

    Time Complexity: O(N + M) where N is the length of the text and M is the length of the pattern.
    Space Complexity: O(N + M) for the concatenated string and Z-array.

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.

    Returns:
        List[int]: List of starting indices (0-based) where pattern is found in text.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> search_pattern("AABAACAADAABAABA", "AABA")
    [0, 9, 12]
    >>> search_pattern("AAAAA", "AA")
    [0, 1, 2, 3]
    >>> search_pattern("ABCDE", "FG")
    []
    """
    if not pattern or not text:
        return []
        
    # Create concatenated string with a special separator
    # The separator must not be present in text or pattern
    concat = pattern + "$" + text
    z = get_z_array(concat)
    
    matches = []
    p_len = len(pattern)
    
    # Check Z values after the "$" character
    # The concatenated string has length p_len + 1 + t_len
    # We check from index p_len + 1 to end
    for i in range(p_len + 1, len(concat)):
        if z[i] == p_len:
            # The match in text starts at i - (p_len + 1)
            matches.append(i - (p_len + 1))
            
    return matches

if __name__ == "__main__":
    print("Z-Algorithm Tests...")
    
    test_cases = [
        ("AABAACAADAABAABA", "AABA", [0, 9, 12]),
        ("AAAAA", "AA", [0, 1, 2, 3]),
        ("ABCDE", "FG", []),
        ("ABCDE", "ABCDE", [0]),
        ("THIS IS A TEST TEXT", "TEST", [10]),
        ("ABABABAB", "ABA", [0, 2, 4])
    ]
    
    for text, pattern, expected in test_cases:
        result = search_pattern(text, pattern)
        print(f"Text: '{text}', Pattern: '{pattern}' -> Found at: {result}, Expected: {expected}")
        assert result == expected
    
    print("All Z-Algorithm tests passed!")

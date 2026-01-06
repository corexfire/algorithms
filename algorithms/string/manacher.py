def manacher(s: str) -> str:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    Manacher's algorithm is an efficient method for finding the longest palindromic substring in a string. It runs in
    linear time, O(N), which is a significant improvement over the naive O(N^3) or even the dynamic programming
    approach of O(N^2). It works by transforming the input string to handle even-length palindromes uniformly and
    exploiting the symmetry of palindromes to avoid unnecessary comparisons.

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Algoritma Manacher adalah metode efisien untuk menemukan substring palindrom terpanjang dalam sebuah string.
    Algoritma ini berjalan dalam waktu linier, O(N), yang merupakan peningkatan signifikan dibandingkan pendekatan
    naif O(N^3) atau bahkan pendekatan pemrograman dinamis O(N^2). Algoritma ini bekerja dengan mengubah string
    input untuk menangani palindrom panjang genap secara seragam dan memanfaatkan simetri palindrom untuk menghindari
    perbandingan yang tidak perlu.

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Transformation**: The string `S` is transformed into `T` by inserting a special character (e.g., `#`)
        between characters and adding sentinels at both ends (e.g., `^` and `$`) to handle boundaries easily.
        For example, `aba` becomes `^#a#b#a#$`.
    2.  **P Array**: An array `P` is maintained where `P[i]` represents the radius of the palindrome centered at
        index `i` in `T`. The length of the palindrome in `T` is `2 * P[i] + 1`, and the length in the original
        string `S` is equal to `P[i]`.
    3.  **Center and Right Boundary**: Variables `C` (center) and `R` (right boundary) track the rightmost
        palindrome found so far.
    4.  **Expansion**: For each index `i`, we use the mirror index `i_mirror = 2*C - i`. If `i` is within `R`,
        `P[i]` is initialized to `min(R - i, P[i_mirror])`. Then, we attempt to expand the palindrome centered at `i`.
    5.  **Update C and R**: If the palindrome at `i` extends beyond `R`, we update `C` and `R`.

    Time Complexity: O(N) where N is the length of the string.
    Space Complexity: O(N) for the transformed string and P array.

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        s (str): Input string.

    Returns:
        str: The longest palindromic substring found in `s`.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> manacher("babad") in ["bab", "aba"]
    True
    >>> manacher("cbbd")
    'bb'
    >>> manacher("racecar")
    'racecar'
    >>> manacher("a")
    'a'
    >>> manacher("")
    ''
    """
    if not s:
        return ""
        
    # Transform S into T
    # e.g., "aba" -> "^#a#b#a#$"
    # ^ and $ are sentinels to avoid boundary checks
    T = '#'.join(f"^{s}$")
    n = len(T)
    P = [0] * n
    C = 0 # Center of the rightmost palindrome found so far
    R = 0 # Right boundary of that palindrome
    
    for i in range(1, n - 1):
        # i' is the mirror of i around C
        i_mirror = 2 * C - i
        
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0
            
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
            
        # If palindrome centered at i expands past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
    # Find the maximum element in P.
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
            
    # Extract the palindrome from the original string
    # The starting position in original string:
    start = (center_index - 1 - max_len) // 2
    return s[start : start + max_len]

if __name__ == "__main__":
    print("Manacher's Algorithm Tests...")
    
    test_cases = [
        ("babad", ["bab", "aba"]), # Both are valid
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]), # "a" or "c"
        ("racecar", ["racecar"]),
        ("", [""]),
        ("bananas", ["anana"])
    ]
    
    for s, expected_list in test_cases:
        result = manacher(s)
        print(f"Input: '{s}', Result: '{result}'")
        if s == "":
            assert result == ""
        else:
            assert result in expected_list or len(result) == len(expected_list[0])
            # Check if result is actually a palindrome and present in s
            assert result == result[::-1]
            assert result in s
            
    print("All Manacher's Algorithm tests passed!")

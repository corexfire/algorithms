from typing import List

def build_suffix_array(s: str) -> List[int]:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    A Suffix Array is a sorted array of all suffixes of a string. It is a fundamental data structure in string
    processing used for pattern matching, finding longest repeated substrings, and more.
    This implementation uses a simple sorting approach, which is easy to understand but not the most efficient for
    very large strings compared to advanced algorithms like SA-IS or skew algorithm.

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Suffix Array adalah array terurut dari semua sufiks sebuah string. Ini adalah struktur data fundamental dalam
    pemrosesan string yang digunakan untuk pencocokan pola, menemukan substring berulang terpanjang, dan lainnya.
    Implementasi ini menggunakan pendekatan pengurutan sederhana, yang mudah dipahami tetapi bukan yang paling efisien
    untuk string yang sangat besar dibandingkan dengan algoritma tingkat lanjut seperti SA-IS atau algoritma skew.

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Suffix Generation**: Implicitly considers all suffixes `s[i:]` for `i` from 0 to `n-1`.
    2.  **Sorting**: Sorts the indices based on the lexicographical order of the corresponding suffixes.
    
    Time Complexity: O(N^2 log N) generally for naive sort due to string comparisons (Python's slice comparison takes O(N)).
    Space Complexity: O(N) to store the suffix array.

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        s (str): The input string.

    Returns:
        List[int]: A list of integers representing the starting indices of the sorted suffixes.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> build_suffix_array("banana")
    [5, 3, 1, 0, 4, 2]
    >>> build_suffix_array("aba")
    [2, 0, 1]
    """
    return sorted(range(len(s)), key=lambda i: s[i:])

def build_lcp(s: str, sa: List[int]) -> List[int]:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    Constructs the Longest Common Prefix (LCP) array using Kasai's algorithm. The LCP array stores the length of
    the longest common prefix between consecutive suffixes in the sorted suffix array.
    LCP[i] stores the length of the longest common prefix between suffix SA[i] and suffix SA[i+1].

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Membangun array Longest Common Prefix (LCP) menggunakan algoritma Kasai. Array LCP menyimpan panjang
    awalan umum terpanjang antara sufiks yang berurutan dalam suffix array yang diurutkan.
    LCP[i] menyimpan panjang awalan umum terpanjang antara sufiks SA[i] dan sufiks SA[i+1].

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Rank Array**: Computes the inverse of the Suffix Array to get the rank of each suffix.
    2.  **Kasai's Algorithm**: Iterates through the suffixes in original order and efficiently computes LCP values.
        It uses the property that `LCP[rank[i]] >= LCP[rank[i-1]] - 1` to achieve linear time complexity.

    Time Complexity: O(N)
    Space Complexity: O(N) for rank and LCP arrays.

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        s (str): The input string.
        sa (List[int]): The suffix array of the input string.

    Returns:
        List[int]: The LCP array.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> s = "banana"
    >>> sa = [5, 3, 1, 0, 4, 2]
    >>> build_lcp(s, sa) # matches [1, 3, 0, 0, 2, 0] roughly depending on exact definition of last element
    [1, 3, 0, 0, 2, 0]
    """
    n = len(s)
    rank = [0] * n
    for i, si in enumerate(sa):
        rank[si] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return lcp

if __name__ == "__main__":
    s = "banana"
    sa = build_suffix_array(s)
    lcp = build_lcp(s, sa)
    print(f"SA: {sa}")
    print(f"LCP: {lcp}")
    assert sa == [5, 3, 1, 0, 4, 2]
    assert lcp[:6] == [1, 3, 0, 0, 2, 0]
    print("All Suffix Array tests passed!")

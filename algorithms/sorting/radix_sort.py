"""
Description:
    [EN] Radix Sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value. It processes the digits from the least significant digit (LSD) to the most significant digit (MSD).
    [ID] Radix Sort adalah algoritma pengurutan integer non-komparatif yang mengurutkan data dengan kunci integer dengan mengelompokkan kunci berdasarkan digit individu yang berbagi posisi dan nilai signifikan yang sama. Algoritma ini memproses digit dari digit paling tidak signifikan (LSD) ke digit paling signifikan (MSD).

Implementation Details:
    [EN]
    - Find the maximum number to determine the number of digits.
    - Perform Counting Sort for each digit position (unit, ten, hundred, etc.).
    - The `exp` variable (1, 10, 100...) represents the current digit position.
    - Counting Sort must be stable to maintain the relative order of elements with the same digit value.
    - Time Complexity: O(d * (n + b)), where d is the number of digits, n is the number of elements, and b is the base (usually 10).
    - Space Complexity: O(n + b).
    [ID]
    - Temukan bilangan maksimum untuk menentukan jumlah digit.
    - Lakukan Counting Sort untuk setiap posisi digit (satuan, puluhan, ratusan, dst.).
    - Variabel `exp` (1, 10, 100...) mewakili posisi digit saat ini.
    - Counting Sort harus stabil untuk menjaga urutan relatif elemen dengan nilai digit yang sama.
    - Kompleksitas Waktu: O(d * (n + b)), di mana d adalah jumlah digit, n adalah jumlah elemen, dan b adalah basis (biasanya 10).
    - Kompleksitas Ruang: O(n + b).

Usage Documentation:
    [EN]
    - Input: List of non-negative integers.
    - Function: `radix_sort(arr)` sorts the list in-place and returns it.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar integer non-negatif.
    - Fungsi: `radix_sort(arr)` mengurutkan daftar di tempat (in-place) dan mengembalikannya.
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
    [2, 24, 45, 66, 75, 80, 90, 170, 802]
    >>> radix_sort([1, 20, 3, 400, 5])
    [1, 3, 5, 20, 400]
"""

from typing import List

def counting_sort_for_radix(arr: List[int], exp: int) -> None:
    """
    A function to do counting sort of arr[] according to
    the digit represented by exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1
        
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of non-negative integers using Radix Sort.
    
    Args:
        arr: List of non-negative integers
        
    Returns:
        Sorted list
    """
    if not arr:
        return arr
        
    # Find the maximum number to know number of digits
    max1 = max(arr)
    
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
        
    return arr

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [170, 45, 75, 90, 802, 24, 2, 66],
        [1, 20, 3, 400, 5],
        [10, 9, 8, 7, 6, 5],
        [],
        [0]
    ]
    
    for i, test in enumerate(test_cases):
        original = test.copy()
        sorted_arr = radix_sort(test)
        print(f"Test Case {i+1}: Original={original}, Sorted={sorted_arr}")
        assert sorted_arr == sorted(original)
    
    print("All test cases passed!")

"""
Description:
    [EN] Counting Sort is an integer sorting algorithm that operates by counting the number of objects that have each distinct key value. It is efficient when the range of input values is not significantly greater than the number of objects to be sorted.
    [ID] Counting Sort adalah algoritma pengurutan integer yang bekerja dengan menghitung jumlah objek yang memiliki nilai kunci unik masing-masing. Algoritma ini efisien ketika rentang nilai input tidak jauh lebih besar daripada jumlah objek yang akan diurutkan.

Implementation Details:
    [EN]
    - Find the maximum value in the input array to determine the range.
    - Create a count array to store the frequency of each element.
    - Modify the count array to store cumulative counts, which indicate the position of each element in the output.
    - Build the output array by placing elements in their correct sorted positions, iterating in reverse to maintain stability.
    - Time Complexity: O(n + k), where n is the number of elements and k is the range of input.
    - Space Complexity: O(n + k).
    [ID]
    - Temukan nilai maksimum dalam array input untuk menentukan rentang.
    - Buat array hitungan (count array) untuk menyimpan frekuensi setiap elemen.
    - Modifikasi array hitungan untuk menyimpan hitungan kumulatif, yang menunjukkan posisi setiap elemen dalam output.
    - Bangun array output dengan menempatkan elemen pada posisi terurut yang benar, iterasi secara terbalik untuk menjaga stabilitas.
    - Kompleksitas Waktu: O(n + k), di mana n adalah jumlah elemen dan k adalah rentang input.
    - Kompleksitas Ruang: O(n + k).

Usage Documentation:
    [EN]
    - Input: List of non-negative integers.
    - Function: `counting_sort(arr)` returns a new sorted list.
    - Raises `ValueError` if the list contains negative integers.
    [ID]
    - Input: Daftar integer non-negatif.
    - Fungsi: `counting_sort(arr)` mengembalikan daftar baru yang sudah diurutkan.
    - Menimbulkan `ValueError` jika daftar berisi integer negatif.

Examples:
    >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
    [1, 2, 2, 3, 3, 4, 8]
    >>> counting_sort([1, 4, 1, 2, 7, 5, 2])
    [1, 1, 2, 2, 4, 5, 7]
"""

from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of non-negative integers using Counting Sort.
    
    Args:
        arr: List of non-negative integers
        
    Returns:
        Sorted list of integers
    """
    if not arr:
        return []
    
    # Find the maximum element in the array to determine range
    max_val = max(arr)
    min_val = min(arr)
    
    if min_val < 0:
        raise ValueError("Counting Sort (basic implementation) only supports non-negative integers.")
    
    # Initialize count array
    # count[i] stores the number of occurrences of value i
    count = [0] * (max_val + 1)
    
    # Store the count of each element
    for num in arr:
        count[num] += 1
        
    # Modify the count array such that each element at each index 
    # stores the sum of previous counts. 
    # count[i] now contains the position of this character in the output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Build the output array
    output = [0] * len(arr)
    
    # Traverse input array in reverse order to maintain stability
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        
    return output

if __name__ == "__main__":
    print("Counting Sort Tests...")
    
    test_cases = [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([1, 4, 1, 2, 7, 5, 2], [1, 1, 2, 2, 4, 5, 7]),
        ([], []),
        ([5], [5]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3])
    ]
    
    for arr, expected in test_cases:
        result = counting_sort(arr)
        print(f"Original: {arr}, Sorted: {result}")
        assert result == expected
    
    print("All Counting Sort tests passed!")

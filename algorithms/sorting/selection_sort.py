"""
Description:
    [EN] Selection Sort is a simple comparison-based sorting algorithm. It divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list.
    [ID] Selection Sort adalah algoritma pengurutan berbasis perbandingan yang sederhana. Algoritma ini membagi daftar input menjadi dua bagian: sub-daftar item yang sudah diurutkan, yang dibangun dari kiri ke kanan di bagian depan (kiri) daftar, dan sub-daftar item yang tersisa untuk diurutkan yang menempati sisa daftar.

Implementation Details:
    [EN]
    - Iterate through the list from the first element to the second-to-last element.
    - For each position `i`, find the minimum element in the unsorted sublist `arr[i:]`.
    - Swap the found minimum element with the element at position `i`.
    - Repeat until the entire list is sorted.
    - Time Complexity: O(n^2) for all cases (best, average, worst) because of the two nested loops.
    - Space Complexity: O(1) auxiliary space (in-place sort).
    [ID]
    - Iterasi melalui daftar dari elemen pertama hingga elemen kedua dari terakhir.
    - Untuk setiap posisi `i`, temukan elemen minimum dalam sub-daftar yang belum diurutkan `arr[i:]`.
    - Tukar elemen minimum yang ditemukan dengan elemen pada posisi `i`.
    - Ulangi sampai seluruh daftar terurut.
    - Kompleksitas Waktu: O(n^2) untuk semua kasus (terbaik, rata-rata, terburuk) karena dua loop bersarang.
    - Kompleksitas Ruang: O(1) ruang tambahan (pengurutan di tempat).

Usage Documentation:
    [EN]
    - Input: A list of comparable elements.
    - Function: `selection_sort(arr)` sorts the list in-place.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar elemen yang dapat dibandingkan.
    - Fungsi: `selection_sort(arr)` mengurutkan daftar di tempat (in-place).
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
"""

from typing import List, TypeVar

T = TypeVar('T')

def selection_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list using the selection sort algorithm.
    
    Args:
        arr: The list to be sorted
        
    Returns:
        The sorted list
    """
    if not arr:
        return arr
        
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [],
        [1]
    ]
    
    for i, test in enumerate(test_cases):
        original = test.copy()
        sorted_arr = selection_sort(test)
        print(f"Test Case {i+1}: Original={original}, Sorted={sorted_arr}")
        assert sorted_arr == sorted(original)
    
    print("All test cases passed!")

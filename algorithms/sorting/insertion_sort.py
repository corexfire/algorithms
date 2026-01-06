"""
Description:
    [EN] Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is similar to how you might sort playing cards in your hands. It is efficient for small data sets or nearly sorted lists.
    [ID] Insertion Sort adalah algoritma pengurutan sederhana yang membangun array terurut akhir satu per satu item. Ini mirip dengan cara Anda mengurutkan kartu remi di tangan Anda. Algoritma ini efisien untuk kumpulan data kecil atau daftar yang hampir terurut.

Implementation Details:
    [EN]
    - Iterate from the second element (index 1) to the last element.
    - Store the current element in a variable `key`.
    - Compare `key` with the elements in the sorted sub-list (to its left).
    - Shift all elements greater than `key` one position to the right.
    - Insert `key` into its correct position.
    - Time Complexity: O(n^2) worst/average case, O(n) best case (already sorted).
    - Space Complexity: O(1) auxiliary space.
    [ID]
    - Iterasi dari elemen kedua (indeks 1) hingga elemen terakhir.
    - Simpan elemen saat ini dalam variabel `key`.
    - Bandingkan `key` dengan elemen-elemen dalam sub-daftar yang sudah terurut (di sebelah kirinya).
    - Geser semua elemen yang lebih besar dari `key` satu posisi ke kanan.
    - Masukkan `key` ke posisi yang benar.
    - Kompleksitas Waktu: O(n^2) kasus terburuk/rata-rata, O(n) kasus terbaik (sudah terurut).
    - Kompleksitas Ruang: O(1) ruang tambahan.

Usage Documentation:
    [EN]
    - Input: A list of comparable elements.
    - Function: `insertion_sort(arr)` sorts the list in-place.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar elemen yang dapat dibandingkan.
    - Fungsi: `insertion_sort(arr)` mengurutkan daftar di tempat (in-place).
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> insertion_sort([12, 11, 13, 5, 6])
    [5, 6, 11, 12, 13]
    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
"""

from typing import List, TypeVar

T = TypeVar('T')

def insertion_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list using the insertion sort algorithm.
    
    Args:
        arr: The list to be sorted
        
    Returns:
        The sorted list
    """
    if not arr:
        return arr
        
    # We modify the list in-place
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
            
    return arr

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [],
        [1]
    ]
    
    for i, test in enumerate(test_cases):
        original = test.copy()
        sorted_arr = insertion_sort(test)
        print(f"Test Case {i+1}: Original={original}, Sorted={sorted_arr}")
        assert sorted_arr == sorted(original)
    
    print("All test cases passed!")

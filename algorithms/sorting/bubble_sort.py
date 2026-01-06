"""
Description:
    [EN] Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
    [ID] Bubble Sort adalah algoritma pengurutan sederhana yang berulang kali melewati daftar, membandingkan elemen yang berdekatan, dan menukarnya jika urutannya salah. Proses ini diulang sampai daftar terurut.

Implementation Details:
    [EN]
    - Iterate through the list multiple times.
    - In each pass, compare adjacent elements (`arr[j]` and `arr[j+1]`).
    - If `arr[j] > arr[j+1]`, swap them.
    - After each pass, the largest element "bubbles up" to its correct position at the end.
    - Optimization: A `swapped` flag tracks if any swap happened. If no swaps occur in a pass, the list is already sorted, and we can terminate early.
    - Time Complexity: O(n^2) in worst/average case, O(n) in best case (already sorted).
    - Space Complexity: O(1) auxiliary space (in-place sort).
    [ID]
    - Iterasi melalui daftar beberapa kali.
    - Dalam setiap pass, bandingkan elemen yang berdekatan (`arr[j]` dan `arr[j+1]`).
    - Jika `arr[j] > arr[j+1]`, tukar mereka.
    - Setelah setiap pass, elemen terbesar "menggelembung" ke posisi yang benar di akhir.
    - Optimasi: Flag `swapped` melacak jika ada pertukaran. Jika tidak ada pertukaran dalam satu pass, daftar sudah terurut, dan kita bisa berhenti lebih awal.
    - Kompleksitas Waktu: O(n^2) pada kasus terburuk/rata-rata, O(n) pada kasus terbaik (sudah terurut).
    - Kompleksitas Ruang: O(1) ruang tambahan (pengurutan di tempat).

Usage Documentation:
    [EN]
    - Input: A list of comparable elements (e.g., integers, strings).
    - Function: `bubble_sort(arr)` sorts the list in-place.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar elemen yang dapat dibandingkan (misalnya, integer, string).
    - Fungsi: `bubble_sort(arr)` mengurutkan daftar di tempat (in-place).
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> bubble_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
"""

from typing import List, TypeVar, Protocol

# Mendefinisikan tipe generik untuk elemen yang bisa dibandingkan
class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)

def bubble_sort(arr: List[T]) -> List[T]:
    """
    Implementasi Bubble Sort.
    Melakukan iterasi dan menukar elemen yang tidak urut.
    Optimasi: Berhenti jika dalam satu pass tidak ada pertukaran (list sudah urut).
    
    Args:
        arr: List yang akan diurutkan.
        
    Returns:
        List[T]: List yang sudah diurutkan (in-place modification).
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Jika tidak ada pertukaran pada inner loop, berarti array sudah terurut
        if not swapped:
            break
            
    return arr

if __name__ == "__main__":
    # Test cases
    print("Running Bubble Sort Tests...")
    
    # Test case 1: List acak
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    bubble_sort(data)
    print(f"Sorted:   {data}")
    assert data == [11, 12, 22, 25, 34, 64, 90], "Test case 1 failed"
    
    # Test case 2: List sudah terurut (Best case O(n))
    sorted_data = [1, 2, 3, 4, 5]
    bubble_sort(sorted_data)
    print(f"Sorted already: {sorted_data}")
    assert sorted_data == [1, 2, 3, 4, 5], "Test case 2 failed"
    
    # Test case 3: List terurut terbalik (Worst case O(n^2))
    reverse_data = [5, 4, 3, 2, 1]
    bubble_sort(reverse_data)
    print(f"Reverse sorted: {reverse_data}")
    assert reverse_data == [1, 2, 3, 4, 5], "Test case 3 failed"
    
    print("All Bubble Sort tests passed!")

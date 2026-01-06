"""
Quick Sort Algorithm
--------------------

1. English Description
----------------------
Quick Sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays.
A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot,
based on which the partition is made and another array holds values greater than the pivot value.

Time Complexity: Average O(n log n), Worst Case O(n^2) (rare with good pivot choice).
Space Complexity: O(log n) due to recursion stack.

2. Indonesian Description
-------------------------
Quick Sort adalah algoritma pengurutan yang sangat efisien dan didasarkan pada pemartisian array data menjadi array yang lebih kecil.
Array besar dipartisi menjadi dua array, salah satunya menampung nilai yang lebih kecil dari nilai yang ditentukan, katakanlah pivot,
berdasarkan mana partisi dibuat dan array lain menampung nilai yang lebih besar dari nilai pivot.

Kompleksitas Waktu: Rata-rata O(n log n), Kasus Terburuk O(n^2) (jarang dengan pilihan pivot yang baik).
Kompleksitas Ruang: O(log n) karena tumpukan rekursi.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Partitioning / Pemartisian**:
  - [EN] This implementation uses the last element as the pivot (Lomuto partition scheme).
  - [ID] Implementasi ini menggunakan elemen terakhir sebagai pivot (skema partisi Lomuto).
  - [EN] Elements smaller than pivot are moved to the left, larger to the right.
  - [ID] Elemen yang lebih kecil dari pivot dipindahkan ke kiri, yang lebih besar ke kanan.
- **Recursion / Rekursi**:
  - [EN] Recursively sorts the sub-arrays to the left and right of the pivot.
  - [ID] Secara rekursif mengurutkan sub-array di kiri dan kanan pivot.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Function / Fungsi**:
  - [EN] `quick_sort(arr)` sorts the list in-place and returns it.
  - [ID] `quick_sort(arr)` mengurutkan list di tempat (in-place) dan mengembalikannya.
"""

from typing import List, TypeVar, Protocol

# Mendefinisikan tipe generik untuk elemen yang bisa dibandingkan
class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...
    def __le__(self, other: 'Comparable') -> bool: ...
    def __ge__(self, other: 'Comparable') -> bool: ...
    def __eq__(self, other: 'object') -> bool: ...

T = TypeVar('T', bound=Comparable)

def quick_sort(arr: List[T]) -> List[T]:
    """
    Fungsi utama untuk Quick Sort.
    Memanggil fungsi rekursif _quick_sort_recursive.
    
    Args:
        arr: List yang akan diurutkan.
        
    Returns:
        List[T]: List yang sudah diurutkan (in-place modification).
    """
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_recursive(arr: List[T], low: int, high: int) -> None:
    """
    Fungsi rekursif helper untuk Quick Sort.
    """
    if low < high:
        # Partition index
        pi = _partition(arr, low, high)
        
        # Rekursif untuk sisi kiri dan kanan pivot
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)

def _partition(arr: List[T], low: int, high: int) -> int:
    """
    Fungsi untuk memilih pivot dan menempatkan elemen lebih kecil di kiri,
    dan elemen lebih besar di kanan pivot.
    Menggunakan elemen terakhir sebagai pivot.
    """
    pivot = arr[high]
    i = low - 1  # Index elemen yang lebih kecil
    
    for j in range(low, high):
        # Jika elemen saat ini lebih kecil atau sama dengan pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Tukar pivot ke posisi yang benar
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    # Test cases
    print("Running Quick Sort Tests...")
    
    # Test case 1: List acak
    data = [10, 7, 8, 9, 1, 5]
    print(f"Original: {data}")
    quick_sort(data)
    print(f"Sorted:   {data}")
    assert data == [1, 5, 7, 8, 9, 10], "Test case 1 failed"
    
    # Test case 2: List sudah terurut
    sorted_data = [1, 2, 3, 4, 5]
    quick_sort(sorted_data)
    print(f"Sorted already: {sorted_data}")
    assert sorted_data == [1, 2, 3, 4, 5], "Test case 2 failed"
    
    # Test case 3: List terurut terbalik
    reverse_data = [5, 4, 3, 2, 1]
    quick_sort(reverse_data)
    print(f"Reverse sorted: {reverse_data}")
    assert reverse_data == [1, 2, 3, 4, 5], "Test case 3 failed"
    
    # Test case 4: List dengan duplikat
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    quick_sort(duplicate_data)
    print(f"Duplicates: {duplicate_data}")
    expected = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    assert duplicate_data == expected, "Test case 4 failed"
    
    print("All Quick Sort tests passed!")

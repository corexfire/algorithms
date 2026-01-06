"""
Merge Sort Algorithm
--------------------

1. English Description
----------------------
Merge Sort is an efficient, general-purpose, comparison-based sorting algorithm.
Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.
Merge sort is a divide and conquer algorithm.

Time Complexity: O(n log n) for Best, Average, and Worst cases.
Space Complexity: O(n) auxiliary space.

2. Indonesian Description
-------------------------
Merge Sort adalah algoritma pengurutan berbasis perbandingan yang efisien dan bertujuan umum.
Sebagian besar implementasi menghasilkan pengurutan yang stabil, yang berarti urutan elemen yang sama adalah sama dalam input dan output.
Merge sort adalah algoritma divide and conquer (bagi dan taklukkan).

Kompleksitas Waktu: O(n log n) untuk kasus Terbaik, Rata-rata, dan Terburuk.
Kompleksitas Ruang: O(n) ruang tambahan.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Divide / Bagi**:
  - [EN] Divide the unsorted list into `n` sublists, each containing one element (a list of one element is considered sorted).
  - [ID] Bagi daftar yang tidak diurutkan menjadi `n` sub-daftar, masing-masing berisi satu elemen (daftar satu elemen dianggap diurutkan).
- **Conquer (Merge) / Taklukkan (Gabung)**:
  - [EN] Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.
  - [ID] Menggabungkan sub-daftar secara berulang untuk menghasilkan sub-daftar baru yang diurutkan hingga hanya tersisa satu sub-daftar.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Function / Fungsi**:
  - [EN] `merge_sort(arr)`: Returns a new sorted list containing elements from `arr`.
  - [ID] `merge_sort(arr)`: Mengembalikan daftar baru yang diurutkan berisi elemen dari `arr`.
"""

from typing import List, TypeVar, Protocol

class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)

def merge_sort(arr: List[T]) -> List[T]:
    """
    Implementasi Merge Sort.
    Membagi array menjadi dua bagian, mengurutkan masing-masing secara rekursif,
    lalu menggabungkannya kembali.
    
    Args:
        arr: List yang akan diurutkan.
        
    Returns:
        List[T]: List baru yang sudah diurutkan.
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Rekursif call
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return _merge(left_sorted, right_sorted)

def _merge(left: List[T], right: List[T]) -> List[T]:
    """
    Menggabungkan dua list terurut menjadi satu list terurut.
    """
    sorted_list = []
    i = 0 # Pointer untuk left
    j = 0 # Pointer untuk right
    
    # Bandingkan elemen dan masukkan yang lebih kecil ke sorted_list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # type: ignore (Assuming T supports comparison)
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            
    # Masukkan sisa elemen (jika ada)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

if __name__ == "__main__":
    # Test cases
    print("Running Merge Sort Tests...")
    
    # Test case 1: List acak
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {data}")
    sorted_data = merge_sort(data)
    print(f"Sorted:   {sorted_data}")
    assert sorted_data == [3, 9, 10, 27, 38, 43, 82], "Test case 1 failed"
    
    # Test case 2: List kosong
    assert merge_sort([]) == [], "Test case 2 failed"
    
    # Test case 3: List satu elemen
    assert merge_sort([1]) == [1], "Test case 3 failed"
    
    # Test case 4: List terbalik
    reverse_data = [5, 4, 3, 2, 1]
    assert merge_sort(reverse_data) == [1, 2, 3, 4, 5], "Test case 4 failed"
    
    print("All Merge Sort tests passed!")

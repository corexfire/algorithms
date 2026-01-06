"""
Binary Search / Pencarian Biner

English Description:
Binary Search is an efficient algorithm for finding an item from a sorted list of items.
It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
This implementation returns the index of the target if found, otherwise -1.

Indonesian Description:
Pencarian Biner (Binary Search) adalah algoritma yang efisien untuk menemukan item dari daftar item yang diurutkan.
Ia bekerja dengan membagi dua secara berulang bagian dari daftar yang mungkin berisi item tersebut, sampai Anda mempersempit kemungkinan lokasi menjadi hanya satu.
Implementasi ini mengembalikan indeks target jika ditemukan, jika tidak -1.

Implementation Details:
- Divide and Conquer / Bagi dan Taklukkan:
  [EN] Compares target with the middle element. If equal, returns index. If target < mid, search left half. If target > mid, search right half.
  [ID] Membandingkan target dengan elemen tengah. Jika sama, kembalikan indeks. Jika target < tengah, cari di setengah kiri. Jika target > tengah, cari di setengah kanan.
  
- Precondition / Prasyarat:
  [EN] The array must be sorted for binary search to work correctly.
  [ID] Array harus diurutkan agar pencarian biner berfungsi dengan benar.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(log n) - logarithmic time.
  [ID] O(log n) - waktu logaritmik.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(1) for iterative implementation.
  [ID] O(1) untuk implementasi iteratif.

Usage Documentation:
  [EN] Pass a sorted list and the target value.
  [ID] Berikan daftar yang sudah diurutkan dan nilai target.
  
  >>> arr = [1, 2, 3, 4, 5, 6, 7]
  >>> binary_search(arr, 4)
  3
  >>> binary_search(arr, 10)
  -1
"""
from typing import List, Union

Number = Union[int, float]

def binary_search(arr: List[Number], target: Number) -> int:
    """
    Implementasi binary search iteratif.
    
    Args:
        arr: List elemen yang sudah terurut (ascending).
        target: Elemen yang dicari.
        
    Returns:
        int: Index elemen jika ditemukan, -1 jika tidak ditemukan.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Menghindari overflow integer pada bahasa lain, aman di Python tapi good practice
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # Target berada di separuh kanan
            left = mid + 1
        else:
            # Target berada di separuh kiri
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    # Test cases
    print("Running Binary Search Tests...")
    
    # Test case 1: Elemen ada di tengah
    sorted_data = [1, 3, 5, 7, 9, 11, 13]
    target_val = 7
    result = binary_search(sorted_data, target_val)
    print(f"Searching for {target_val} in {sorted_data}: Index {result}")
    assert result == 3, "Test case 1 failed"
    
    # Test case 2: Elemen ada di awal
    target_val = 1
    result = binary_search(sorted_data, target_val)
    print(f"Searching for {target_val} in {sorted_data}: Index {result}")
    assert result == 0, "Test case 2 failed"
    
    # Test case 3: Elemen ada di akhir
    target_val = 13
    result = binary_search(sorted_data, target_val)
    print(f"Searching for {target_val} in {sorted_data}: Index {result}")
    assert result == 6, "Test case 3 failed"
    
    # Test case 4: Elemen tidak ditemukan
    target_val = 6
    result = binary_search(sorted_data, target_val)
    print(f"Searching for {target_val} in {sorted_data}: Index {result}")
    assert result == -1, "Test case 4 failed"
    
    # Test case 5: List kosong
    result = binary_search([], 5)
    print(f"Searching for 5 in []: Index {result}")
    assert result == -1, "Test case 5 failed"
    
    print("All Binary Search tests passed!")

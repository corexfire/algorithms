"""
Description:
    [EN] Linear Search is the simplest searching algorithm that checks every element in the list sequentially until the target element is found or the list ends. It works on both sorted and unsorted lists.
    [ID] Linear Search adalah algoritma pencarian paling sederhana yang memeriksa setiap elemen dalam daftar secara berurutan hingga elemen target ditemukan atau daftar berakhir. Algoritma ini bekerja baik pada daftar yang terurut maupun tidak terurut.

Implementation Details:
    [EN]
    - Iterate through the list from the first element to the last.
    - Compare each element with the target value.
    - If a match is found, return the index.
    - If the end of the list is reached without finding the target, return -1.
    - Time Complexity: O(n) in the worst case (target at the end or not present).
    - Space Complexity: O(1) as it requires no extra space.
    [ID]
    - Iterasi melalui daftar dari elemen pertama hingga terakhir.
    - Bandingkan setiap elemen dengan nilai target.
    - Jika kecocokan ditemukan, kembalikan indeksnya.
    - Jika akhir daftar tercapai tanpa menemukan target, kembalikan -1.
    - Kompleksitas Waktu: O(n) dalam kasus terburuk (target di akhir atau tidak ada).
    - Kompleksitas Ruang: O(1) karena tidak memerlukan ruang tambahan.

Usage Documentation:
    [EN]
    - Input: A list of elements `arr` and a `target` value.
    - Function: `linear_search(arr, target)`.
    - Returns: The index of the target if found, otherwise -1.
    [ID]
    - Input: Sebuah daftar elemen `arr` dan nilai `target`.
    - Fungsi: `linear_search(arr, target)`.
    - Mengembalikan: Indeks target jika ditemukan, jika tidak -1.

Examples:
    >>> linear_search([10, 20, 30, 40], 30)
    2
    >>> linear_search([10, 20, 30, 40], 50)
    -1
"""

from typing import Any, List, Optional

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Implementasi linear search untuk mencari target dalam list.
    
    Args:
        arr: List elemen yang akan dicari.
        target: Elemen yang dicari.
        
    Returns:
        int: Index elemen jika ditemukan, -1 jika tidak ditemukan.
    """
    # Iterasi melalui setiap elemen dalam list
    for i, item in enumerate(arr):
        if item == target:
            return i
            
    # Kembalikan -1 jika elemen tidak ditemukan setelah memeriksa seluruh list
    return -1

if __name__ == "__main__":
    # Test cases
    print("Running Linear Search Tests...")
    
    # Test case 1: Elemen ada di dalam list
    data = [2, 4, 6, 8, 10]
    target_val = 6
    result = linear_search(data, target_val)
    print(f"Searching for {target_val} in {data}: Index {result}")
    assert result == 2, "Test case 1 failed"
    
    # Test case 2: Elemen tidak ada di dalam list
    target_val = 5
    result = linear_search(data, target_val)
    print(f"Searching for {target_val} in {data}: Index {result}")
    assert result == -1, "Test case 2 failed"
    
    # Test case 3: List kosong
    empty_list = []
    result = linear_search(empty_list, 1)
    print(f"Searching for 1 in {empty_list}: Index {result}")
    assert result == -1, "Test case 3 failed"
    
    print("All Linear Search tests passed!")

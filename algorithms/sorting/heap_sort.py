"""
Description:
    [EN] Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap data structure. It divides its input into a sorted and an unsorted region, and iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.
    [ID] Heap Sort adalah algoritma pengurutan berbasis perbandingan yang menggunakan struktur data Binary Heap. Algoritma ini membagi inputnya menjadi wilayah terurut dan tidak terurut, dan secara iteratif menyusutkan wilayah tidak terurut dengan mengambil elemen terbesar dan memindahkannya ke wilayah terurut.

Implementation Details:
    [EN]
    - Build a Max Heap from the input data.
    - At this point, the largest item is stored at the root of the heap.
    - Replace it with the last item of the heap followed by reducing the size of the heap by 1.
    - Finally, heapify the root of the tree.
    - Repeat the above steps while the size of the heap is greater than 1.
    - Time Complexity: O(n log n) for all cases (best, average, worst).
    - Space Complexity: O(1) auxiliary space (in-place sort).
    [ID]
    - Bangun Max Heap dari data input.
    - Pada titik ini, item terbesar disimpan di akar heap.
    - Ganti dengan item terakhir dari heap diikuti dengan mengurangi ukuran heap sebanyak 1.
    - Terakhir, heapify akar pohon.
    - Ulangi langkah di atas selama ukuran heap lebih besar dari 1.
    - Kompleksitas Waktu: O(n log n) untuk semua kasus (terbaik, rata-rata, terburuk).
    - Kompleksitas Ruang: O(1) ruang tambahan (pengurutan di tempat).

Usage Documentation:
    [EN]
    - Input: A list of comparable elements (e.g., integers, floats).
    - Function: `heap_sort(arr)` sorts the list in-place.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar elemen yang dapat dibandingkan (misalnya, integer, float).
    - Fungsi: `heap_sort(arr)` mengurutkan daftar di tempat (in-place).
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> heap_sort([12, 11, 13, 5, 6, 7])
    [5, 6, 7, 11, 12, 13]
    >>> heap_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
"""

from typing import List, Any

def heapify(arr: List[Any], n: int, i: int) -> None:
    """
    Mengubah subtree yang berakar di index i menjadi Max Heap.
    
    Args:
        arr: Array yang akan di-heapify.
        n: Ukuran heap.
        i: Index root dari subtree.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Cek jika anak kiri lebih besar dari root
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    # Cek jika anak kanan lebih besar dari largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    # Jika largest bukan root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swap
        
        # Recursively heapify subtree yang terpengaruh
        heapify(arr, n, largest)

def heap_sort(arr: List[Any]) -> List[Any]:
    """
    Mengurutkan array menggunakan algoritma Heap Sort.
    
    Args:
        arr: Array yang akan diurutkan.
        
    Returns:
        List[Any]: Array yang sudah terurut.
    """
    n = len(arr)
    
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap
        heapify(arr, i, 0)
        
    return arr

if __name__ == "__main__":
    # Test Cases
    print("Running Heap Sort Tests...")
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [3, 0, 2, 5, -1, 4, 1],
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for arr in test_cases:
        expected = sorted(arr.copy())
        # Note: heap_sort modifies array in-place, but we return it for convenience
        result = heap_sort(arr.copy())
        assert result == expected, f"Failed on {arr}, Expected {expected}, Got {result}"
        
    print("All Heap Sort tests passed!")

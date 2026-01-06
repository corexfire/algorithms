"""
Description:
    [EN] Bucket Sort is a sorting algorithm that works by distributing elements into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort algorithm. It is mainly useful when input is uniformly distributed over a range.
    [ID] Bucket Sort adalah algoritma pengurutan yang bekerja dengan mendistribusikan elemen ke dalam sejumlah ember (bucket). Setiap ember kemudian diurutkan secara individual, baik menggunakan algoritma pengurutan yang berbeda atau menerapkan algoritma bucket sort secara rekursif. Ini sangat berguna ketika input terdistribusi secara seragam dalam suatu rentang.

Implementation Details:
    [EN]
    - Create `n` empty buckets.
    - Normalize input values and place them into the appropriate bucket based on the formula: `index = floor((value - min) / range * (n - 1))`.
    - Sort each non-empty bucket (typically using Insertion Sort or built-in sort).
    - Concatenate all sorted buckets to get the final sorted list.
    - Time Complexity: O(n + k) on average (n = number of elements, k = number of buckets), O(n^2) worst case.
    - Space Complexity: O(n + k) to store the buckets.
    [ID]
    - Buat `n` ember kosong.
    - Normalisasi nilai input dan tempatkan ke dalam ember yang sesuai berdasarkan rumus: `index = floor((value - min) / range * (n - 1))`.
    - Urutkan setiap ember yang tidak kosong (biasanya menggunakan Insertion Sort atau built-in sort).
    - Gabungkan semua ember yang sudah terurut untuk mendapatkan daftar akhir.
    - Kompleksitas Waktu: O(n + k) rata-rata (n = jumlah elemen, k = jumlah ember), O(n^2) kasus terburuk.
    - Kompleksitas Ruang: O(n + k) untuk menyimpan ember.

Usage Documentation:
    [EN]
    - Input: A list of numerical values (integers or floats).
    - Function: `bucket_sort(arr)` returns a new sorted list.
    - Returns: The sorted list.
    [ID]
    - Input: Daftar nilai numerik (integer atau float).
    - Fungsi: `bucket_sort(arr)` mengembalikan daftar baru yang sudah diurutkan.
    - Mengembalikan: Daftar yang sudah diurutkan.

Examples:
    >>> bucket_sort([0.897, 0.565, 0.656, 0.1234])
    [0.1234, 0.565, 0.656, 0.897]
    >>> bucket_sort([10, 50, 30, 20])
    [10, 20, 30, 50]
"""

from typing import List

def bucket_sort(arr: List[float]) -> List[float]:
    """
    Sorts a list of numbers using Bucket Sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    # 1. Buat bucket kosong
    # Jumlah bucket biasanya disamakan dengan jumlah elemen
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Cari range data untuk normalisasi jika data tidak dalam range [0, 1)
    max_val = max(arr)
    min_val = min(arr)
    r = max_val - min_val
    
    # Jika semua elemen sama
    if r == 0:
        return arr

    # 2. Masukkan elemen ke dalam bucket
    for num in arr:
        # Normalisasi ke index 0..(n-1)
        # Rumus: floor((num - min_val) / r * (n - 1))
        # Menggunakan n-1 agar max_val masuk ke bucket terakhir, bukan overflow
        idx = int((num - min_val) / r * (n - 1))
        buckets[idx].append(num)

    # 3. Urutkan setiap bucket dan gabungkan
    sorted_arr = []
    for bucket in buckets:
        # Kita gunakan insertion sort atau built-in sort untuk setiap bucket
        # Python's Timsort sangat efisien untuk list kecil
        bucket.sort()
        sorted_arr.extend(bucket)
        
    return sorted_arr

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434],
        [10, 50, 30, 20, 40], # Integer inputs
        [5.5, 2.2, 9.9, 1.1, 7.7], # Float > 1
        [], # Empty
        [1.0], # Single element
        [2.0, 2.0, 2.0] # Duplicates
    ]
    
    for i, arr in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print(f"Input: {arr}")
        sorted_arr = bucket_sort(arr.copy())
        print(f"Output: {sorted_arr}")
        
        # Verifikasi
        assert sorted_arr == sorted(arr), f"Error on test case {i+1}"
        print("Status: PASSED\n")
        
    print("All Bucket Sort tests passed!")

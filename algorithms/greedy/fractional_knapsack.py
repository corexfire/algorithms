"""
Description:
    [EN] The Fractional Knapsack problem involves selecting items with specific weights and values to maximize total value in a knapsack of limited capacity. Unlike the 0/1 Knapsack problem, items can be broken down into smaller fractions. This is a classic greedy algorithm problem.
    [ID] Masalah Fractional Knapsack melibatkan pemilihan item dengan berat dan nilai tertentu untuk memaksimalkan total nilai dalam tas dengan kapasitas terbatas. Berbeda dengan masalah 0/1 Knapsack, item dapat dipecah menjadi bagian yang lebih kecil. Ini adalah masalah algoritma greedy klasik.

Implementation Details:
    [EN]
    - Calculate the value-to-weight ratio for each item.
    - Sort items in descending order based on this ratio.
    - Iterate through the sorted items:
        - If the item fits entirely, take it all.
        - If not, take the fraction that fits to fill the knapsack.
    - Time Complexity: O(N log N) due to sorting.
    - Space Complexity: O(1) auxiliary space (ignoring input storage) or O(N) depending on sort implementation.
    [ID]
    - Hitung rasio nilai-terhadap-berat untuk setiap item.
    - Urutkan item secara menurun (descending) berdasarkan rasio ini.
    - Iterasi melalui item yang sudah diurutkan:
        - Jika item muat sepenuhnya, ambil semuanya.
        - Jika tidak, ambil pecahan yang muat untuk memenuhi tas.
    - Kompleksitas Waktu: O(N log N) karena pengurutan.
    - Kompleksitas Ruang: O(1) ruang tambahan (mengabaikan penyimpanan input) atau O(N) tergantung implementasi sort.

Usage Documentation:
    [EN]
    - Input: List of tuples (weight, value) and the maximum capacity.
    - Call `fractional_knapsack(items, capacity)` to get the maximum total value.
    - Returns a float representing the maximum value.
    [ID]
    - Input: List dari tuple (berat, nilai) dan kapasitas maksimum.
    - Panggil `fractional_knapsack(items, capacity)` untuk mendapatkan total nilai maksimum.
    - Mengembalikan float yang merepresentasikan nilai maksimum.

Examples:
    >>> items = [(10, 60), (20, 100), (30, 120)]
    >>> capacity = 50
    >>> fractional_knapsack(items, capacity)
    240.0
"""

from typing import List, Tuple

# Item direpresentasikan sebagai tuple (weight, value)
Item = Tuple[float, float]

def fractional_knapsack(items: List[Item], capacity: float) -> float:
    """
    Menghitung nilai maksimum yang bisa didapat dengan kapasitas tertentu.
    
    Args:
        items: List of tuples (weight, value).
        capacity: Kapasitas maksimum tas.
        
    Returns:
        float: Nilai total maksimum.
    """
    # Hitung rasio value/weight untuk setiap item dan urutkan menurun (descending)
    # x[1] is value, x[0] is weight
    # Sort key: value / weight
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for weight, value in sorted_items:
        if remaining_capacity <= 0:
            break
            
        if weight <= remaining_capacity:
            # Ambil seluruh item
            total_value += value
            remaining_capacity -= weight
        else:
            # Ambil sebagian item (fractional)
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0 # Tas penuh
            
    return total_value

if __name__ == "__main__":
    # Test cases
    print("Running Fractional Knapsack Tests...")
    
    # Test case 1
    # Items: (weight, value)
    # Item A: (10, 60) -> Ratio 6.0
    # Item B: (20, 100) -> Ratio 5.0
    # Item C: (30, 120) -> Ratio 4.0
    # Capacity: 50
    # Strategy:
    # 1. Take A (10 weight, 60 val) -> rem cap: 40
    # 2. Take B (20 weight, 100 val) -> rem cap: 20
    # 3. Take 20/30 of C (20 weight, 20/30 * 120 = 80 val) -> rem cap: 0
    # Total val: 60 + 100 + 80 = 240
    
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    max_val = fractional_knapsack(items, capacity)
    print(f"Max Value for cap {capacity}: {max_val}")
    assert max_val == 240.0, "Test case 1 failed"
    
    # Test case 2: Kapasitas cukup untuk semua item
    capacity_full = 100
    max_val_full = fractional_knapsack(items, capacity_full)
    print(f"Max Value for cap {capacity_full}: {max_val_full}")
    assert max_val_full == 60 + 100 + 120, "Test case 2 failed"
    
    # Test case 3: Kapasitas 0
    assert fractional_knapsack(items, 0) == 0, "Test case 3 failed"
    
    print("All Fractional Knapsack tests passed!")

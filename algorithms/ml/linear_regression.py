"""
Description:
    [EN] Simple Linear Regression is a supervised learning algorithm that models the relationship between a dependent variable (target) and a single independent variable (feature) by fitting a straight line.
    [ID] Regresi Linear Sederhana adalah algoritma supervised learning yang memodelkan hubungan antara variabel dependen (target) dan satu variabel independen (fitur) dengan mencocokkan garis lurus.

Implementation Details:
    [EN]
    - Model: `y = wx + b`, where `w` is the weight (slope) and `b` is the bias (intercept).
    - Cost Function: Mean Squared Error (MSE) measures the average squared difference between predicted and actual values.
    - Optimization: Gradient Descent is used to minimize the MSE by iteratively updating `w` and `b`.
    - Update Rule: `w = w - lr * dw`, `b = b - lr * db`, where `lr` is the learning rate.
    - Time Complexity: O(epochs * N), where N is the number of data points.
    - Space Complexity: O(1) beyond storing input data.
    [ID]
    - Model: `y = wx + b`, di mana `w` adalah bobot (kemiringan) dan `b` adalah bias (intersep).
    - Fungsi Biaya: Mean Squared Error (MSE) mengukur rata-rata kuadrat selisih antara nilai prediksi dan aktual.
    - Optimasi: Gradient Descent digunakan untuk meminimalkan MSE dengan memperbarui `w` dan `b` secara iteratif.
    - Aturan Update: `w = w - lr * dw`, `b = b - lr * db`, di mana `lr` adalah learning rate.
    - Kompleksitas Waktu: O(epochs * N), di mana N adalah jumlah titik data.
    - Kompleksitas Ruang: O(1) di luar penyimpanan data input.

Usage Documentation:
    [EN]
    - Input: Lists of `xs` (features) and `ys` (targets), learning rate `lr`, and number of `epochs`.
    - Function: `fit_linear_regression(xs, ys, lr, epochs)` trains the model.
    - Returns: Tuple `(w, b)` representing the learned parameters.
    [ID]
    - Input: List dari `xs` (fitur) dan `ys` (target), learning rate `lr`, dan jumlah `epochs`.
    - Fungsi: `fit_linear_regression(xs, ys, lr, epochs)` melatih model.
    - Mengembalikan: Tuple `(w, b)` yang merepresentasikan parameter yang dipelajari.

Examples:
    >>> xs = [0, 1, 2, 3, 4]
    >>> ys = [1, 3, 5, 7, 9]  # y = 2x + 1
    >>> w, b = fit_linear_regression(xs, ys, lr=0.01, epochs=1000)
    >>> abs(w - 2.0) < 0.1
    True
    >>> abs(b - 1.0) < 0.1
    True
"""

from typing import List, Tuple

def predict(x: float, w: float, b: float) -> float:
    return w * x + b

def mse(xs: List[float], ys: List[float], w: float, b: float) -> float:
    n = len(xs)
    if n == 0:
        return 0.0
    return sum((predict(x, w, b) - y) ** 2 for x, y in zip(xs, ys)) / n

def gradient(xs: List[float], ys: List[float], w: float, b: float) -> Tuple[float, float]:
    n = len(xs)
    if n == 0:
        return 0.0, 0.0
    dw = sum(2 * (predict(x, w, b) - y) * x for x, y in zip(xs, ys)) / n
    db = sum(2 * (predict(x, w, b) - y) for x, y in zip(xs, ys)) / n
    return dw, db

def fit_linear_regression(xs: List[float], ys: List[float], lr: float = 0.01, epochs: int = 1000) -> Tuple[float, float]:
    w, b = 0.0, 0.0
    for _ in range(epochs):
        dw, db = gradient(xs, ys, w, b)
        w -= lr * dw
        b -= lr * db
    return w, b

if __name__ == "__main__":
    xs = [0, 1, 2, 3, 4]
    ys = [1, 3, 5, 7, 9]
    w, b = fit_linear_regression(xs, ys, lr=0.05, epochs=5000)
    print(f"w: {w}, b: {b}")
    assert abs(w - 2.0) < 0.05
    assert abs(b - 1.0) < 0.1
    print("All Linear Regression tests passed!")

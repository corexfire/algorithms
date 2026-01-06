# Koleksi Algoritma Python

Repositori ini berisi implementasi berbagai algoritma populer dan struktur data menggunakan bahasa pemrograman Python. Proyek ini bertujuan untuk menyediakan referensi yang jelas, terstruktur, dan edukatif bagi pengembang yang ingin mempelajari atau mengimplementasikan algoritma standar.

Setiap implementasi dilengkapi dengan dokumentasi bilingual (Inggris dan Indonesia), penjelasan kompleksitas, dan contoh penggunaan.

## 1. Pendahuluan

### Tujuan Proyek
- **Edukasi**: Membantu memahami cara kerja algoritma melalui kode yang bersih dan terdokumentasi dengan baik.
- **Referensi**: Menyediakan implementasi standar yang siap digunakan atau dimodifikasi untuk kebutuhan proyek.
- **Praktik Terbaik**: Menunjukkan struktur kode Python yang baik dengan type hinting dan doctests.

### Prasyarat
- **Bahasa**: Python 3.6 atau lebih baru.
- **Library**: Sebagian besar algoritma hanya menggunakan library standar Python (`typing`, `collections`, `math`, dll). Beberapa algoritma Machine Learning mungkin memerlukan `numpy` (opsional untuk versi dasar).

### Instalasi dan Penggunaan
1.  **Clone repositori**:
    ```bash
    git clone https://github.com/username/algoritma.git
    cd algoritma
    ```
2.  **Jalankan algoritma**:
    Setiap file algoritma dapat dijalankan secara langsung untuk melihat hasil tes (doctest) atau contoh penggunaan.
    ```bash
    python3 algorithms/sorting/bubble_sort.py
    ```
3.  **Import ke proyek lain**:
    Anda dapat mengimpor fungsi dari file-file ini ke dalam skrip Python Anda.
    ```python
    from algorithms.sorting.quick_sort import quick_sort
    arr = [3, 1, 4, 1, 5]
    print(quick_sort(arr))
    ```

---

## 2. Daftar Algoritma & 3. Contoh Penggunaan Nyata

Berikut adalah daftar algoritma yang diimplementasikan beserta detail dan contoh kasus nyatanya.

### A. Sorting Algorithms (Pengurutan)

#### 1. Bubble Sort
- **Kategori**: Comparison Sort
- **Kompleksitas**: Waktu: O(N^2), Ruang: O(1)
- **Cara Kerja**: Membandingkan elemen bersebelahan dan menukarnya jika urutannya salah, mengulangi proses hingga tidak ada lagi penukaran.
- **Contoh Kasus Nyata**:
    1.  **Edukasi Pemrograman**: Mengajarkan konsep dasar loop bersarang dan pertukaran variabel kepada pemula.
    2.  **Verifikasi Keterurutan**: Memeriksa apakah daftar sudah terurut (modifikasi Bubble Sort bisa mendeteksi ini dalam O(N)).
    3.  **Grafik Komputer Sederhana**: Mengurutkan poligon berdasarkan kedalaman (Z-order) dalam engine rendering sederhana di mana elemen hampir terurut.

#### 2. Selection Sort
- **Kategori**: Comparison Sort
- **Kompleksitas**: Waktu: O(N^2), Ruang: O(1)
- **Cara Kerja**: Mencari elemen terkecil dari bagian yang belum terurut dan menukarnya dengan elemen pertama dari bagian tersebut.
- **Contoh Kasus Nyata**:
    1.  **Memori Terbatas (Embedded Systems)**: Berguna ketika penulisan ke memori (write) jauh lebih mahal daripada pembacaan, karena Selection Sort melakukan jumlah penukaran minimum (O(N)).
    2.  **Menyeleksi Pemenang**: Mencari Top-K elemen (misal: 3 nilai tertinggi) tanpa perlu mengurutkan seluruh array.
    3.  **Sistem Antrian Sederhana**: Memilih tugas dengan prioritas tertinggi untuk diproses selanjutnya dalam sistem batch sederhana.

#### 3. Insertion Sort
- **Kategori**: Comparison Sort
- **Kompleksitas**: Waktu: O(N^2), Ruang: O(1)
- **Cara Kerja**: Membangun array terurut satu per satu dengan mengambil elemen dan menyisipkannya ke posisi yang benar.
- **Contoh Kasus Nyata**:
    1.  **Pengurutan Kartu di Tangan**: Cara alami manusia mengurutkan kartu remi saat bermain.
    2.  **Online Algorithms**: Mengurutkan data yang datang secara bertahap (streaming), karena sangat efisien untuk menambahkan data baru ke daftar yang sudah terurut.
    3.  **Optimasi Hybrid Sort**: Digunakan oleh algoritma canggih (seperti Timsort atau Introsort) untuk mengurutkan bagian array yang kecil (size < 64) karena overhead-nya sangat rendah.

#### 4. Heap Sort
- **Kategori**: Comparison Sort
- **Kompleksitas**: Waktu: O(N log N), Ruang: O(1)
- **Cara Kerja**: Menggunakan struktur data Binary Heap untuk mengambil elemen maksimum/minimum secara efisien dan menempatkannya di akhir array.
- **Contoh Kasus Nyata**:
    1.  **Sistem Operasi (Process Scheduling)**: Mengelola antrian prioritas proses yang akan dieksekusi CPU.
    2.  **Algoritma Seleksi (Order Statistics)**: Menemukan elemen ke-k terbesar/terkecil dalam kumpulan data besar tanpa mengurutkan semuanya.
    3.  **Sistem Keamanan Embedded**: Digunakan di sistem kritis (seperti kernel Linux) karena menjamin kompleksitas waktu O(N log N) di skenario terburuk, menghindari risiko serangan DoS pada Quick Sort.

#### 5. Counting Sort
- **Kategori**: Non-Comparison Sort
- **Kompleksitas**: Waktu: O(N+K), Ruang: O(K)
- **Cara Kerja**: Menghitung frekuensi kemunculan setiap nilai unik (integer) dan menggunakan aritmatika untuk menentukan posisi setiap elemen.
- **Contoh Kasus Nyata**:
    1.  **Pengolahan Citra (Histogram)**: Menghitung distribusi frekuensi piksel dalam gambar untuk histogram equalization.
    2.  **Sistem Grading**: Mengurutkan ribuan siswa berdasarkan nilai ujian (rentang nilai 0-100 yang terbatas).
    3.  **Bioinformatika**: Mengurutkan urutan DNA berdasarkan frekuensi kemunculan nukleotida atau k-mers tertentu.

---

### B. Graph Algorithms (Graf)

#### 1. Topological Sort
- **Kategori**: DAG (Directed Acyclic Graph)
- **Kompleksitas**: Waktu: O(V + E), Ruang: O(V)
- **Cara Kerja**: Mengurutkan node dalam graf berarah sedemikian rupa sehingga untuk setiap edge u->v, node u muncul sebelum v.
- **Contoh Kasus Nyata**:
    1.  **Manajemen Ketergantungan (Build Systems)**: Menentukan urutan kompilasi file dalam proyek (misal: Makefile atau npm dependencies) agar library prasyarat dikompilasi lebih dulu.
    2.  **Penjadwalan Mata Kuliah**: Menentukan urutan pengambilan mata kuliah berdasarkan prasyarat (pre-requisites) yang ada.
    3.  **Pipeline Data Science**: Mengurutkan task dalam workflow ETL (Extract, Transform, Load) di mana output satu task menjadi input task lain (misal: Apache Airflow).

#### 2. Dijkstra Algorithm
- **Kategori**: Shortest Path
- **Kompleksitas**: Waktu: O(E log V), Ruang: O(V)
- **Cara Kerja**: Menemukan jalur terpendek dari satu node sumber ke semua node lain dalam graf dengan bobot non-negatif.
- **Contoh Kasus Nyata**:
    1.  **Sistem Navigasi (Google Maps)**: Mencari rute tercepat antara dua lokasi di peta jalan raya.
    2.  **Routing Protokol Jaringan (OSPF)**: Menentukan jalur pengiriman paket data paling efisien antar router di internet.
    3.  **Perencanaan Jaringan Logistik**: Menentukan rute pengiriman barang terpendek dari gudang ke berbagai lokasi distribusi.

---

### C. String Algorithms (String)

#### 1. Aho-Corasick
- **Kategori**: Multi-Pattern Matching
- **Kompleksitas**: Waktu: O(N + L + Z), Ruang: O(L * sigma)
- **Cara Kerja**: Membangun automaton dari sekumpulan kata kunci (menggunakan Trie dan failure links) untuk mencari semua kata kunci dalam teks secara bersamaan.
- **Contoh Kasus Nyata**:
    1.  **Intrusion Detection Systems (IDS)**: Snort atau antivirus menggunakan ini untuk memindai paket jaringan terhadap ribuan signature virus/serangan sekaligus.
    2.  **Search Engine Indexing**: Menemukan kemunculan berbagai kata kunci dalam dokumen web secara efisien.
    3.  **Bioinformatika**: Mencari beberapa sekuens DNA pendek dalam database genom yang besar.

#### 2. Z-Algorithm
- **Kategori**: Pattern Matching
- **Kompleksitas**: Waktu: O(N), Ruang: O(N)
- **Cara Kerja**: Menghitung array Z di mana Z[i] adalah panjang substring terpanjang yang dimulai dari i yang juga merupakan prefix dari string.
- **Contoh Kasus Nyata**:
    1.  **Pencarian Teks Efisien**: Mencari kemunculan pola tunggal dalam dokumen teks besar (alternatif KMP).
    2.  **Analisis Struktur DNA**: Menemukan pengulangan motif atau pola tandem repeats dalam sekuens genetik.
    3.  **Kompresi Data**: Membantu menemukan substring berulang untuk algoritma kompresi berbasis kamus (seperti Lempel-Ziv).

#### 3. Manacher's Algorithm
- **Kategori**: Palindrome
- **Kompleksitas**: Waktu: O(N), Ruang: O(N)
- **Cara Kerja**: Menemukan substring palindrom terpanjang dengan memanfaatkan simetri palindrom yang sudah ditemukan sebelumnya.
- **Contoh Kasus Nyata**:
    1.  **Pemrosesan Bahasa Alami (NLP)**: Menganalisis struktur morfologi kata atau menemukan pola simetris dalam teks.
    2.  **Analisis Sekuens Genetik**: Palindrom dalam DNA seringkali merupakan situs restriksi enzim atau memiliki fungsi biologis penting (hairpin loops).
    3.  **Kompresi Audio/Gambar**: Mendeteksi redundansi simetris dalam sinyal untuk teknik kompresi tertentu.

#### 4. Suffix Array
- **Kategori**: String Data Structure
- **Kompleksitas**: Konstruksi O(N log N) atau O(N)
- **Cara Kerja**: Menyimpan indeks awal semua sufiks string yang telah diurutkan secara leksikografis.
- **Contoh Kasus Nyata**:
    1.  **Full-Text Search Indexing**: Memungkinkan pencarian substring apapun dalam teks besar dengan sangat cepat (misal: "grep" pada skala besar).
    2.  **Plagiarism Detection**: Menemukan bagian teks yang identik atau sangat mirip di antara dokumen-dokumen besar (Longest Common Substring).
    3.  **Kompresi Data (Burrows-Wheeler Transform)**: Suffix Array adalah langkah kunci dalam BWT yang digunakan di bzip2 untuk kompresi teks berkualitas tinggi.

---

### D. Math & Cryptography

#### 1. Euclidean Algorithm (GCD)
- **Kategori**: Number Theory
- **Kompleksitas**: Waktu: O(log(min(a, b)))
- **Cara Kerja**: Menghitung Faktor Persekutuan Terbesar (FPB) dari dua angka dengan pembagian berulang.
- **Contoh Kasus Nyata**:
    1.  **Kriptografi (RSA)**: Digunakan untuk menentukan kunci publik dan privat, memastikan dua angka saling prima (coprime).
    2.  **Penyederhanaan Pecahan**: Digunakan dalam sistem komputasi simbolik untuk menyederhanakan hasil operasi matematika.
    3.  **Desain Grafis (Aspek Rasio)**: Menentukan ukuran tile terbesar yang bisa mengisi area persegi panjang tanpa sisa.

#### 2. Modular Exponentiation
- **Kategori**: Modular Arithmetic
- **Kompleksitas**: Waktu: O(log exponent)
- **Cara Kerja**: Menghitung (base^exp) % mod dengan cepat menggunakan metode "square and multiply".
- **Contoh Kasus Nyata**:
    1.  **Enkripsi RSA & Diffie-Hellman**: Operasi inti dalam pertukaran kunci dan enkripsi data yang aman di internet (HTTPS).
    2.  **Primality Testing (Miller-Rabin)**: Digunakan untuk menguji apakah angka besar adalah bilangan prima (penting untuk pembuatan kunci kriptografi).
    3.  **Random Number Generation**: Linear Congruential Generators (LCG) menggunakan aritmatika modular.

#### 3. Bit Manipulation
- **Kategori**: Low-level Optimization
- **Kompleksitas**: O(1) per operasi
- **Cara Kerja**: Memanipulasi bit individual (AND, OR, XOR, Shift) untuk operasi aritmatika atau logika yang sangat cepat.
- **Contoh Kasus Nyata**:
    1.  **Kompresi Data**: Menyimpan status boolean atau data kecil dalam satu integer (flags/bitmasks) untuk menghemat memori.
    2.  **Networking**: Menghitung subnet mask dan alamat IP dalam routing paket.
    3.  **Driver Perangkat Keras**: Mengontrol register hardware dengan menyalakan/mematikan bit tertentu pada alamat memori.

---

### E. Machine Learning & Greedy

#### 1. Linear Regression
- **Kategori**: Supervised Learning
- **Cara Kerja**: Memodelkan hubungan antara variabel dependen dan independen dengan garis lurus (y = mx + c) menggunakan metode kuadrat terkecil atau Gradient Descent.
- **Contoh Kasus Nyata**:
    1.  **Prediksi Harga Rumah**: Memperkirakan harga jual berdasarkan luas tanah, jumlah kamar, dan lokasi.
    2.  **Analisis Tren Ekonomi**: Memprediksi pertumbuhan penjualan atau GDP berdasarkan data historis.
    3.  **Manajemen Risiko**: Menilai hubungan antara usia pengemudi dan frekuensi klaim asuransi.

#### 2. Fractional Knapsack
- **Kategori**: Greedy Algorithm
- **Kompleksitas**: Waktu: O(N log N)
- **Cara Kerja**: Memilih item dengan rasio nilai/berat tertinggi untuk mengisi kapasitas maksimal, memperbolehkan pengambilan sebagian item.
- **Contoh Kasus Nyata**:
    1.  **Manajemen Portofolio Investasi**: Mengalokasikan dana ke berbagai aset (saham, emas, obligasi) yang bisa dibeli dalam pecahan untuk memaksimalkan return.
    2.  **Pemotongan Bahan Baku**: Memotong bahan (kain, logam) untuk memaksimalkan penggunaan sisa bahan dalam manufaktur.
    3.  **Alokasi Bandwidth Jaringan**: Mengatur prioritas paket data yang dapat dipecah untuk memaksimalkan throughput jaringan.

---

## 4. Referensi

- **Buku**:
    - *Introduction to Algorithms* (CLRS) - Cormen, Leiserson, Rivest, Stein.
    - *The Algorithm Design Manual* - Steven Skiena.
- **Website**:
    - [GeeksforGeeks](https://www.geeksforgeeks.org/)
    - [CP-Algorithms](https://cp-algorithms.com/)
    - [Visualgo](https://visualgo.net/)
- **Dokumentasi Python**: [docs.python.org](https://docs.python.org/3/)

---
*Dibuat dengan bantuan AI Assistant di Trae IDE.*

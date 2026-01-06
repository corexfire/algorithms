"""
Suffix Automaton
================

1. English Description
----------------------
A Suffix Automaton (SAM) is a powerful data structure for string processing. It is a Directed Acyclic Graph (DAG) where nodes represent equivalence classes of substrings of a given string, and edges represent character transitions.

- **Logic**: It represents all substrings of a string in a compressed form. Each path from the initial state corresponds to a substring. The structure relies on the concept of "endpos" sets (sets of end positions of substrings). Substrings with the same endpos set form an equivalence class (a state).
- **Properties**:
  - **Minimality**: It has the minimum number of states among all deterministic automata accepting all suffixes of the string.
  - **Linear Construction**: It can be built in linear time O(n) online (adding characters one by one).
- **Time Complexity**: Construction is O(n), where n is the length of the string. Transitions and operations typically take O(1) or O(log k) where k is alphabet size.
- **Space Complexity**: O(n * k) or O(n) depending on transition storage (array vs map). Max number of states is 2n-1, max edges 3n-4.

2. Indonesian Description (Deskripsi Bahasa Indonesia)
------------------------------------------------------
Suffix Automaton (SAM) adalah struktur data yang kuat untuk pemrosesan string. Ini adalah Graf Terarah Tak Bersiklus (DAG) di mana simpul mewakili kelas ekuivalensi substring dari string yang diberikan, dan sisi mewakili transisi karakter.

- **Logika**: SAM merepresentasikan semua substring dari sebuah string dalam bentuk terkompresi. Setiap jalur dari state awal berkorespondensi dengan sebuah substring. Struktur ini bergantung pada konsep himpunan "endpos" (himpunan posisi akhir substring). Substring dengan himpunan endpos yang sama membentuk kelas ekuivalensi (sebuah state).
- **Properti**:
  - **Minimalitas**: Memiliki jumlah state minimum di antara semua automata deterministik yang menerima semua suffix string.
  - **Konstruksi Linear**: Dapat dibangun dalam waktu linear O(n) secara online (menambahkan karakter satu per satu).
- **Kompleksitas Waktu**: Konstruksi adalah O(n), di mana n adalah panjang string. Transisi dan operasi biasanya memakan waktu O(1) atau O(log k) di mana k adalah ukuran alfabet.
- **Kompleksitas Ruang**: O(n * k) atau O(n) bergantung pada penyimpanan transisi (array vs map). Jumlah maksimum state adalah 2n-1, maksimum sisi 3n-4.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Use Cases / Kasus Penggunaan**: 
  - [EN] Finding the Longest Common Substring of two or more strings.
  - [ID] Mencari Substring Umum Terpanjang (Longest Common Substring) dari dua string atau lebih.
  - [EN] Counting the number of distinct substrings.
  - [ID] Menghitung jumlah substring yang berbeda.
  - [EN] Finding the k-th lexicographical substring.
  - [ID] Mencari substring leksikografis ke-k.
  - [EN] Finding the smallest cyclic shift.
  - [ID] Mencari pergeseran siklik terkecil.
  - [EN] Pattern matching (can replace KMP/Aho-Corasick in some contexts).
  - [ID] Pencocokan pola (dapat menggantikan KMP/Aho-Corasick dalam beberapa konteks).
- **Key Components / Komponen Utama**:
  - [EN] `len`: Length of the longest substring in the equivalence class.
  - [ID] `len`: Panjang substring terpanjang dalam kelas ekuivalensi.
  - [EN] `link`: Suffix link pointing to the state representing the longest suffix that is in a different equivalence class.
  - [ID] `link`: Tautan suffix yang menunjuk ke state yang mewakili suffix terpanjang yang berada di kelas ekuivalensi berbeda.
  - [EN] `next`: Dictionary/Map of transitions to next states.
  - [ID] `next`: Kamus/Peta transisi ke state berikutnya.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **How to Use / Cara Menggunakan**:
  1. [EN] Initialize `sam = SuffixAutomaton("your_string")`.
     [ID] Inisialisasi `sam = SuffixAutomaton("string_anda")`.
  2. [EN] Use methods like `sam.longest_common_substring("other_string")`.
     [ID] Gunakan metode seperti `sam.longest_common_substring("string_lain")`.
- **Dependencies / Ketergantungan**: 
  - [EN] Python 3.x. Standard library only.
  - [ID] Python 3.x. Hanya pustaka standar.
- **Testing / Pengujian**: 
  - [EN] Run the file to execute built-in tests for Longest Common Substring functionality.
  - [ID] Jalankan file untuk mengeksekusi tes bawaan untuk fungsionalitas Substring Umum Terpanjang.
"""

class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.len = 0

class SuffixAutomaton:
    def __init__(self, s: str = ""):
        self.states = [State()]
        self.last = 0
        if s:
            for ch in s:
                self.extend(ch)

    def extend(self, ch: str):
        cur = len(self.states)
        self.states.append(State())
        self.states[cur].len = self.states[self.last].len + 1
        p = self.last
        while p != -1 and ch not in self.states[p].next:
            self.states[p].next[ch] = cur
            p = self.states[p].link
        if p == -1:
            self.states[cur].link = 0
        else:
            q = self.states[p].next[ch]
            if self.states[p].len + 1 == self.states[q].len:
                self.states[cur].link = q
            else:
                clone = len(self.states)
                self.states.append(State())
                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].len = self.states[p].len + 1
                self.states[clone].link = self.states[q].link
                while p != -1 and self.states[p].next.get(ch, None) == q:
                    self.states[p].next[ch] = clone
                    p = self.states[p].link
                self.states[q].link = clone
                self.states[cur].link = clone
        self.last = cur

    def longest_common_substring(self, t: str) -> int:
        """
        Finds the length of the longest common substring between the initial string (in SAM) and string t.
        """
        v = 0
        l = 0
        best = 0
        for ch in t:
            while v != -1 and ch not in self.states[v].next:
                v = self.states[v].link
                if v != -1:
                    l = self.states[v].len
            if v == -1:
                v = 0
                l = 0
                continue
            v = self.states[v].next[ch]
            l += 1
            if l > best:
                best = l
        return best

if __name__ == "__main__":
    print("Suffix Automaton Tests...")
    s = "abacaba"
    sam = SuffixAutomaton(s)
    
    # Test 1
    t1 = "acab"
    lcs1 = sam.longest_common_substring(t1)
    print(f"LCS of '{s}' and '{t1}': {lcs1}")
    assert lcs1 == 4
    
    # Test 2
    t2 = "xyz"
    lcs2 = sam.longest_common_substring(t2)
    print(f"LCS of '{s}' and '{t2}': {lcs2}")
    assert lcs2 == 0
    
    # Test 3
    sam2 = SuffixAutomaton("banana")
    t3 = "ananas"
    lcs3 = sam2.longest_common_substring(t3)
    print(f"LCS of 'banana' and '{t3}': {lcs3}")
    assert lcs3 == 5
    
    print("All Suffix Automaton tests passed!")

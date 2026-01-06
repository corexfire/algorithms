"""
LRU Cache / Cache LRU (Least Recently Used)

English Description:
Least Recently Used (LRU) Cache is a cache eviction algorithm that organizes items in order of use. When the cache reaches its capacity, the least recently used item is removed to make room for a new item.

Indonesian Description:
Cache LRU (Least Recently Used) adalah algoritma pengusiran cache yang mengatur item berdasarkan urutan penggunaan. Ketika cache mencapai kapasitasnya, item yang paling jarang digunakan dihapus untuk memberi ruang bagi item baru.

Implementation Details:
- Data Structures / Struktur Data:
  [EN] Uses a combination of a Hash Map (Dictionary) and a Doubly Linked List.
  [ID] Menggunakan kombinasi Hash Map (Dictionary) dan Doubly Linked List.

- Doubly Linked List / Linked List Ganda:
  [EN] Stores items ordered by recency. Head is most recent, Tail is least recent.
  [ID] Menyimpan item yang diurutkan berdasarkan kebaruan. Head adalah yang paling baru, Tail adalah yang paling lama.

- Hash Map / Peta Hash:
  [EN] Maps keys to nodes in the linked list for O(1) access.
  [ID] Memetakan kunci ke simpul dalam linked list untuk akses O(1).

- Time Complexity / Kompleksitas Waktu:
  [EN] O(1) for both `get` and `put` operations.
  [ID] O(1) untuk operasi `get` dan `put`.

- Space Complexity / Kompleksitas Ruang:
  [EN] O(capacity) to store items.
  [ID] O(capacity) untuk menyimpan item.

Usage Documentation:
  [EN] Initialize `LRUCache(capacity)`. Use `put(key, value)` to add items and `get(key)` to retrieve them.
  [ID] Inisialisasi `LRUCache(capacity)`. Gunakan `put(key, value)` untuk menambahkan item dan `get(key)` untuk mengambilnya.

  >>> cache = LRUCache(2)
  >>> cache.put(1, 1)
  >>> cache.put(2, 2)
  >>> cache.get(1)
  1
  >>> cache.put(3, 3)
  >>> cache.get(2)
  -1
"""

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key: int, value: int):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_front(node)
        else:
            if len(self.map) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            node = Node(key, value)
            self.map[key] = node
            self._add_front(node)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("All LRU Cache tests passed!")

from typing import Dict, List, Tuple
from collections import deque

class Node:
    """
    Node for the Aho-Corasick automaton.
    
    Attributes:
        next (Dict[str, int]): Transitions to next nodes based on character.
        fail (int): Failure link index.
        out (List[str]): Output patterns ending at this node.
    """
    def __init__(self):
        self.next: Dict[str, int] = {}
        self.fail: int = 0
        self.out: List[str] = []

def aho_corasick_search(text: str, patterns: List[str]) -> List[Tuple[int, str]]:
    """
    --------------------------------------------------------------------------------------------------------------------
    Description (English):
    --------------------------------------------------------------------------------------------------------------------
    The Aho-Corasick algorithm is a string searching algorithm that locates elements of a finite set of strings
    (the "dictionary") within an input text. It matches all patterns simultaneously. The complexity of the algorithm
    is linear in the length of the patterns plus the length of the searched text plus the number of output matches.
    It constructs a finite state machine (automaton) from the patterns using a Trie (prefix tree) augmented with
    "failure links".

    --------------------------------------------------------------------------------------------------------------------
    Deskripsi (Indonesian):
    --------------------------------------------------------------------------------------------------------------------
    Algoritma Aho-Corasick adalah algoritma pencarian string yang menemukan elemen dari himpunan string terbatas
    ("kamus") di dalam teks input. Algoritma ini mencocokkan semua pola secara bersamaan. Kompleksitas algoritma
    ini linier terhadap panjang pola ditambah panjang teks yang dicari ditambah jumlah kecocokan output.
    Algoritma ini membangun mesin keadaan hingga (automaton) dari pola menggunakan Trie (pohon awalan) yang
    dilengkapi dengan "link kegagalan" (failure links).

    --------------------------------------------------------------------------------------------------------------------
    Implementation Details:
    --------------------------------------------------------------------------------------------------------------------
    1.  **Trie Construction**: Construct a Trie from the set of pattern strings. Each node represents a prefix of one
        or more patterns.
    2.  **Failure Links**: Add failure links to the Trie. A failure link from node u points to the longest proper
        suffix of the string represented by u that is also a prefix of some pattern in the dictionary. This is done
        using Breadth-First Search (BFS).
    3.  **Output Links**: During the BFS, if a failure link points to a node that is an output node (end of a pattern),
        merge the outputs.
    4.  **Search**: Traverse the text using the automaton. If a character matches a transition, follow it. If not,
        follow failure links until a match is found or the root is reached. Check for outputs at each step.

    Time Complexity: O(N + L + Z)
        - N: Length of the text.
        - L: Total length of all patterns (construction phase).
        - Z: Total number of matches occurrences.
    Space Complexity: O(L * sigma)
        - sigma: Size of the alphabet (number of possible characters).

    --------------------------------------------------------------------------------------------------------------------
    Usage Documentation:
    --------------------------------------------------------------------------------------------------------------------
    Args:
        text (str): The input text to search in.
        patterns (List[str]): A list of patterns (keywords) to search for.

    Returns:
        List[Tuple[int, str]]: A list of tuples, where each tuple contains:
            - The starting index of the match in the text (int).
            - The matched pattern string (str).
            The list is ordered by the position in the text where the match ends.

    --------------------------------------------------------------------------------------------------------------------
    Examples:
    --------------------------------------------------------------------------------------------------------------------
    >>> text = "ushers"
    >>> patterns = ["he", "she", "hers"]
    >>> aho_corasick_search(text, patterns)
    [(1, 'she'), (2, 'he'), (2, 'hers')]

    >>> text = "ababaabababa"
    >>> patterns = ["aba", "bab", "aa"]
    >>> matches = aho_corasick_search(text, patterns)
    >>> len(matches)
    9
    >>> (0, 'aba') in matches
    True
    >>> (1, 'bab') in matches
    True
    """
    nodes: List[Node] = [Node()]
    for pat in patterns:
        cur = 0
        for ch in pat:
            if ch not in nodes[cur].next:
                nodes[cur].next[ch] = len(nodes)
                nodes.append(Node())
            cur = nodes[cur].next[ch]
        nodes[cur].out.append(pat)
    q = deque()
    for ch, nxt in nodes[0].next.items():
        nodes[nxt].fail = 0
        q.append(nxt)
    while q:
        v = q.popleft()
        for ch, u in nodes[v].next.items():
            q.append(u)
            f = nodes[v].fail
            while f and ch not in nodes[f].next:
                f = nodes[f].fail
            nodes[u].fail = nodes[f].next[ch] if ch in nodes[f].next else 0
            nodes[u].out += nodes[nodes[u].fail].out
    res: List[Tuple[int, str]] = []
    state = 0
    for i, ch in enumerate(text):
        while state and ch not in nodes[state].next:
            state = nodes[state].fail
        state = nodes[state].next[ch] if ch in nodes[state].next else 0
        if nodes[state].out:
            for pat in nodes[state].out:
                res.append((i - len(pat) + 1, pat))
    return res

if __name__ == "__main__":
    text = "ababaabababa"
    patterns = ["aba", "bab", "aa"]
    matches = aho_corasick_search(text, patterns)
    cnt = {p: 0 for p in patterns}
    for idx, p in matches:
        cnt[p] += 1
        assert text[idx:idx+len(p)] == p
    assert cnt["aba"] == 5
    assert cnt["bab"] == 3
    assert cnt["aa"] == 1
    print("All Aho-Corasick tests passed!")

from typing import List

def boyer_moore_horspool(text: str, pattern: str) -> List[int]:
    m = len(pattern)
    n = len(text)
    if m == 0 or n < m:
        return []
    shift = {c: m for c in set(text)}
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i
    res: List[int] = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            res.append(i)
            i += m
        else:
            i += shift.get(text[i + m - 1], m)
    return res

if __name__ == "__main__":
    t = "abracadabra abracadabra"
    p = "abra"
    idxs = boyer_moore_horspool(t, p)
    print(f"Matches: {idxs}")
    for idx in idxs:
        assert t[idx:idx+len(p)] == p
    assert idxs == [0, 7, 12, 19]
    print("All Boyer-Moore-Horspool tests passed!")

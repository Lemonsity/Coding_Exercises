def isAnagram(s: str, t: str) -> bool:
    count_s = dict()
    count_t = dict()
    for c in s:
        if not (c in count_s):
            count_s[c] = 1
        else:
            count_s[c] += 1
    for c in t:
        if not (c in count_t):
            count_t[c] = 1
        else:
            count_t[c] += 1

    for (char, count) in count_s.items():
        if (not char in count_t) or count != count_t[char]:
            return False
    for (char, count) in count_t.items():
        if (not char in count_s) or count != count_s[char]:
            return False
    return True

def lengthOfLongestSubstring(s : str) -> int:
    length = len(s)
    max_length = 0
    i = 0
    j = 0
    char_set = set()
    while j < length:
        char = s[j]
        if char in char_set:
            while i < j:
                char_ = s[i]
                char_set.remove(char_)
                i += 1
                if char_ == char:
                    break
        else: # char not in char_set:
            char_set.add(char)
            j += 1
            max_length = max(max_length, j - i)
    return max_length

def characterReplacement(s: str, k: int) -> int:
    optimal = 0
    length = len(s)
    for ph in range(26):
        char = chr(ord('A') + ph)
        i = 0
        j = 0
        remaining_k = k
        while j < length:
            j_char = s[j]

            if j_char == char:
                j += 1
            elif j_char != char and remaining_k > 0:
                j += 1
                remaining_k -= 1
            else:
                if (s[i] != char):
                    remaining_k += 1
                i += 1
                continue
            optimal = max(optimal, j - i)

    return optimal

divisor = int(1e9 + 7)
r = [x for x in range(201)]
keys = [(x,y) for x in r for y in r]
diagonal = [(x,x) for x in r]

def subsequencePairCount(nums : List[int]) -> int:
    dp = {}
    for key in keys:
        dp[key] = 0

    result = helper(dp, nums)
    return result

def helper(dp: dict[tuple[int, int], int], nums : List[int]) -> int:
    # List runs empty, collect answers
    if len(nums) == 0:
        total = 0
        for key in diagonal:
            count = dp[key]
            total = total + count
            total = total % DIVISOR
        return total

    head = nums.pop()
    temp = {}
    for key in keys:
        temp[key] = 0
    for (gcd1, gcd2) in keys:
        if (gcd1, gcd2) == (0, 0):
            temp[(head, 0)] = temp[(head, 0)] + 1
            temp[(0, head)] = temp[(0, head)] + 1
        else:
            gcd1_ = gcd(max(gcd1, head), min(gcd1, head))
            gcd2_ = gcd(max(gcd2, head), min(gcd2, head))
            curr = dp[(gcd1, gcd2)]
            temp[(gcd1_, gcd2)] = temp[(gcd1_, gcd2)] + curr
            temp[(gcd1, gcd2_)] = temp[(gcd1, gcd2_)] + curr

    for (gcd_pair, count) in temp.items():
        dp[gcd_pair] = (dp[gcd_pair] + count) % DIVISOR

    return helper(dp, nums)


def gcd(larger : int, smaller : int) -> int:
    if smaller == 0:
        return larger
    return gcd(smaller, larger % smaller)

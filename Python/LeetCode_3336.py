import math

def subsequencePairCount(nums : List[int]) -> int:
    M = max(nums)

    DIVISOR = int(1e9 + 7)
    RANGE = range(M + 1)
    GCD_PAIRS = [(x,y) for x in RANGE for y in RANGE]

    dp = [[0 for x in RANGE] for y in RANGE]
    dp[0][0] = 1

    for num in nums:
        ndp = [[0 for x in RANGE] for y in RANGE]
        for (gcd1, gcd2) in GCD_PAIRS:
            curr = dp[gcd1][gcd2]
            gcd1_ = math.gcd(gcd1, num)
            gcd2_ = math.gcd(gcd2, num)
            ndp[gcd1][gcd2] = (ndp[gcd1][gcd2] + curr) % DIVISOR
            ndp[gcd1_][gcd2] = (ndp[gcd1_][gcd2] + curr) % DIVISOR
            ndp[gcd1][gcd2_] = (ndp[gcd1][gcd2_] + curr) % DIVISOR

        dp = ndp

    total = 0
    for gcd in range(1, M+1):
        total = (total + dp[gcd][gcd]) % DIVISOR
    return total

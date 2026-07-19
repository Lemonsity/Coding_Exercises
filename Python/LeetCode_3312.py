import math

def gcdValues(nums: List[int], queries: List[int]) -> List[int]:
    MAX_NUM = max(nums)
    nums_count = [0] * (MAX_NUM + 1)
    for num in range(MAX_NUM + 1):
        nums_count[num] = 0
    for num in nums:
        nums_count[num] += 1

    gcd_count = [0] * (MAX_NUM + 1)
    for gcd in range(1, MAX_NUM + 1):
        max_other_divisor = MAX_NUM // gcd
        coprime_divisor_pair = [(x,y) \
                                for x in range(1, max_other_divisor + 1) \
                                for y in range(x, max_other_divisor + 1) \
                                if math.gcd(x,y) == 1]
        for (d1, d2) in coprime_divisor_pair:
            if (d1 == d2):        # In this case it must be d1 == 1 == d2
                gcd_count[gcd] += nums_count[gcd] * (nums_count[gcd] - 1) // 2
            else:
                num1 = gcd * d1
                num2 = gcd * d2
                gcd_count[gcd] += nums_count[num1] * nums_count[num2]

    total = 0
    for c in gcd_count:
        total += c
    return total

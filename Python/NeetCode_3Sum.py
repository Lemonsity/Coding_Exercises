def threesum(nums : List[int]) -> List[List[int]]:
    count = dict()
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    keys = sorted(list(count.keys()))
    keys_length = len(keys)

    result = []
    for i1 in range(keys_length):
        num1 = keys[i1]
        for i2 in range(i1, keys_length):
            num2 = keys[i2]
            num3 = 0 - num1 - num2
            if not (num1 <= num2 and num2 <= num3):
                continue
            if not (num3 in count):
                continue
            if (num1 == num2 and count[num1] < 2) or \
               (num2 == num3 and count[num2] < 2) or \
               (num1 == num2 and num2 == num3 and count[num1] < 3):
                continue
            result.append([num1, num2, num3])

    return result

def threesum_twopointers(nums: List[int]) -> List[List[int]]:
    length = len(nums)

    result = []

    nums.sort()
    num1_prev = None

    for i in range(length - 2):
        num1 = nums[i]
        if num1 == num1_prev:
            continue

        num1_prev = num1
        target = 0 - num1
        j = i + 1
        k = length - 1
        num2_prev = None
        num3_prev = None
        while j < k:
            num2 = nums[j]
            num3 = nums[k]
            if num2 == num2_prev:
                j += 1
                continue
            if num3 == num3_prev:
                k -= 1
                continue

            total = num2 + num3
            if total == target:
                result.append([num1, num2, num3])
                j += 1
                num2_prev = num2
            elif total < target:
                j += 1
                num2_prev = num2
            else: # total > target
                k -= 1
                num3_prev = num3

    return result

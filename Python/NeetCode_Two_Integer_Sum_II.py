def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else: # total > target
            j -= 1

    return []

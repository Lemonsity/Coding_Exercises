def hasDuplicate(nums : List[int]) -> bool:
    num_set = set()
    for num in nums:
        if num in num_set:
            return true
        else:
            num_set.add(num)
    return false

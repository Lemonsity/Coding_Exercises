def twoSum(nums: List[int], target : int) -> List[int]:
    indices_by_num = dict()
    for i in range(len(nums)):
        num = nums[i]
        if num not in indices_by_num:
            indices_by_num[num] = [i]
        else:
            indices_by_num[num].append(i)

    result = []
    for num in indices_by_num:
        other_num = target - num
        if other_num in indices_by_num.keys():
            if num != other_num:
                return [indices_by_num[num][0], indices_by_num[other_num][0]]
            if num == other_num and len(indices_by_num[num]) >= 2:
                return [indices_by_num[num][0], indices_by_num[num][1]]
    return []

def longestConsecutive(nums: List[int]) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    if len(heap) == 0:
        return 0

    result = 1
    curr_value = heapq.heappop(heap)
    curr_len = 1
    while heap:
        next = heapq.heappop(heap)
        if curr_value == next:
            continue
        elif curr_value + 1 == next:
            curr_len += 1
            result = max(result, curr_len)
        else:
            curr_len = 1
        curr_value = next

    return result

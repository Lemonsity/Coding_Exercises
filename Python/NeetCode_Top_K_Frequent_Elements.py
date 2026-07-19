def topKFrequent(nums: List[int], k : int) -> List[int]:
    frequency = dict()
    for num in nums:
        frequency[num] = 1 + frequency.get(num, 0)

    heap = []
    for (num, freq) in frequency.items():
        heapq.heappush_max(heap, (freq, num))

    result = [0] * k
    for i in range(k):
        (_, top) = heapq.heappop_max(heap)
        result[i] = top

    return result

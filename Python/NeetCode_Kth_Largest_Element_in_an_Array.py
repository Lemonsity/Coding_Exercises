import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    heap = [-1001] * k # min heap
    for num in nums:
        top = heapq.heappop(heap)
        heapq.heappush(heap, max(top, num))

    return heapq.heappop(heap)

import math
from collections import deque

def gcdSum(nums : list[int]) -> int:
    mxi = 0
    prefix = []
    for numi in nums:
        if numi >= mxi:
            mxi = numi
        prefix.append(math.gcd(numi, mxi))

    q = deque(sorted(prefix))
    total = 0
    while q:
        smallest = q.popleft()
        if q:
            largest = q.pop()
            total = total + math.gcd(smallest, largest)

    return total

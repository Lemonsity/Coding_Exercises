def maxProfit(prices: List[int]) -> int:
    length = len(prices)

    if length == 1:
        return 0

    max_profit = 0

    left = 0
    right = 1
    segment_lowest = prices[left]

    while right < length:
        right_price = prices[right]
        max_profit = max(max_profit, right_price - segment_lowest)

        if right_price < segment_lowest:
            left = right
            segment_lowest = right_price
            right += 1
        else:
            right += 1

    return max_profit

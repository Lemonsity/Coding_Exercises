def maxArea(height: List[int]) -> int:
    MAX_HEIGHT = 10000
    left_most_ = dict()
    right_most_ = dict()

    length = len(height)
    for i in range(length):
        left_height = height[i]
        right_height = height[length - i - 1]
        if not (left_height in left_most_):
            left_most_[left_height] = i
        if not (right_height in right_most_):
            right_most_[right_height] = length - i - 1

    best = 0
    for h in range(1, MAX_HEIGHT + 1):
        if (h in left_most_):
            left_index = left_most_[h]
            for right_height in range(h, MAX_HEIGHT + 1):
                if (right_height in right_most_):
                    best = max(best, (right_most_[right_height] - left_index) * h)

        if (h in right_most_):
            right_index = right_most_[h]
            for left_height in range(h, MAX_HEIGHT + 1):
                if (left_height in left_most_):
                    best = max(best, (right_index - left_most_[left_height]) * h)

    return best

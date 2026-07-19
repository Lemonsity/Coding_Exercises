def productExceptSelf(nums : List[int]) -> List[int]:
    length = len(nums)

    product_from_left = 1
    product_from_right = 1
    products_from_left = [0] * length
    products_from_right = [0] * length

    for i in range(length):
        product_from_left *= nums[i]
        product_from_right *= nums[length - i - 1]
        products_from_left[i] = product_from_left
        products_from_right[length - i - 1] = product_from_right

    print(products_from_left)
    print(products_from_right)

    result = [0] * length
    result[0] = products_from_right[1]
    result[length - 1] = products_from_left[length - 2]
    for i in range(1, length-1):
        result[i] = products_from_left[i-1] * products_from_right[i+1]

    return result

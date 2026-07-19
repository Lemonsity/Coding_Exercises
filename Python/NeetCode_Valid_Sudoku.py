def isValidSudoku(board: List[List[str]]) -> bool:
    grid_mid = [(x, y) for x in range(1, 9, 3) for y in range(1, 9, 3)]
    direction = [(x, y) for x in range(-1, 2, 1) for y in range(-1, 2, 1)]

    for row in range(9):
        occur = set()
        for col in range(9):
            elem = board[row][col]
            if elem != "." and elem in occur:
                return False
            occur.add(elem)

    for col in range(9):
        occur = set()
        for row in range(9):
            elem = board[row][col]
            if elem != "." and elem in occur:
                return False
            occur.add(elem)

    for (x,y) in grid_mid:
        occur = set()
        for (dx, dy) in direction:
            elem = board[x + dx][y + dy]
            if elem != "." and elem in occur:
                return False
            occur.add(elem)

    return True

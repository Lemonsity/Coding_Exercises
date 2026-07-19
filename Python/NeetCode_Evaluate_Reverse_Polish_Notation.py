def evalRPN(tokens: List[str]) -> int:
    stack = []
    tokens.reverse()
    while tokens:
        item = tokens.pop()
        if item == "+":
            op_2 = stack.pop()
            op_1 = stack.pop()
            stack.append(op_1 + op_2)
        elif item == "-":
            op_2 = stack.pop()
            op_1 = stack.pop()
            stack.append(op_1 - op_2)
        elif item == "*":
            op_2 = stack.pop()
            op_1 = stack.pop()
            stack.append(op_1 * op_2)
        elif item == "/":
            op_2 = stack.pop()
            op_1 = stack.pop()
            abs_val = (abs(op_1) // abs(op_2))
            true_val = abs_val * (1 if (op_1 * op_2 >= 0) else -1)
            stack.append(true_val)
        else:
            stack.append(int(item))
    return stack.pop()

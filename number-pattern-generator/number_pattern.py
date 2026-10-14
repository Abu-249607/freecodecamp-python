def number_pattern(n):
    if type(n) != int:
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    pattern = []
    for number in range(1, n+1):
        pattern.append(str(number))

    return " ".join(pattern)

number_pattern(4)

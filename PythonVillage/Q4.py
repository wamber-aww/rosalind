def addOddNumbers(a, b):
    result = 0
    for i in range(a, b+1):
        if i % 2 == 1:
            result = result + i
    return result

def isPower (x, y):
    while (x % y == 0):
        x = x / y
    result = x == 1
    print(result)

isPower(16, 2)
isPower(12, 2)
isPower(100000,10)
isPower(990, 9)
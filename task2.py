def Ipower(n, b):
    if n < 1 or b < 1:
        return False
    if n == 1:
        return True
    if b == 1:
        return n == 1
    power = 1
    while power < n:
        power *= b
    return power == n
print(Ipower(16,2))
print(Ipower(12,2))
print(Ipower(100000, 10))
print(Ipower(990, 9))

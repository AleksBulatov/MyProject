def check(a, b):
    if b <= 1:
        return a == b or a == 1
    if a < 1:
        return False
    if a == 1:
        return True
    if a % b != 0:
        return False
    return check(a // b, b)
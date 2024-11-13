def is_power(a, b):
    if b <= 1:
        return a == b
    if a < 1:
        return False

    power = 1
    while power < a:
        power *= b

    return power == a

print(is_power(16, 2))
print(is_power(12, 2))
print(is_power(100000, 10))
print(is_power(990, 9))


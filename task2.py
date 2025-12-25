def check_power(power, base):
    if power <= 0 and base <= 1:
        return False
    while power % base == 0:
        power = power // base
    return power == 1
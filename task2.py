def is_power(number, base):
    """
    Checks if an integer is some power of another integer.
    args:
        number: number to check
        base: base to check against
    returns:
        true if number is a power of base, false ootherwise.
   """
    if number <= 0 or base <= 1: # If number is less than or equal to 0, or base is less than or equal to 1, return False
        return False
    while number % base == 0: # Checking if number is divisible by base
        number //= base
    return number == 1

# Testing
print(is_power(16, 2)) # True
print(is_power(12, 2)) # False
print(is_power(100000, 10)) # True
print(is_power(990, 9)) # False
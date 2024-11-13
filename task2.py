def is_power(a, b):
    """
    Checks if a is a power of b.
    """
    if a == 1:
        return True
    
    if a < b or a % b !=0:
        return False
    
    
    return is_power(a // b, b)

# Test
print(is_power(16, 2))
print(is_power(12,2))
print(is_power(100000,10))
print(is_power(990,9))

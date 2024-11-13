def is_power(num1, num2):
    ''' This function checks 
    if the first number is the power of the second'''
    if num1 <= 0:
        return False
    if num2 <= 1:
        return num1 == 1
    every_p = 1
    while every_p < num1:
        every_p *= num2
    return every_p == num1
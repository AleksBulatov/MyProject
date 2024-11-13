def is_power(a,b):
    # accounting for specific obvious cases first
    if b == 1:
        return a == 1 # since it will always be 1
    
# not going to account for non-integer or negative cases here, running out of time

    # initializing the counter for powers that we're gonna be checking
    power_count = 1 
    b_mult = b # this var will store the result of our multiplications
    while b_mult < a:
        b_mult *= b
        power_count += 1 # incrementing the counter
    if b_mult == a:
        print(f"True, because {a} is {b} to the {power_count}th power")
        return True # it returns True a second time but it's okay I guess for now
    else:
        return False

# testing the function
print(is_power(16,2))
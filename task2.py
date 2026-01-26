def count(lst):
    n = len(lst)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                inv += 1
    return inv

print(count([2, 4, 1, 3, 5]))     
print(count([1, 9, 3, 4]))        
print(count([4, 3, 2, 1]))        
print(count([]))                
print(count([7]))                
print(count([13, 5, 777]))     
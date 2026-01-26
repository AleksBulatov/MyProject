def count_inversions(lst):
    if lst is None:
        return 0
    n = len(lst)
    if n < 2:
        return 0

    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                inv += 1
    return inv
print(count_inversions([13, 4, 12, 3, 5]))   
print(count_inversions([1]))                 
print(count_inversions([1, 1, 1]))    
print(count_inversions([]))               
print(count_inversions([-1, -2, 0]))

def count_inversions(lst):
    """
    Inversions
    """
    if not lst or len(lst) < 2:
        return 0
    
    inversions = 0
    n = len(lst)
    
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                inversions += 1
    
    return inversions

print (count_inversions ([2,4,1,3,5]))
print (count_inversions ([1]))
print (count_inversions ([3,2,1]))
def inversions(lst):
    count = 0
    n = len(lst)   
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1              
    return count
lst = list(map(int, input("Enter a list of integers( separate them with spaces): ").split()))
print(inversions(lst))
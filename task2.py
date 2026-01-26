def count_inverssions(lst):
    n = len(lst)
    inversions = 0

    for i in range(n):
        for j in range (i+1, n):
            if lst[i] > lst[j]:
                inversions += 1

    return inversions
lst = [2, 4, 1, 3, 5]
print(count_inversions(lst))

def count_inversions(lst):
    """
    Func discription
    """
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1

    return count

lst = [2, 4, 1, 3, 5]
print(count_inversions(lst))

lst = [0, 1, 1, 2, 5]
print(count_inversions(lst))
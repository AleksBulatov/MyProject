def count_inversions(lst):
    count = 0
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1

    return count


lst1 = [4, 2, 9, 3, 5]
print(count_inversions(lst1))

lst2 = [2, 3, 4, 5, 9]
print(count_inversions(lst2))

lst3 = [9, 5, 4, 3, 2]
print(count_inversions(lst3))

lst4 = [5, 2, 2, 1, 1]
print(count_inversions(lst4))

lst5 = []
print(count_inversions(lst5))

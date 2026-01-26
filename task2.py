def count_inversions(lst):
    count = 0
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1

    return count


print(count_inversions([2, 4, 1, 3, 5]))  # 3
print(count_inversions([]))              # 0
print(count_inversions([1]))             # 0
print(count_inversions([3, 2, 1]))       # 3

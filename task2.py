def count_inversions(lst):
inv = 0
n = len(lst)
for i in range(n):
for j in range(i + 1, n):
if lst[i] > lst[j]:
inv += 1
return inv
print(count_inversions([2, 4, 1, 3, 5]))



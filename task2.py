def solve(arr):
    cnt = 0
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            if (arr[i] > arr[j]):
                cnt += 1
    return cnt

print(solve([2, 4, 1, 3, 5]))

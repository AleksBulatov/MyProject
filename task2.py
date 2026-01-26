def count_inversions(lst):
    """Count inversions in a list of integers"""
    count = 0
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1
                
    return count

if __name__ == "__main__":
    test_list = [2, 4, 1, 3, 5]
    result = count_inversions(test_list)
    print(f"Input: {test_list}")
    print(f"Number of inversions: {result}")

    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
        [2, 1, 3, 1, 2]
    ]

    for case in test_cases:
        print(f"{case} -> {count_inversions(case)}")
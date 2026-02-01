def count_inversions(lst):

    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    if len(lst) <= 1:
        return 0
    
    count = 0
    n = len(lst)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1
    
    return count

# Test cases
if __name__ == "__main__":
    # Test example from the question
    print("Test 1:", count_inversions([2, 4, 1, 3, 5]))  # Expected: 3
    
    # Additional test cases
    print("Test 2:", count_inversions([1, 2, 3, 4, 5]))
    print("Test 3:", count_inversions([5, 4, 3, 2, 1]))
    print("Test 4:", count_inversions([]))
    print("Test 5:", count_inversions([1]))
    print("Test 6:", count_inversions([3, 1, 2]))
    print("Test 7:", count_inversions([1, 1, 1]))
    
    try:
        print("Test 8:", count_inversions("not a list"))
    except TypeError as e:
        print("Test 8: Error:", e)

# Time Complexity: O(n²) bc we have nested loops. The outer loop runs n-1 times. The inner loop runs (n-i-1) times. In total, we check n(n-1)/2 pairs. So, this is quadratic time complexity.
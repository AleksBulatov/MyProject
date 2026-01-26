def count_inversions(lst):
    if not lst or len(lst) < 2:
        return 0

    inversion_count = 0

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                inversion_count += 1

    return inversion_count


def test_count_inversions():
    
    test_list = [2, 4, 1, 3, 5]
    result = count_inversions(test_list)
    print(f"List: {test_list}")
    print(f"Number of inversions: {result}")
    print(f"Expected result: 3")
    print(f"Correct: {'Yes' if result == 3 else 'No'}")
    print()

    test_cases = [
        ([1, 2, 3, 4, 5], 0),        
        ([5, 4, 3, 2, 1], 10),      
        ([1], 0),                   
        ([], 0),              
        ([3, 1, 4, 2], 3),        
        ([2, 2, 2, 2], 0),          
        ([7, 5, 3, 1], 6),          
    ]

    for test_list, expected in test_cases:
        result = count_inversions(test_list)
        print(f"List: {test_list}")
        print(f"Result: {result}, Expected: {expected}")
        print(f"Correct: {'Yes' if result == expected else 'No'}")
        print()


if __name__ == "__main__":
    print("Testing the inversion counting function:")
    print("=" * 50)
    test_count_inversions()

    print("\nAlgorithm complexity analysis:")
    print("- Time complexity: O(n²)")
    print("- Space complexity: O(1)")
    print("- Where n is the number of elements in the list")
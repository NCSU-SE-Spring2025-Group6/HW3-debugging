from hw2_debugging import merge_sort

def merge_test_1():
    arr = [1, 6, 9, 7, 2, 4, 3] # Odd number of inputs
    sorted = merge_sort(arr)
    assert sorted == [1, 2, 3, 4, 6, 7, 9]

def merge_test_2():
    arr = [1, 1, 4, 3, 2, 6, 2, 7] # Repeat inputs
    sorted = merge_sort(arr)
    assert sorted == [1, 1, 2, 2, 3, 4, 6, 7]

def merge_test_3():
    arr = [1, 2, 3, 4, 5, 6] # Already sorted
    sorted = merge_sort(arr)
    assert sorted == [1, 2, 3, 4, 5, 6]
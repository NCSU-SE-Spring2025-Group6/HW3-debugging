import pytest
from hw2_debugging import merge_sort

def test_merge_sort_unsorted_array():
    arr = [5, 3, 8, 6, 2, 7, 4, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort_sorted_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort_array_with_duplicates():
    arr = [4, 5, 6, 4, 3, 2, 1, 2]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 2, 3, 4, 4, 5, 6]from hw2_debugging import merge_sort

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
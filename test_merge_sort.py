import pytest
from hw2_debugging import mergeSort

def test_merge_sort_unsorted_array():
    arr = [5, 3, 8, 6, 2, 7, 4, 1]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort_sorted_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort_array_with_duplicates():
    arr = [4, 5, 6, 4, 3, 2, 1, 2]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 2, 2, 3, 4, 4, 5, 6]
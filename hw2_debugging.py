"""
Main script for HW3, contains functions for merge and selection sorting
Author: Autumn Wright (git: a-wright-git)(NCSU: jmwrigh3)
"""

import rand

# Broken Selection Sort
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n): # Should be n-1
#         minIndex = i

#         for j in range(i, n): # Should be i+1
#             if arr[j] > arr[minIndex]: # Should be <
#                 minIndex = j

#         arr[i], arr[minIndex] = arr[minIndex], arr[i]

#     return arr

# Fixed Selection Sort
def selection_sort(arr):
    """Returns a sorted array with selection sort"""
    n = len(arr)
    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def merge_sort(arr):
    """Returns a sorted array with merge sort"""
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """Recombines two arrays by pulling the smallest elements in a loop"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    merge_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            right_index += 1
        merge_index += 1

    while left_index < len(left_arr):
        merge_arr[merge_index] = left_arr[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right_arr):
        merge_arr[merge_index] = right_arr[right_index]
        right_index += 1
        merge_index += 1

    return merge_arr

# Merge Sort

arr1 = rand.random_array([None] * 20)
print(arr1)

arr_out = merge_sort(arr1)
print(arr_out)

# Selection Sort

arr2 = rand.random_array([None] * 20)
print(arr2)

arr2_out = selection_sort(arr2)
print(arr2_out)

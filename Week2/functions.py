import numpy as np

total_comparisons = 0
def swap(array_A, idx_elem1, idx_elem2):
    temp = array_A[idx_elem1]
    array_A[idx_elem1] = array_A[idx_elem2]
    array_A[idx_elem2] = temp


def quicksort(array_A, n, pivot_type):
    global total_comparisons

    if n <= 1:
        return array_A, total_comparisons
    else:
        # Count the total number of comparisons
        total_comparisons += n - 1

        # partition
        array_A, pivot_index = partition(array_A, 0, n - 1, pivot_type)

        # define new subarrays
        array_A_less = np.array(array_A[0:pivot_index])
        array_A_more = np.array(array_A[pivot_index + 1:n])

        # recursive calls around pivot
        array_A_less, total_comparisons = quicksort(array_A_less, len(array_A_less), pivot_type)
        array_A_more, total_comparisons = quicksort(array_A_more, len(array_A_more), pivot_type)

        # concatenate
        return np.concatenate([array_A_less , [array_A[pivot_index]] , array_A_more]), total_comparisons


def isMedian(elem1, elem2, elem3):
    # Determines if elem1 is the median of elem1 elem2 elem3
    return (elem1 < elem2 and elem1 > elem3) or (elem1 > elem2 and elem1 < elem3)


def partition(array_A, left_index, right_index, pivot_type):

    #Swaps elements in array depending on the pivot type
    if pivot_type == "last":
        # swap last element with the first one
        swap(array_A, left_index, right_index)

    elif pivot_type == "medthree":

        # find the middle index of an array, which can be of size pair or impair
        len = right_index + 1 - left_index
        if (len % 2 == 0):
            # array is pair size
            middle_index = left_index + (right_index - 1) / 2
        else:
            # array is pair size
            middle_index = left_index + right_index / 2

        # Find median of the first, last and middle elements
        if (isMedian(array_A[middle_index], array_A[left_index], array_A[right_index])):
            # middle is the median
            swap(array_A, left_index, middle_index)
        elif (isMedian(array_A[right_index], array_A[left_index], array_A[middle_index])):
            # last is the median
            swap(array_A, left_index, right_index)

    # pivot will always be the left element after the swaps that might or not happen
    pivot = array_A[left_index]
    i = left_index + 1

    for j in range(left_index + 1, right_index + 1):
        if (array_A[j] < pivot):
            # swap
            swap(array_A, i, j)
            # update i
            i = i + 1
    # swap
    swap(array_A, left_index, i - 1)
    # update pivot_index
    pivot_index = i - 1

    return array_A, pivot_index

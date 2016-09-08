def merge_sort(input_array):
    n = len(input_array)

    if n > 1:

        # Divide
        array_A = input_array[0: int(n / 2)]
        array_B = input_array[int(n / 2): n]

        # Recursive calls and count number of inversions
        array_A, left_inv = merge_sort(array_A)
        array_B, right_inv = merge_sort(array_B)

        # Merge
        input_array, split_inv = merge(array_A, array_B)

        # sum of inversions
        total_inv = left_inv + right_inv + split_inv

        return input_array, total_inv
    else:
        return input_array, 0


def merge(array_A, array_B):
    i = 0
    j = 0
    k = 0
    split_inv = 0
    len_arrayA = len(array_A)
    len_arrayB = len(array_B)

    # Init of output array
    output_array = (len_arrayA + len_arrayB) * [0]

    # See pseudo code in the lecture.
    while i < len_arrayA and j < len_arrayB:
        if int(array_A[i]) < int(array_B[j]):
            output_array[k] = array_A[i]
            i = i + 1
        elif int(array_A[i]) > int(array_B[j]):
            output_array[k] = array_B[j]
            j = j + 1
            # Split inversions are the number of left elements in array A, see lecture
            split_inv = split_inv + len(array_A) - i
        k = k + 1

    # Complete the array with the elements from array A ,if Any
    while i < len_arrayA:
        output_array[k] = array_A[i]
        i = i + 1
        k = k + 1

    # Complete the array with the elements from array B ,if Any
    while j < len_arrayB:
        output_array[k] = array_B[j]
        j = j + 1
        k = k + 1

    return output_array, split_inv

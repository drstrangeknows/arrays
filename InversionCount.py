def mergeSort(arrayay, n):
    temp_array = [0] * n
    return _mergeSort(arrayay, temp_array, 0, n - 1)


# Sort list [low..high] using auxiliary space temp_array
def _mergeSort(array, temp_array, left, right):
    inv_count = 0

    if left < right:
        # find mid point
        mid = (left + right) // 2
        # recursively split runs into two halves until run size == 1,
        # then merge them and return back up the call chain
        inv_count += _mergeSort(array, temp_array, left, mid)

        inv_count += _mergeSort(array, temp_array, mid + 1, right)

        inv_count += merge(array, temp_array, left, mid, right)

    return inv_count


# Merge two sorted sublists array[low .. mid] and array[mid + 1 .. high]
def merge(array, temp_array, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    # While there are elements in the left and right runs
    while i <= mid and j <= right:

        if array[i] <= array[j]:
            temp_array[k] = array[i]
            k += 1
            i += 1
        else:
            temp_array[k] = array[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    # Copy remaining elements
    while i <= mid:
        temp_array[k] = array[i]
        k += 1
        i += 1

    while j <= right:
        temp_array[k] = array[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        array[loop_var] = temp_array[loop_var]

    return inv_count


array = [9, 1, 6, 4, 5]
n = len(array)
# get inversion count by performing merge sort on list
result = mergeSort(array, n)
print("Number of inversions are", result)
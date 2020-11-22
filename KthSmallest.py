def kthSmallest(array, low, high, k):
    if (k > 0 and k <= high + 1):
        index = divideArray(array, low, high)

        if (index == k - 1):
            return array[index]
        if (index > k - 1):
            return kthSmallest(array, low, index - 1, k)

        return kthSmallest(array, index + 1, high, k)

    return 999999999999


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def divideArray(array, low, high):
    x = array[high]
    i = low
    for j in range(low, high):
        if (array[j] <= x):
            swap(array, i, j)
            i += 1
    swap(array, i, high)
    return i


# def divideArray(array, low, high):
#     pivot = array[high]
#     swap(array, low + pivot, high)
#     return partition(array, low, high)


if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 20, 55, 35, 10, 58, 67, 685, 102, 24, 66, 94]
    n = len(array)
    k = 15
    print(k,"th smallest element is",kthSmallest(array, 0, n - 1, k))
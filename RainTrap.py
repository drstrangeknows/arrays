'''

'''

def findWater(arr, n):
    maxLeft = [0]*n
    maxRight = [0]*n

    leftMax = maxLeft[0] = arr[0]
    rightMax = maxRight[n-1] = arr[n-1]
    storedWater = 0

    for i in range(1, n):
        if (arr[i]>leftMax):
            leftMax = arr[i]

        maxLeft[i] = leftMax

    for i in range(n-2, -1, -1):
        if(arr[i]>rightMax):
            rightMax = arr[i]

        maxRight[i]=rightMax

    print(maxLeft)
    print(maxRight)

    for i in range(0, n):
        if maxLeft[i]<maxRight[i]:
            result = maxLeft[i]-arr[i]
        else:
            result = maxRight[i]-arr[i]

        storedWater += result
    return storedWater

def main():
    arr = [5,3,4,6,3,6]
    n = len(arr)

    print("Total capacity of Water stored ", findWater(arr, n))

if __name__ == "__main__":
    main()

# def findWater(array, n):
#     # lists to store the left max and right max of each point in the map
#     left = [0] * n
#
#     right = [0] * n
#     # keeps track of the total water as we traverse the elevation map
#     water = 0
#     # default values
#     left[0] = array[0]
#     # filling the left max list
#     for i in range(1, n):
#         left[i] = max(left[i - 1], array[i])
#
#     right[n - 1] = array[n - 1]
#     # filling the right max list
#     for i in range(n - 2, -1, -1):
#         right[i] = max(right[i + 1], array[i]);
#         # calculating the amount of water
#     for i in range(0, n):
#         water += min(left[i], right[i]) - array[i]
#
#     return water
#
#
# array = [5,3,4,6,3,6]
# n = len(array)
# print("Maximum water", findWater(array, n))

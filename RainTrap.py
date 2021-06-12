'''
Basic idea is to find water stored by each bar and add it.
1st and last bars won't store any water as they form the boundaries
within which water will be stored. Idea is to calculate for each bar-
what will be it's left bar & what will be it's right bar. Use 2 arrays
of the length of original heights array-maxLeft[] & maxRight[]. Iterate
original array and store the maxLeft for each bar by comparing with
default maxLeft i.e. 1st item. Siilarly for right bar by comparing 
by default maxRight i.e. last item. This wasy we established boundary
for each bar on it's left and right. Now, for each bar water will be
stored depending on the smaller of the 2 boundaries and that will be
difference of height of smaller boundary and the bar height.
Conclusion - eastablish left and right boundary for each bar, calc min
of the two boundaries for each bar and then calc height difference of the
boundary from the bar and keep adding to a counter

'''

def findWater(height, n):
        n=len(height)
        if n>0:
            maxLeft = [0]*n
            maxRight = [0]*n

            leftMax = maxLeft[0] = height[0]
            rightMax = maxRight[n-1] = height[n-1]
            storedWater = 0

            for i in range(1, n):
                if (height[i]>leftMax):
                    leftMax = height[i]

                maxLeft[i] = leftMax

            for i in range(n-2, -1, -1):
                if(height[i]>rightMax):
                    rightMax = height[i]

                maxRight[i]=rightMax

            for i in range(0, n):
                if maxLeft[i]<maxRight[i]:
                    result = maxLeft[i]-height[i]
                else:
                    result = maxRight[i]-height[i]

                storedWater += result
            return storedWater
        else:
            return 0

def main():
    arr = [5,3,4,6,3,6]

    print("Total capacity of Water stored ", findWater(arr))

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

def findMaxSum(arr, n):

    maxum = curSum = arr[0]

    for i in range(1, n):
        curSum = max(curSum + arr[i], arr[i])
        maxum = max(curSum, maxum)

    # while i < n-1:
    #     curSum = arr[i]
    #     for j in range(i+1, n):
    #         curSum = curSum + arr[j]
    #         curSUm = max(curSum, arr[i])
    #         if curSum > maxum:
    #              maxum = curSum
    #     i+=1

    # for i in range(0, n):
    #     maxum = max(arr[i], maxum)

    return maxum

def main():
    arr = [-1, -2, 3, -2, 4, -8]
    n = len(arr)

    print("Max sum: ", findMaxSum(arr, n))

if __name__ == "__main__":
    main()
def findProfit(array, n):
    if (n == 1):
        return

    i = 0
    while (i < n):

        while (i<n-1 and array[i + 1] <= array[i]):
            i += 1

        if (i == n - 1):
            break

        buy = i
        i += 1

        while (i < n and array[i] <= array[i + 1]):
            i += 1

        sell = i

        print("Buy on day: ", buy+1, "\t",
              "Sell on day: ", sell+1)


array = [7,6,5,4,3,1]
n = len(array)

findProfit(array, n)
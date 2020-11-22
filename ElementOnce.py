arr = [7, 8, 8, 9, 9, 10, 10]
n = len(arr)

for i in range(0, n, 2):

    if (arr[i]!=arr[i+1]):
        break

print(arr[i])




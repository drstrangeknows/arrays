def rotate_mat(matrix):
    n = len(matrix[0])

    # transpose
    for i in range(len(matrix)):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse
    for i in range(0, len(matrix)):
        li = 0
        ri = len(matrix[i]) - 1

        while li < ri:
            temp = matrix[i][li]
            matrix[i][li] = matrix[i][ri]
            matrix[i][ri] = temp

            li = li + 1
            ri = ri - 1

    # display
    for i in range(n):
        print(matrix[i])


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

rotate_mat(matrix)

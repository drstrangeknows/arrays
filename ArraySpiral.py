def spiralPrint(m, n, matrix):

    k=s=0
    p=q=n-1

    while(k<=q and p>=s):

        i=k
        for j in range(s,q+1):
            print(matrix[i][j])

        j=q
        s=s+1
        for i in range(s,p+1):
            print(matrix[i][j])

        i=p
        q=q-1
        for j in range(q,k-1,-1):
            print(matrix[i][j])

        j=k
        p=p-1
        for i in range(p, s-1, -1):
            print(matrix[i][j])

        k=k+1
        #s=s+1
        #p=p-1
        #q=q-1


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
          ]
R=4
C=4
spiralPrint(R, C, matrix)
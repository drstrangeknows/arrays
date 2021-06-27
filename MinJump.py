def minJumpsToEnd(array1, n):

    i=0
    a = array1[0]
    b = array1[0]
    jump = 1

    for i in range(1, n):

        if i ==  len(array1) - 1:
            return jump

        a -=1
        b -=1

        if array1[i] > b:
            b = array1[i]

        if a == 0:
            jump +=1
            a = b

    return jump


def main():
    my_list = [1, 3, 5, 8, 2, 7, 6, 8]
    n = len(my_list)

    print("Minimum number of jumps to reach end is : ", minJumpsToEnd(my_list, n))

if __name__ == "__main__":
    main()
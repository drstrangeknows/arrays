def main():

    input_num = 11
    
    print("Square Root is ", findSquareRoot(input_num))


def findSquareRoot(input_num):

    if input_num == 0 or input_num == 1:
        return input_num

    start = 1
    end = input_num

    while(start<=end):

        mid = (start + end) // 2

        if mid * mid == input_num:
            return  mid

        if mid * mid > input_num:
            end = mid-1
        else:
            start = mid+1
            answer = mid

    return answer



if __name__ == "__main__":
    main()
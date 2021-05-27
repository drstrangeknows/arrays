#Hacker Rank code
'''
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    my_len = len(h)
    rb = [0]*my_len
    lb = [0]*my_len

    rb_stac = []

    rb_stac.append(my_len-1)
    rb[my_len-1] = my_len

    for i in range((my_len-2), -1, -1):
        while rb_stac and h[rb_stac[-1]] > h[i]:
            rb_stac.pop()
        if not rb_stac:
            rb[i] = my_len
        else:
            rb[i] = rb_stac.pop()
        rb_stac.append(i)

    lb_stac = []
    lb_stac.append(0)
    lb[0] = -1
    j = 1
    for j in range(my_len):
        while lb_stac and hist_arr[lb_stac[-1]] >= h[j]:
            lb_stac.pop()
        if not lb_stac:
            lb[j] = -1
        else:
            lb[j] = lb_stac.pop()
        lb_stac.append(j)

    max_ar = 0

    for ar in range(my_len):
        wid = rb[ar] - lb[ar] - 1
        the_area = wid * h[ar]
        max_ar= max(max_ar, the_area)

    return max_ar


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

############################  My Code  ###################################################################
def find_area(hist_arr):

    maxArea = 0
    stac = []

    for i, h in enumerate(hist_arr):
        start = i

        while stac and stac[-1][1] > h:
            index, height = stac.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stac.append((start, h))

    for i, h in stac:
        maxArea = max(maxArea, h * (len(hist_arr) - i))
    return maxArea

def main():
    hist = [6, 2, 5, 4, 5, 1, 6]

    largest_area = find_area(hist)

    print("Largest Rectangle Area Is: ", largest_area)

if __name__ == '__main__':
    main()
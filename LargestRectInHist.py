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
'''
Brute force approach
for each bar, calculate all rectangles wrt the bar and compute max of them
for in in range(len(heights)):
    minH = arr[i]
    for j in range(i, len(heights)):
        minH = min(arr[i], arr[j])
        maxArea=max(maxArea, minH*(j-i+1))
return maxArea

More efficient sol-
We need left limit and right limits of each bar in order to calculate area constituted by that bar
After that we can compare for maxArea.

Draw few example histos and analyse
    * Right Limit - While scanning the array 1 bar at a time, as we reach a lower bar than the one being scanned
    that means the bar being scanned can't be extended further - this is the right limit of the bar
    * Left Limit - Similarly, for any bar, a lower bar to the left will be it's left limit.
    
    Here we can think that this problem can solved on similar lines to Rain Water trap problem
        - Get Right limit for each bar
        - Get left limit for each bar
        - Right - Left * height is area
        - Get max area
    However, the tricky thing is unlike the rain water the limits for each bar can be extended further even
    if we find a minimum element(in rain water we find max and setlle there as it is about storing water in 
    that capacity and not about extending further to calculate the area). We need something to keep track of
    further bars which can be compared to current bars, to get actual limit of each bar - That's where Stack
    comes into picture - LIFO - latest element is processed first

    So we can scan the array as usual from index 1. Push the 1st element onto stack. While scanning from 1st 
    index, if top of stack is > than current array element, we calculate area of top of stack then and there 
    by right - left* height. We keep updating a maxArea accordingly. Now, right limit of popped element will be the index of current bar of array, left limit 
    will be top of stack. Then we push we push current array element on stack(all elements are pushed on stack, even 
    if top of stack is < curr array element). IMPORTANT: Right here when we push the current array element on stack, 
    we can use which index to use as cur element's left limit. As top of stack was higher than current, that means current
    can be extended to left till top of stack element. ame way we can keep checking top of stack till it is > curr element
    and while pushing current element set it's index as that of last popped item from stack.

    After iterating the array, we should ckeck if stack is not empty then calculate area for them using len(array)-index*height
    and update maxArea
'''

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
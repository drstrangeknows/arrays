#!/bin/python3
# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    str_len = len(w)
    
    for i in range(str_len-1, 0, -1):
        if w[i] > w[i-1]:
            break

    if i == 1 and w[i]<=w[i-1]:
        print("no answer")
        return
    
    prev = w[i-1]
    smallest = i
    
    for j in range(i+1, str_len):
        if w[j] > prev and w[j] < w[smallest]:
            smallest = j
    
    w[i-1], w[smallest] = w[smallest], w[i-1]
    
    w = "".join(w[:i])+"".join(sorted(w[i:]))
    print(w)
    print(type(w))

if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        biggerIsGreater(w)
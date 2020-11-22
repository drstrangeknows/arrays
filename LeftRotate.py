# Function to left rotate a list by d positions
def leftRotate(A, d):
    return A[d:] + A[:d]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    d = 2

    result = leftRotate(A, d)

    print(result)
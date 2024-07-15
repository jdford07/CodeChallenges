import math

inputArr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
inputArr2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotateMatrix(inputArr):
    inputArrLength = len(inputArr)  # Since N x N, can be reused for row and column
    currentColumn = 0
    rotatedArr = []

    for row in range(inputArrLength):
        rotatedArr.append([None] * inputArrLength)

    for i in range(inputArrLength, 0, -1):
        for j in range(inputArrLength):
            rotatedArr[j][currentColumn] = inputArr[i - 1][j]
        currentColumn += 1

    return rotatedArr


def rotateMatrixInPlace(arr):
    # for i = 0 to n
    # temp = topLeft[i]
    # topLeft[i] = bottomLeft[i]
    # bottomLeft[i] = bottomRight[i]
    # bottomRight[i] = topRight[i]
    # topRight[i] = temp

    # Implemented based off of the book, was unable to find proper index math in custom solution
    n = len(arr)

    for layer in range(math.floor(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = arr[first][i]

            # bottomLeft -> topLeft
            # N,0 -> 0,0
            arr[first][i] = arr[last - offset][first]

            # bottomRight -> bottomLeft
            # N,N -> N,0
            arr[last - offset][first] = arr[last][last - offset]

            # topRight -> bottomRight
            # 0,N -> N,N
            arr[last][last - offset] = arr[i][last]

            # topLeft -> topRight
            # 0,0 -> 0,N
            arr[i][last] = top
    return arr


# answer = rotateMatrix(inputArr)
answer = rotateMatrixInPlace(inputArr2)
print(answer)


# 0,1 -> 1,N
# 1,N -> N,N-1
# N,N-1->N-1,0
# N-1,0-> 0,1

# 0,2-> 2,N
# 2,N->N,N-2
# N,N-2->N-2,0
# N-2,0->0,2

# 1,1 -> 1,N-1
# 1,N-1->N-1,N-1
# N-1,N-1->N-1,1
# N-1,1-> 1,1

# [1, 2, 3,  4]
# [5, 6, 7,  8]
# [9,10,11, 12]
# [13,14,15,16]

# [13, 9, 5, 1]
# [14, 10, 6,2]
# [15, 11, 7,3]
# [16, 12, 8,4]

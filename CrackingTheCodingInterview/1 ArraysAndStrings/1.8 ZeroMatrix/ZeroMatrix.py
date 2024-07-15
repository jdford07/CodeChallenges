inputMatrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
inputMatrix2 = [[1, 2, 3, 4, 0]]
inputMatrix3 = [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


def zeroMatrix(inputMatrix):
    m = len(inputMatrix)
    zeroRow = set()
    zeroCol = set()
    if len(inputMatrix) == 0:
        return False

    for row in range(m):
        for col in range(len(inputMatrix[row])):
            if inputMatrix[row][col] == 0:
                zeroRow.add(row)
                zeroCol.add(col)

    for row in range(m):
        for col in range(len(inputMatrix[row])):
            if (row in zeroRow) or (col in zeroCol):
                inputMatrix[row][col] = 0
    return True


answer = zeroMatrix(inputMatrix3)
print(answer)

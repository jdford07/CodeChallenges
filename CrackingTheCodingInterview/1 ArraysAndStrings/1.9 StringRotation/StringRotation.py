str1 = "thisisastring"
str2 = "stringthisisa"


# Pass in already calculcated and unchanging string length to avoid repetitive counting
def shiftStr(str, strLen):
    str = list(str)
    firstChar = str[0]
    for i in range(strLen):
        if i < strLen - 1:
            str[i] = str[i + 1]
        else:
            str[strLen - 1] = firstChar

    return "".join(str)


def solution(s1, s2):
    str1Length = len(s1)
    str2Length = len(s2)
    if str1Length != str2Length:
        return False

    isRotation = False
    indexCount = 0
    while not isRotation and indexCount < str1Length:
        if s1 == s2:
            isRotation = True
        else:
            s1 = shiftStr(s1, str1Length)
            indexCount += 1

    return isRotation


answer = solution(str1, str2)
print(answer)

str1 = "pale"
str2 = "rbale"


def OneAway(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    diffCount = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diffCount += 1
            if diffCount > 1:
                return False
        return True
    elif len(str1) == len(str2) + 1:
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                if str1[i + 1] != None and str2[i] != str1[i + 1]:
                    diffCount += 1
            if diffCount > 0:
                return False
        return True

    elif len(str1) == len(str2) - 1:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str2[i + 1] != None and str1[i] != str2[i + 1]:
                    diffCount += 1
            if diffCount > 0:
                return False
        return True
    else:
        return False


answer = OneAway(str1, str2)
print(answer)

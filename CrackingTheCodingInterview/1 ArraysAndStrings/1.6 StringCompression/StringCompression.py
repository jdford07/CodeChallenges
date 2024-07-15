str = list("aaaaaabbbbbbcccccaaaabbbbddddaaaassssaaaabcbcbcbcbcbbcaaaaa")


def StringCompression(str):
    charCount = 0
    newStr = ""
    for i in range(len(str)):
        charCount += 1
        if (i == len(str) - 1) or (str[i] != str[i + 1]):
            newStr += f"{str[i]}{charCount}"
            charCount = 0

    if len(newStr) > len(str):
        return "".join(str)
    else:
        return newStr


answer = StringCompression(str)
print(answer)

string1 = "thisisastring"
string2 = string1[::-1]

sortedString1 = "".join(sorted(string1))
sortedString2 = "".join(sorted(string2))

if(sortedString1 == sortedString2):
    print("True")
else:
    print("False")
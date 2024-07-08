import sys

uniqueStr = "notUiqe"
nonUniqueStr = "unique"


# Implementation with use of additional data structures
# uniqueChars = {}
# for char in uniqueStr:
#     if(char in uniqueChars):
#         print("String has duplicate characters")
#         sys.exit()
#     else:
#         uniqueChars[char] = 0

# print("String has unique characters")

# Implementation withOUT use of additional data structures
for i, char in enumerate(nonUniqueStr):
    for j, char2 in enumerate(nonUniqueStr):
        if(i == j):
            continue # Skip iteration 
        if(char == char2):
            print("String has duplicate characters")
            sys.exit()

print("String has unique characters")
    
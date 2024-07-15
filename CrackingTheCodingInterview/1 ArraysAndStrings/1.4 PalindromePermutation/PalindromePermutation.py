import sys
inputStr = "TactCoa".lower()
uniqueChars = {}
oddNumCount = 0

for char in inputStr:
    if(char in uniqueChars):
        uniqueChars[char] += 1
    else:
        uniqueChars[char] = 1
        
for key in uniqueChars.keys():
    if(uniqueChars[key] % 2 != 0):
        oddNumCount+=1
        if(oddNumCount > 1):
            print("Multiple letters with odd number occurences")
            print(f"FALSE: {inputStr} is not a permutation of a palindrome")
            sys.exit() # Return false in proper function layout

print(f"TRUE: {inputStr} is a permutation of a palindrome")
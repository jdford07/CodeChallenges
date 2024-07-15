# String Rotation

## Challenge Details

- Source: Chapter 1, Question 9, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
    - Example: "waterbottle" is a rotation of "erbottlewat"
  - Hints: #34, #88, $104
  - Solution: Page 207

## Challenge Commentary

### Initial Thoughts

> First, I need to think through what it means for a string to be a rotation of another.
> I think this means "ThisIsAString" would be a rotation of "StringThisIsA" or vice versa
>
> The other thing to clarify would be: Is one call to isSubString a singular call or is it a singular call inside a loop (which would be multiple calls but only called in one programmatic place). My interpretation, since I can't call the author, is I can call isSubstring once but inside of a loop
>
> Even though the question declares I can use isSubstring, do I need to? I think I can shift each character in `str1` and do a comparison after each shift to see if `str1` == `str2`. If `str2` is a rotation of `str1` then eventually, after N shifts, the strings will be equivalent
>
> Performing a character shift could increase time complexity since in the worst case we would shift every single character, but O(N) isn't objectively terrible. This approach would save us from having to try and decipher which piece of `str1` is inside `str2` with no shift. In the example, this saves us from having to find "bottle", which thinking through seems like an impossible/unworth-while task when extrapolated/scaled
>
> To find any early exit places, if the strings are not the same length, we can immediately return `False`. We could also perform a check to see if both strings contain the same characters but that could needlessly increase time, space and code complexity

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N^2) I think`\
**Completion Date:** `07\14\2024`\
**`Python3` Specific Notes:**
> First get the lengths of the 2 input strings, if they're different then we return False
>
> Declare a flag to determine if the comparison of the 2 strings are equal. This allows us to break out of the while loop and also compare the 2 strings with no shifting
>
> A while loop made more sense instead of a for loop but I implement a counter to make sure we don't go past the length of the input string, avoiding an infinite loop
>
> If the strings are not equal, pick one of the 2 strings to consistently rotate. I chose input string 1
>
> Call shiftStr function. Pass in the string and the length, we pass in the already calculated length to save processing time (if it's non-negligable)
>
> - Convert input string to char array so we can manipulate indices
> - Store first character of string for later placement at the last index, post shift
> - Loop through the str and replace each ith index value with the ith+1 index's value
> - Once the last index is reached, overwrite with stored firstCharacter value
> - Join the charArray back to a string
> - The split to char array is O(N), the shift is O(N) and the join is O(N) time
>   - Overall O(N+N+N) or O(3N) is O(N) for ShiftStr function
>
> The while loop is O(N) time with the nested ShiftStr O(N), making the time complexity O(N^2) time. This is not ideal and could most likely be improved. I think overall the same approach can be tackled in a more efficient manner, potentially getting to O(N)

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- I was wildly off base and implemented an overthought solution along with a less efficient solution
- The book points out a math series where a substring of s1 = x and a substring of s2 = y with the rotated string being yx
  - We can deduce that yx will always be inside of xyxy or s2 will always be inside s1s1
  - We can call, after making sure the string lengths are equal, isSubStr(s1s1, s2)
- This solution challenges the though approach of if there's a simpler, mathematical, way to approach the solution instead of straight programmatic
  - My solution went straight to programmatic with index shifting, when that was wholly unrequired after writtin out logic deduction
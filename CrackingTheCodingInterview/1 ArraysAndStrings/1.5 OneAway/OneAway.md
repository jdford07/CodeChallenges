# Palindrome Permutation

## Challenge Details

- Source: Chapter 1, Question 5, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
  - Example:
    - pale, ple   -> true
    - pales, pale -> true
    - pale, bale  -> true
    - pale, bake  -> false
  - Hints: #23, #97, #130
  - Solution: Page 199

## Challenge Commentary

### Initial Thoughts

> - We can return false if the 2nd string is 2 or more shorter/longer in length than the 1st string\
> - If the strings are in equal length or 1+/- of each other we can continue 
>   - We have to check in all 3 cases if a character replacement occurs, since the replacement is an invisible action with regards to string length comparison. A direct string comparison won't work since we won't be able to tell how many of each character is changed unless we iterate over both strings somehow\
> - If the strings are the same length we can iterate over both strings and compare each index to each other, if more than 1 index is not equal then return false
> - If the strings are 1 +/- in length we know automatically the strings are one away
>   - As an edge case: We need to check if any character replacement has occured which would invalidate the one away principle
>   - In the case of `String2` length +1 more than `String1` length:
>     - We know in this scenario that `String2` has 1 additional character than `String1`
>     - We can iterate over `String1` and compare each character index
>       - If there is a mismatch, we can check the ith+1 index to see if the current char[i] == char[i+1]
>         - This would mean the current char[i] was potentially the additional char
>   - In the case of `String2` length -1 less than `String1` length:
>     - We know in this scenario that `String1` has 1 additional character than `String2`
>     - We can iterate over `String2` and compare each character index
>       - If there is a mismatch, we can check the ith+1 index to see if the current char[i] == char[i+1]
>         - This would mean the current char[i] was potentially the removed char
> - We could take a different approach and try to use hashtables to keep track of character occurences but that seems overly complex and would likely require too many conditionals
> - We could find all different permutations of the 3 operations on each string to see if they eventually match but that would be slow and riddled with inefficiency

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\08\2024`\
**`Python3` Specific Notes:**
> I implemented the approach that I laid out in the initial thoughts\
> There are multiple methods to entering the specific logic blocks, in Python I had to use an if elif sequence when I would have preferred to use a switch block. Due to Python not having a clean switch block implementation I went with the if elif sequence

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

- One thing I could have done better is to remove the duplicate code inside the 2 python elif blocks as they perform the exact same operations just using the smaller of the 2 input strings
  - To do this I would have created a 2nd function and argument 1 would have been the smaller string `str1` and argument 2 would have been the longer string `str2`

Reading the solution, the book points out

- The book solution implements what i'll call boolean trickery where I implement a counter
  - The boolean trickery is:
    - Define bool as `false`
    - Check conditional we care about
      - Check if bool is `true`
      - return false
    - Set bool to `true`
  - This makes it so the function returns false if the conditional we care about returns `true` TWICE
  - Essentially, makes it to where if we check differenceCounter > 1, return false but in a more elegant fashion
  - Full code boolean trickery snippet example:

```text
        bool foundDifference = false
        for(int i = 0; i < string1.length(); i++){
          if (string1[i] != string2[i]){
            if (foundDifference){
              return false
            }
            foundDifference = true
          }
        } 
```

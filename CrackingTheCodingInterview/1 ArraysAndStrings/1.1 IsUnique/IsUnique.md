# Is Unique

## Challenge Details

- Source: Chapter 1, Question 1, Page 90
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
  - Hints: #44, #117, #132
  - Solution: Page 192

## Challenge Commentary

### Initial Thoughts

- First thought is to use a hash table.
- This would result in O(N) time since we would need to iterate through each character to load the hashtable
  - Each key would be a unique character from the string and the value could be a count or a bool T/F (value doesn't really matter in this case)
  - If a duplicate character is found
    - Break the loop or return false to indicate the string has duplicate characters
    - For fun, we could have the hash table value be a count and when a duplicate character is encountered, add to the count and see how many characters were NOT unique by the resultant key value

- If we can't use additional data structures then we can't use a hashtable
  - In this case we could iterate through the each character (i) in the  string then have a nested loop to iterate over each character (j) in the string again and compare the values of i and j
    - This implementation would need to keep in mind the index to not compare the same index (i = 1 and j = 1)
      - We would skip every j[n] where n = i
  - This solution would result in O(n^2) which is not as favorable as the hash table solution
  
After searching for a unique string generator for python test case, my mind went to `a-z` characters and not `a-z0-9`. This is a mistake/overlook that does not impact this solution, however, it may impact further string solutions.

One further consideration is capitalized letters vs lowercase letters.

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\07\2024`\
**`Python3` Specific Notes:**
> Hashtables are dicts in python and for loops are structured differently where you don't define an index to iterate through (ex: `int i = 0; i <10; i++`)

### `C#` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `06\06\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- Clarify the character set between ASCII and unicode
  - I assumed unicode and failed to ask
- Take into account the size of the input string and return false if larger than X size
  - I failed this, which could have real world/true runtime impacts if the input string is over X size where duplicate characters 100% exist
- Use an array of booleans, representing each character, and break when a duplicate is found
  - This is a different implementation than mine, the time complexity is O(N), the space complexity if O(1)
  - Initially, i'd argue the book's is a much more sound solution due to O(1) space, however I challenge that the hashtable will also take O(1) space since it will only grow to the size of each unique character
    - In real world run time, it may often be smaller than the boolean array since the duplicate character may not always be at the end of the string
- For the non-additional data structure
  - My initial O(n^2) solution is perfectly reasonable
  - The book also points out we could sort the string first then perform an linear comparison
    - This solution could bring the time complexity down to O(nlogn) depending on the sorting algorithm used but sorting algorithms may come at extra space consumption
  - I like this solution as a more creative and less brute-force solution, it feels more in line with the spirit of the exercises and it challenges wanting to run with the initial "easy" solution of O(n^2)
    - Such thinking may be required, and will certainly help, with more elaborate/tough exercises in the future
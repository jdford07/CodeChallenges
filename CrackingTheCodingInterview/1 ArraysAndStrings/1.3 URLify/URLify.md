# URLify

## Challenge Details

- Source: Chapter 1, Question 3, Page 90
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Write a method to replace all spaces in a string with `%20`. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string.
    - Example:
      - Input: "Mr John Smith     ", 13
      - Output: "Mr%20John%20Smith"
  - Hints: #53, #118
  - Solution: Page 194

## Challenge Commentary

### Initial Thoughts

> Since we are given the true length of the string and told the string has sufficient space at the end to hold the additional characters, we should take an in-place approach\
>\
> To accomplish this:
> 
> - We should convert the string to an arrayList
>   - Since the string has enough space, we can use a normal array as dynamic resizing is not required
> - Then we should iterate over the array
>   - Any time a " " character is encountered we should:
>     - Replace the " " in the ith position with "%"
>     - Insert "2" in the ith + 1 position
>     - Insert "0" in the ith + 2 position
>     - Increment i to i + 3 so the newly inserted characters are skipped and we pick up with the next input string character

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\08\2024`\
**`Python3` Specific Notes:**
> Due to for loop structuring in Python, iterating over the array itself and skipping indices can be tricky. We'll need to define and use an external counter. In other languages we can simply iterate over the array itself and increment the iterator's value
>
> For this implementation, my mind went to using an auto-resizing array, I didn't want to have to menually create the extra space that is given in the solution description for each test string. Using an auto-resizing array could decrease time complexity to O(N^2) as it's O(N) nested inside the O(N) for loop.\
> If we assume the extra space in the input string is set to null or "", we don't need to perform any special operations on the resultant array to find the true terminal input string character and perform any push/pop operations on the array to insert any of the `%20` characters into the array\
> For the implementation itself, I converted the input string to a list then stored the length of the list into an iterable count variable\
> I then use the count iterable to iterate over the list to find any " " characters\
> Once a " " character is found, the ith index is replaced with "%", the ith+1 and ith+2 indices have "20" inserted and the iterable is incremented by 3 to skip over the newly inserted characters and resume iterating over the input string characters

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- My solution is quite a bit different and i'm not positive how far off I am since there's a bit of gray area in my answering of the question
  - The book iterates through the string from 0 to given true length, counting all spaces
    - These spaces are valid since we iterate through the true length of the string
  - Since there's extra space to account for the additional characters, we can create a new index at the true length + space count * 2
    - Space count * 2 is derived from replacing 1 character and inserting 2 more
  - An old index is defined as the true length and is used to iterated over the input string backwards
    - Because the new index includes space count * 2, there's a buffer between the old index j and the new index i
      - This means, when adding new characters inplace, no input string characters are overwritten
    - When a space is encountered
      - ith index is replaced with "0"
      - ith - 1 index is replaced with "2"
      - ith - 2 index is replaced with "%"
      - i is set to i=-3
    - When a non-space is encountered
      - jth character is copied to ith position
      - i is set to i=-1
- My solution assumes the expanded space is given as null characters and there is no consequence to overwriting thus no need to count the number of space characters
- Something I should keep in mind, is the book says it's common for string problems to iterate over the string backwards
  - This is not my initial inclination, and it should be at minimum considered moving forward
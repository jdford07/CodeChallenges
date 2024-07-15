# String Compression

## Challenge Details

- Source: Chapter 1, Question 6, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Implement a method to perform basic string compression using the count of repeated characters. For example, string aabcccccaaa would become a1b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
  - Hints: #92, #110
  - Solution: Page 201

## Challenge Commentary

### Initial Thoughts

> My first thought is we need to build a 2nd string while iterating over the first string then compare the lengths at the end and return the smaller of the input or built strings
>
> From the question, we know that only A-Za-z characters are allowed in the string which would cap any data structure at size 56
>
> Would going backwards benefit this usecase? I don't think so, it would be the same forwards as backwards since we only care about the repetitive count
>
> My approach can implement logic used in Q1.5 where I used a look ahead. In this exercise, I can use a look ahead to keep track of when the current char no longer repeats by comparing char[i] to char[i+1]
>
> Another approach could be to iterate over the string and store each character and count of occurence in a hashtable then iterate over the resultant hashtable and build a string of "keyValuekeyValue..."
>This approach actually wouldn't work since it would count all occurences not JUST the repetitive occurences, "aaabbbaaa" would break this approach

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N) maybe O(N^2)`\
**Completion Date:** `07\09\2024`\
**`Python3` Specific Notes:**
> My initial implementation contained variables that were assigned to str[i] and str[i+1] which made it harder to read/less clean. Also I forgot to initially convert the str into a char array and then when the str needs to be returned I forgot to "".join(str). These were remedied when running the code, which I can't do on a whiteboard
> 
> I had dupliate code but condensed it to 1 conditional by having proper ordering of checking the str[i+1] index. By checking if i==len(str) first, that will result in True and the str[i+1] won't be evaluated when the last index is encountered which means we can avoid the out of bounds exception
>
> The runtime may be O(N^2) since when the new string is built, it's being added to an existing array. On a smaller string, this would have a larger impact for the dynamically sizing array but on a larger string it would move to O(1) since the size would be changed less and less

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- Immediately one improvement is to use a string builder instead of appending to an existing string
  - Not sure if a string builder exists in python, potentially a library for it? It's built into Java and C languages
- The more optimal solution the book takes is to first count the size of the string if it were to be compressed first
  - This would cause an additional loop over the input string but
  - We can return the input string if it's smaller without wasting time/space building a new string
  - If the compressed string count will still be shorter, we then build the string with the StringBuilder
    - However, since we know the end size of the compressed string, we can initiliaze the StringBuilder to the appropriate size, saving on time complexity
      - This will cause the StringBuilder to NOT have to dynamically re-size
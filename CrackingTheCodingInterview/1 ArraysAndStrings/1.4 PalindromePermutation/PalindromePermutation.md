# Palindrome Permutation

## Challenge Details

- Source: Chapter 1, Question 4, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.
    - Example:
      - Input: Tact Coa
      - Output: True (permutations: "taco cat", "atco cta" etc.)
  - Hints: #106, #121, #134, #136
  - Solution: Page 196

## Challenge Commentary

### Initial Thoughts

> The wording, especially with the example is confusing me quite a bit. I believe we need to take the input string, find all palindrom permutatations of the string, if a palindrome permutation exists return True, if there are no possible palindrom permutations then return False.
>
> Returning after thinking through some of the logic below, we just need to determine if a palindrome is possible from the input string, the input string itself does not need to be a palindrome
>
> I think a false example would be strings where all characters are unique.\
> In a permutation, all but 1 character would need to have a factor of 2X the character. So in "palo altop" the "l" is single but all other characters have 2X so there are possible palindrome permutations
>
> A few things to note from the question:
>
> - Ignoring casing and non-letter characters
>   - This makes solving the exercise a bit easier and more straight forward as spaces can be ignored
> - Palindrome does not need to be limited to just dictionary words
>   - This also makes it a bit simpler as you don't need to perform any dictionary lookups AND you don't need to produce each and every permutation which can be costly
>
> The goal for this solution should be to not have to produce any permutations and focus on if more than 1 letter-character has only a single occurence
>
> - Going this route:
>   - We could copy each letter into a hash table
>     - Keep count of each letters occurence
>     - Return false if:
>       - More than 1 letter has count = 1 (0 or 1 letters with count = 1 is acceptable)
>       - More than 1 letter's count is not a factor of 2
>       - This can be achieved by iterating over the hashtable's values and taking %2, if %2 != 0 more than 1 time, return false
>     - This solution would take less time (O(N)) but would be less space efficient as the hashtable would be O(charset)
>       - However, thinking about it, the hashtable size would be capped at total number of unique letters
>   - We could sort the string
>     - Count occurences of character
>     - Perform a look ahead to reset count when a new character is next
>     - Keep a flag where if any of the counts % 2 return 1 (or not 0) more than once, return false
>     - This solution would take longer as the string needs to be sorted, however space complexity is optimal since no additional space is required

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\08\2024`\
**`Python3` Specific Notes:**
> 

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- My solution was correct
- The only thing I could have done better would be to have implemented a way to check if the string values were letters A-Z
  - Since the question said to ignore those, I took that as I didn't need to check for them then ignore them in the code itself
- The created a solution using a bit vector and bit math
  - I'm out of my league on this and would need further studying/practice
# Check Permutations

## Challenge Details

- Source: Chapter 1, Question 2, Page 90
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Given two strings, write a method to decide if one is a permutation of the other.
  - Hints: #1, #84, #122, #131
  - Solution: Page 193

## Challenge Commentary

### Initial Thoughts

Initially, I want to question if the characters are ASCII or unicode, however i'm only asking to get in the habit of it since in Q1.1, I failed to ask. With the inherent comparison, i'm not sure asking is required or would get me anywhere.

Thinking out loud, in order to be a permutation, each string must be of equal length, contain the exact same characters and each character must have the same count. Example: `abc` = `bac`, `cba`

My first thought is to use a hashtable and keep count of each unique character's occurence. However, that seems overly complex and you would need to keep track of the values which could increase runtime/unnecessary work.

My second thought is an O(n^2) solution where:

- We loop over the first string, i
  - O(N) time
- Loop over the second string, j
  - Compare i == j and go until a match is found

This solution falls flat with duplicate characters where `bbac` = `bac` would return true

My third thought is, thinking about the sorting solution from Q1.1

- We can sort each string
- Then compare the 2 sorted strings and determine if the match.
- This would take at worst O(nlogn) time complexity depending on the sorting algorithm used.
  - I need to brush up on my sorting algorithms and implementations before I can definitively choose one.
  - In the implementation languages I could just use already created sorting methods, however that defeats the purpose of the exercises
    - As a note, the solutions contain the use of already created sorting methods, therefor I will but I will note which sorting algorithm would be my choice and share that with the interviewer if asked
  - I'm leaning towards bubble sort before doing any research
    - This was the wrong decision
  - The best sorting algorithm for strings is either radix sort or bucket sort

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\07\2024`\
**`Python3` Specific Notes:**
> In order to specifically sort a string alphabetically you must pass the string into the sorted() method then join on a null "" character: `"".join(sorted(string))`\
> \
> This solution is rather straight forward once you recognize sorting alphabetically is a viable solution. Pass each string to the language specific sorting function then compare the results to return a T/F bool

### `C#` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `06\06\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the book solution:

- I should have stuck with my initial proposal as that is shown to be CLOSE to the more optimal solution between thoughts 1 and 2
  - I swayed myself off of the 1st solution as it felt too complicated
  - The book implementation initialized an array of all ASCII characters then took a count of each occurence in the first string
    - My solution would not have done this and I would have iterated over the array/hashtable to check if all count values were 0 which would increase real world run time but have the effective same O() on paper as it wouldn't be nested and the solution wouldn't have been quicker than O(N)
- The solution I went with (2), ended up still being viable
  - This solution takes into account a more creative thought process, to me, where sorting the array did not come to me as my first thought
    - This creative thinking can be more beneficial in later/more indepth exercises
    - I find more value in this way of thinking as it feels more out-of-the-box which I believe can help in striving to eliminate all non-optimal solutions and overall finding the most optimal solution
  
# Template

## Challenge Details

- Source: Chapter 3, Question 1, Page 98
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Describe how you could use a single array to implement three stacks
  - Hints: #2, #12, #38, #58
  - Solution: Page 227

## Challenge Commentary

### Initial Thoughts

> I don't fully understand what the question is asking. Is it asking for me to figure out if a single array can be represented in a stack 3 unique ways? Forward, Reverse, Split? 
> 
> Reading the solution because I couldn't call up the author to clarify, the question is asking how can you split up an array into 3 separate stacks
>
> The brute force and first thought I have is take the length of the array and split it into 3 pieces. Put each piece into its own stack:
>
> - Array length: 10
>   - Stack 1: 0 - 3
>   - Stack 2: 4 - 6
>   - Stack 3: 7 - 10
> - Array length: 1
>   - Stack 1: 0
>   - Stack 2: None
>   - Stack 3: None
>
> A different approach would be to have the user determine how many elements to put into each stack. In that instance you'd keep a count of how many elements have been inserted into each stack then move to the next stack once X amount of elements have been inserted

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O()`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> Because I created my own stack class I thought to instantiate 3 stacks, iterate through the given array and place the elements of the array into each stack.
>
> - Stack 1: index inclusive 0 to less than n/3
> - Stack 2: index inclusive n/3 to less than 2/3
> - Stack 3: index less than or equal to n

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

I struggled the most with properly splitting a given array into 3 but that was because I couldn't figure out the cascading for the if statements. I kept trying to do [0,n/3), [2n/3, 2n/3), [2n/3, n) when it should have been [0,n/3), [n/3, 2n/3), [2n/3, n). The question of pushing the elements wasn't ever an issue, just splitting the array into 3 to account for all edge cases

Reading the solution, the book points out

- I had to reference the solution before implementing my own solution because I didn't understand the question
- The book implements a whole class where as I use my pre-implemented class and use a function to split a given array into 3 stacks
  - Her solution is more modular as it's encompassed all in one class
  - Her solution also uses lists to keep track of the stack values as opposed to a linked list
  - If I was restricted to implementing a singular class I would have followed her approach
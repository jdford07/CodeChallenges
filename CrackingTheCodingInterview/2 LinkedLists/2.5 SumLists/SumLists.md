# Sum Lists

## Challenge Details

- Source: Chapter 2, Question 5, Page 95
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - You have wo numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. (You are not allowed to "cheat" and just convert the linked list to an integer)
  - EXAMPLE:
    - Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
    - Output: (2 -> 1 -> 9). That is, 912.
  - FOLLOW UP:
    - Suppose the digits are stored in forard order. Repeat the above problem
    - EXAMPLE:
      - Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617+295
      - Output: (9 -> 1 -> 2). That is, 912
  - Hints: #7, #30, #71, #95, #109
  - Solution: Page 214

## Challenge Commentary

### Initial Thoughts

> Initial thought is we can iterate through each list simulataneously. First question, will the 2nd linked list always be smaller than the first? If so, we can step through the first linked list. If not, we would spend effort finding the larger of the 2, node wise. 
>
> While positively iterating, we can add the 2 Nodes together. We can store the result in the first linked list node (to avoid creating new nodes). If the result is >9 we can set a carry variable and add the carry variable with the next 2 nodes. The stored result of >9 would be the result of % 10
>
> Another question is, will the resultant added number have the same number of Nodes as the longest linked list? If not, a new node would need to be added to the linked list tail

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O()`\
**Completion Date:** `07\13\2024`\
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

-
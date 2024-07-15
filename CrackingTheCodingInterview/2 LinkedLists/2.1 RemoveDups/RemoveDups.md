# Remove Dups

## Challenge Details

- Source: Chapter 2, Question 1, Page 94
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Write code to remove duplicates from an unsorted linked list.
    - FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
  - Hints: #9, #40
  - Solution: Page 208

## Challenge Commentary

### Initial Thoughts

> Initially, I want to iterate through the linked list and put any unique values in a hashtable. Each iteration can check the hashtable if the value exists. If the value is in the hashtable, remove the linked list node
>
> First question, is this a singly or doubly linked list? I don't think it matters since we only care to go one way but if it's singly, we can only interate positively
>
> The question points out that the linked list is unsorted, with my initial approach, I don't think it being sorted or unsorted matters. Spending time sorting the list seems like a waste.
>
> For the FOLLOW UP, i'm not sure what a temporary buffer would be used for in the initial solve. This may mean my initial solution is not optimal. Potentially the buffer is used as a lookahead to determine if the current node's value exists in the later nodes

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O()`\
**Completion Date:** `07\14\2024`\
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
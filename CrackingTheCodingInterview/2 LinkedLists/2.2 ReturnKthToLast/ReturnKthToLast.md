# Return Kth to Last

## Challenge Details

- Source: Chapter 2, Question 2, Page 94
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Implement an algorithm to find the kth to last element of a singly linked list
  - Hints: #8, #25, #41, #67, #126
  - Solution: Page 209

## Challenge Commentary

### Initial Thoughts

> My first thought is to create a count variable, iterate over the linked list and increment the count variable for each Node encountered
>
> We can then compare the k input with the count. If count - k < 0 then return False else, return kth to last Node
>
> For iterating over the List, to return to the kth to last node, there are a few options I can think of:
>
> - Using the count variable from the first iteration that took O(N) time
>   - We iterate to count - k Node and return Node
>   - This would still be O(N + N), however it would be O(N) space
> - While iterating over the initial linked list, we create a 2nd linked list that maps the reverse of the input linked list
>   - This would essentially be creating a doubly linked list but with 2 singly linked lists
>   - We then iterate over the 2nd linked list K times
>   - Worst case this is still O(N + N) time but O(N+N) space
> - We could get whacky and defeat the purpse of using a linked list by implementing a hashtable
>   - We iterate over the linked list, storing each Node for each position of the linked list
>   - To find kth to last element we then reference the hashtable at kth to last hashtable entry
>   - This would be O(N+N) space and O(N) time, however grabbing the Node from the hashtable would be O(1)

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O()`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> Kth to last means the last element is index 0 and we want to find K indices from 0
>
> So if we have a list[1,2,3,4,5], the list[last] == 5. Thinking reverse, reverseList[0] == 5. If we wanted 3rd from the last, it would really be reverseList[3] == 2 starting from reverseList[0] == 5

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

My solution was quickly regarded as one that would be unintended by the interviewer, assuming we were given the linked list the length. The problem would become trivial, which  by iterating through the list I made the problem trivial. 

Reading the solution, the book points out

- Recursion should be employed to find the cleanest solution, multiple options were given
  - fd
- One non recursive option was given that I never thought of, and challenged by immediate way of thinking
  - Use 2 pointers, p1 and p2
    - p1 is k spots into the linked list
    - p2 is at the 0th spot of the linked list
    - Step them through the list at the same rate (+1 each step)
    - When p1 is at the end of the array, p2 is at the LENGTH - k spot
    - return p2 node as it's kth from the last spot
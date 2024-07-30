# Stack Min

## Challenge Details

- Source: Chapter 3, Question 2, Page 99
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time
  - Hints: #27, #59, #78
  - Solution: Page 232

## Challenge Commentary

### Initial Thoughts

> My first thought is to add an object attribute that contains the minimum value and then change the value to the lowest that gets pushed. However, what do you do if you pop the lowest value and there's still nodes in the stack?
>
> I think the best is in addition to the stack.top we create a stack.min attribute where min is a nested stack. For the nested min stack, we push to it if the currently pushed node.data is <= stack.min.top.data. This will store a sub stack that contains the lowest of the remaining nodes in the main stack. When the min.top is popped from the main stack, we will also pop from the min stack.
>
> Main Stack: 9->8->10->4->10->5->20
> Min Stack: 4->5->20

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
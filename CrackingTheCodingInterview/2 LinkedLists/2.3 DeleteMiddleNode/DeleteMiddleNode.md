# Delete Middle Node

## Challenge Details

- Source: Chapter 2, Question 3, Page 94
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis Implement an aglorithm to delete a node in the middle (i.e any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node
  - EXAMPLE
    - Input: the node c from the linked list a -> b -> c -> d -> e -> f
    - Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
  - Hints: #72
  - Solution: Page 211

## Challenge Commentary

### Initial Thoughts

> Initially, we are constrained to using a singly linked list from the question itself. This would be easy and straight forward if we were able to use a doubly linked list as we'd have access to the previous node through the current nodes prev value.
>
> The tricky part is we can't access the previous node, it's not possible since we're only given access to the current node and the current node only. It's tempting to remove the node itself but that's not the solution. 
>
> I looked at the solution to clarify access the meaning of "given only access to that node" and read the word "Copy". This was a major tip in finding a correct solution. Thinking it through, my solution is:
>
> - Find which node contains the input value
>   - We need to check to make sure the node isn't the head or tail of the linked list
> - From the current node, access the next node's data value
> _ Copy the next node's data over the current node's data value
> - Move positively through the linked list, moving each next node's value to the current node's value
> - When the final node is reached, remove the entire final node from the list
>   - If we don't remove the entire final node from the list, the final node and the final node - 1 will have duplicate values
>
> Other considerations when building the solution
>
> - Do we need to be concerned with duplicate values in the list?
>   - If so, we can handle duplicates by removing all duplicates that aren't in the head or tail position
>   - We can perform a check during the copying of the data to make sure the data doesn't contain the input value
>   - I don't think we need to handle removing duplicates since the question specifies removing A node from the list, not multiple nodes
>     - Removing multiple would increase the complexity and most likely the solution approach of having to handle multiple nodes

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
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

- I overcomplicated my solution by copying data from all successing nodes instead of only the next node
- The book takes the node to delete, copies the entire next node on top of the node to delete, then deletes the next node
  - This does what my solution does however, this recognizes you only need to delete copy data from the next node
  - Whereas I copy data from all successing nodes, resulting in a longer run time and performing unnecessary work
    - I also rely on finding the end of the list and removing the resultant 'dead'/'duplicated' node
  - I think this is one of the only optimizations I can make to my solution
- One overall note is the book solution is only a function instead of a fully functional code block so the solution looks simpler as it's expecting the node to remove as input whereas my solution finds the node to remove first
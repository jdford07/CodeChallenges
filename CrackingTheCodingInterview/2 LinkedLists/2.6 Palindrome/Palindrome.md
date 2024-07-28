# Palindrome

## Challenge Details

- Source: Chapter 2, Question 6, Page 95
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Implement a function to check if a linked list is a palindrome
  - Hints: #5, #13, #29, # 61, #101
  - Solution: Page 217

## Challenge Commentary

### Initial Thoughts

> In the spirit of the challenge I should avoid using other data structures. A palindrome is a series of characters that is the same forwards as it is backwards
>
> This solution would be simple if I could use a hashtable (exactly as in 1.4) or a stack (to push and pop characters)
>
> You can't use 2 variables, one set to the head and one set to the tail. Then iterate the head positively and the tail negatively, comparing each node.data until they meet. This is not feasible because you can't simply negatively iterate through a singly linked list (unless using recursion)
>
> We could possibly:
>
> - Iterate to the tail node recursively
>   - Thinking it through, there's no way to exit out of recursion early so we could go from node at spot Length/2 to tail and recurse from there
>   - Although, if the linked list is a palindrome, the comparison should never fail. It's just that we would be doing N/2 extra work since we really only need to compare the first half to the 2nd half. If we didn't go from Length/2 to tail, we would be comparing every node.
> - Return tail node recursively
> - While recursing, positively iterate through the head of the list
>   - Compare node.data of each until the nodes meet in the middle
>
> A non-recursive and easy solution would be to simply:
>
> - Reverse the input linked list into a 2nd linked list
> - Step through both lists
>   - Compare each node.data
>   - Return False early if !==
>   - Return True if ==

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

Overall, I considered almost everything there was to consider with this problem. A few minute implementation details such as recognizing N/2 would be more real-time efficient but not implementing it in the actual code solution. 

Reading the solution, the book points out

- My recursive solution is slightly different than the book one
  - We both implement a class to handle returning the Node and the comparison value
  - Her recursion starts at node N/2 and iterates through to the tail
  - My recursion starts at the tail and negatively iterates to the head
    - Her solution takes account of only needing to compare the 2 halves whereas mine compares the entire list
- A solution I didn't FULLY consider is the slow/fast runner approach
  - I DID consider the stack implementation but I would have found the middle node differently than her
    - She found the middle node using a slow runner and a fast runner increasing at 2x the slow runner
      - When the fast runner reaches the end, the slow runner is at the middle node
      - You can then compare the stack top to the 2nd half of the nodes
        - Popping from the stack for each true comparison
  - I would have found the middle node by simply counting the length then iterating to it
- The reverse and compare approach was the same as mine
  - I would use this approach in an interview
- The recursive approach was a nice exercise but I'm not confident enough yet to be able to implement that on the fly in a timed interview
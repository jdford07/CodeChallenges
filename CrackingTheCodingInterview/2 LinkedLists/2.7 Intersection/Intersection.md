# Intersection

## Challenge Details

- Source: Chapter 2, Question 7, Page 95
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting
  - Hints: #20, #45, #55, #65, #76, #93, #111, #120, #129
  - Solution: Page 221

## Challenge Commentary

### Initial Thoughts

> First think that jumps out is we don't care about value, we only care about memory location so any comparison will be done with node == node NOT node.data == node.data
>
> One clarification point is, in the linked list, does each index contain a unique node? It's possible there could be a circle linked list implementation. Coming back, I misread, we only need to return the Node and NOT the intersecting position. Therefore, if the linked list is circular one it doesn't matter
>
> The brute force solution I think is:
>
> - Iterate over list 1
>   - Nested iteration over list 2
>   - Compare list 1 node to list 2 node
>   - If equal return Node
>
> The above solution is not efficient as it would be O(N^2) run time.
>
> This next approach seems to skirt the challenge but, you could:
>
> - Create a hashtable
>   - Iterate over first linked list, placing each node as key with their positions as value
>   - Iterate over second list, check if current node exists in hashtable
>     - If exists, return Node
>     - Else, keep iterating
>
> I knew there was a solution that was better than O(N^2) but nothing apparent screamed to me. I consulted the hints and hint #65 pointed out that if the lists intersect, the tail nodes will be the same. I did not think of or consider this. This helps in determining if the 2 lists intersect, however we still need to find the intersecting node
>
> Using hint #65 we could solve this recursively:
>
> - Find lengths of both lists, pad shorter list with empty nodes to make both lists equal in length
> - Iterate to tail of list 1
> - Iterate to tail of list 2
> - Create a wrapper than contains the most recent Node that was equal between the 2 lists
> - Recurse negatively through both lists comparing the nodes
>   - The last node to be equal between the 2 lists will be the intersecting node
>
> After thinking how to construct an intersecting linked list for testing the solution, we're really checking to see if one list is inside of another list.

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> I implemented what was described referencing hint #65

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- I used recursion when it wasn't necessary 
  - Most likely made it overly complex and certainly made it unable to exit early in the event of no intersection
- She chops off the longer of the 2 lists front nodes by advancing the longer list head pointer (longer - shorter) nodes
  - I pad the shorter with 0s at the front
  - I think both achieve the same result as you need to find the length of both lists first and you're still comparing the nodes which will always be different until the intersecting node
  - Padding with 0s makes the realtime solution longer by ensuring O(N) which isn't ideal
- She iterates to the tails of both lists and exits early if the final nodes of each list are not equal
  - My approach does not allow for exiting early
- Conceptually, I think her approach makes more sense and is easier to read simply because recursion can be a bit confusing
- At the core of my solution, it isn't wildly different of wildly more ineffecient however I do extra work that isn't required
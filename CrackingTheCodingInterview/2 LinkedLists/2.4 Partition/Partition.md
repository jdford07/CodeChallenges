# Partition

## Challenge Details

- Source: Chapter 2, Question 4, Page 94
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions. The additonal spacing in the example below indicates the partition. Yes, the output below is one of many valid outputs)
  - EXAMPLE:
    - Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
    - Output: 3 -> 1 -> 2   ->  10 -> 5 -> 5 -> 8
  - Hints: #3, #24
  - Solution: Page 212

## Challenge Commentary

### Initial Thoughts

> We can assume the input linked list will not be sorted and from the question, the resultant linked list does NOT need to be sorted around the partition. This helps with reducing complexity as we can simply insert left or right of the partition number. We can also assume the partition value will appear more than once and the multiple node needs to be put on the right side of the partition. We can also assume we're working with a singly linked list although the question doesn't specify. Something we should clarify is if the input value X is present in the linked list or not.
>
> Something from the example I noticed is the partition is taking place around the input partition values index in the linked list and not the value itself. My initial thinking and expectation was the partition value would always be around the partition value irrespective of its index. I could be over analyzing and overcomplicating.
>
> If we were to work with a doubly linked list the solution would change since we have access to forward and reverse iteration
>
> I'd like to create a new singly linked where the head is the partition node then create 2 functions. One function to insert to the left and one functoin to insert to the right. Each function would find the partition node before inserting. This would result in O(N) for finding and O(1) for insertion.
>
> There is another potential solution working with a singly linked list where we iterate through the linked list, find the partition node then iterate through the linked list again and rearrange the nodes. However, I think this would be O(N^2) for the 2nd iteration, however if we find the partition node and store it we may be able to have a non-nested loop and get away with O(N)
>
> I think the proper solution would be to make use of the advantage of using a linked list: the nodes are easily movable. I think my current thinking lends itself to solving this as if the input was an array, where indices are not easily moved
>
> I think the final solution is to:
> - Iterate through the list:
>   - Find and store the partition node
>   - Store the partiton node - 1 (if the partition node is not the head)
> _ Iterate through the list again:
>   - Compare each node to the partition node (skip the partition node)
>   - If current node less than partition node, 
>     - Insert the current node to the left of the partition node
>     - Update prev node to current node
>   - If current node greater than or equal to partition node
>     - Insert the current node to the right of the partition node
>
> Another potential solution is to iterate through the linked list to find the final node and store it. We could then iterate through the linked list and if the node is greater than or equal to X we move the node to the tail. This leaves all lesser nodes intact and we don't need to worry about the partition value being in the linked list

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> Of the multiple solutions I could have used, I went with an in-place re-arrangement approach:
>
> - Iterate through the linked list to find the tail node and keep a count of how large the linked list
>   - Use a while loop to iterate
> - Iterate through the linked list length (with a for loop):
>   - Use a for loop with the linked list length so we can avoid getting into an infinite loop using a while loop
>     - An infinite loop is possible since all tail node values would be >= partition. If we checked for currentnode.next, we would endlessly shuffle >= values at the tail instead of exiting
>   - Keep a variable containing the previous node for when a node is moved
>   - Compare each node value to the partition value
>   - If the node value is >= partition value:
>     - Move the current node to the tail
>       - Set tailNode.next to None (this avoids creating a looped list)
>     - Update the prev node
>       - If prevNode is null (current node is the head), update the head to the next node
>       - If prevNode is not null, set prevNode.next to currentNode.next
>     - Move currentNode to currentNode.next (to continure forward iteration through list)
>   - If the node value is < partition value:
>     - Update prevNode to currentNode
>     - Update currentNode to currentNode.next

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Initially I assumed the partition value would be a node inside the linked list. This was wrong and i'm glad the solution I implemented took the approach of assuming the partition value was not a present node.

Overall, I think my solution is pretty good as it's O(N). The in-place re-arrangement is probably more akin to array reorder thinking. Thinking about space complexity, since each Node takes up space, creating a new Linked List doesn't take additional space (UNLESS WE CREATE NEW NODES). I failed to consider that and caught myself thinking creating an additional linked list would take up more space, when that isn't the case. Recognizing this sooner I may have gone with using additional linked lists in the solution instead of doing something inplace.

I think the inplace solution is more out of the box and probably unnecessary but overall it's an acceptable solution.

Reading the solution, the book points out

- There are multiple different solutions, the 2 outlined make me laugh as they were some of my first thoughts but I decided there were better ways
  - The book's first solution creates 2 new linked lists, one contains all values less than X and one contains all values greater than X
    - I don't particularly like this solution since it can be tricky to keep track of 2 separate linked lists especially since it's not entirely necessary
    - I think this solution is easier from an approach perspective and feels like more brute-forcy
  - The book's 2nd solution is similar to my very initial inclination of creating 1 new linked list
    - The implementation would add >= values to the tail and < values to the head of the linked list
      - My implementation would have been different but it was also dependant on the partition value being a node in the list
      - Assuming the partition value would not be a present node, I would have changed my implementation but not sure I would have gotten to the book's exact implementation
- 
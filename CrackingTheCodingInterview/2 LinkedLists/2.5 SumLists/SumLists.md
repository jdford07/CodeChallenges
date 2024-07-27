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
>
> For the FOLLOW-UP:
>
> I think the simplest solution is to reverse the list such that the numbers are stored in the reverse order.
>
> To reverse the linked list we can:
>
> - Instantiate a list length variable
> - Iterate to the tail and count all of the nodes
> - Remove the tail node
> - Append the removed tail node to the head of the linked list
> - Iterate to the tail node and repeat previous 2 steps until each node has been reversed
>
> I think the, bad, run time would be O((N-1)! + N) since we need to continually reach the tail node
>
> We can't simply iterate through the forward linked lists positively because if you have 4999 + 2999 the result would be 7998 ((4+2+1), (9+9+1), (9+9+1), (9+9)). It would be impossible with a singly linked list to effectively look more than 1 node back to handle carrying the overflow 1.
>
> Unless, we did 1 pass through the lists and stored the addition result in the first linked list node. Then performed a 2nd pass, where the carry is handled by checking the currentNode.next.data value. We can do this because there's no limit on the node.Data that requires the stored digit be singular, only that the returned node.data value is singular. This would be O(2N) which is much better than O((N-1)!+N)
>
> Revisiting the reversal of a singly linked list, the above is overly complicated. You can simply iterate through the linked list positively, create a new linked list and insert each node at the head of the new linked list to reverse the original linked list which would be an O(N) time and splace complexity. O(N) time for the iteration and O(N) space since no new nodes were created
>
> To effectively solve the follow-up without reversing the list, since the 2 pass outlined above is not valid, you need to use recursion as it gives you the ability to go to the tail node then from the tail back to the head node. During the going back to the head node from the tail, you can add the carry appropriately

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\23\2024`\
**`Python3` Specific Notes:**
> Both implementations assume that appending an additional node would ***not*** be required
>
> For the initial question:
>
> - We assume:
>   - The first number linked list will always be larger than the second number linked list
>     - If we can't assume this, we could iterate through each list and find the longest one before performing place addition
>   - Each number is positive
> - To solve:
>   - We iterate through the larger of the 2 number linked lists starting at each linked lists head nodes
>   - We assign a carry variable
>     - The carry flag represents a 1 needs to be added in the following place
>     - Initially set to False
>   - We assign a numResult variable
>     - Set to 0 if the carry flag is False
>     - Set to 1 if the carry flag is True
>   - For each node we add the 2 linked list data values together
>     - If the result is > 9, we assign a carry flag to true
>       - We take the % 10 of the addition and place the result in the first linked list node, overwriting the previous value
>     - If the result is < 9
>       - We place the result in the first linked list node, overwriting the previous value
>   - Before iterating to the next node, we check if the second linked list's next node is valid
>     - If it's not, we set the current node.data to 0
>       - This prevents us from having to create dummy nodes for the length of first linked list
>     - If it is, we move to the next node
> For the FOLLOWUP:
> - Refer to book solution

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- The more optimal initial solution uses recursion
  - Overall I should try to use recursion more as I didn't even consider a recursive solution
  - My solution is similar in approach but does not use recursion
- For the follow-up, I did NOT pad the smaller linked list with 0's when I should have
  - I had considered this for the initial question by thoughtfully choosing not to append 0's to the smaller list
  - For the follow-up arithmetic, the padded 0s are crucial as you can't overwrite the value of node as I do in the initial question
- Both solutions create a new node when needed, I considered this but did not implement it since it felt unecessary and I would question the interviewer if it was required beyond verbally considering
- For the follow-up, the solution is completely different from mine
  - She implemented a class to keep track of the node and if a carry is required
    - This elemenates my necessity to iterate over the list a 2nd time
  - She created a new list and inserted each node at the head
    - I did the addition inplace
- Overall, my inplace arithmetic doesn't take advantage of the movability linked list nodes have as it's completely unecessary to do something in-place with a linked list
  - The approach is too focused on arrays/lists
- For the follow-up solution, I read the book solution after failing to implement my own recursive solution
  - I got tripped up on handling the wrapper class for the carry
  - The recursion itself wasn't too difficult to conceptualize/implement but the carry class was
  - In an interview, I would reverse the list and be done with it
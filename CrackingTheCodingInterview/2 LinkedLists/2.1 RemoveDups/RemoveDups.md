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
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\18\2024`\
**`Python3` Specific Notes:**
> I created a library (LinkedListLib) to initialize a custom singly linked list for solution testing.
>
> To solve removing dups, I first create a set to hold all unique characters encountered. Then, I initialize a currentNode variable set to the input Linked Lists head. Lastly, I need to keep track of the previous node, so I initialize a prevNode variable set to 'None'. The prevNode variable will be set to the currentNode-1 when iterating through the input linked list
> 
> I use a while loop to iterate over the linked list, escaping when the currentNode is 'None'
> 
> When a unique char is found:
> - The char gets added to the set
> - prevNode is set to currentNode
> - currentNode is set to currentNode.next (this specifically continues the iteration)
>
> When a duplicate char is found:
> - The prevNode.Next is set to currentNode.next
>   - This skips the currentNode by changing the prevNode.next from the currentNode to the next node's memory location
>   - In a lower level language, the Node memory would be cleaned up at the same time

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

My solution is the exact same as the book's solution. 

The solution for not using a buffer is referencing the inability to use a hashtable/set

Reading the solution, the book points out

- Use the 'runner' technique to iterate over the linked list 
  - This uses a currentNode and then a runnerNode
  - You iterate over the linkedList as you normally would, however
    - For each currentNode.data,
      - use the runnerNode to iterate over all following Nodes, comparing currentNode.data to runnerNode.data
      - If the currentNode.data == runnerNode.data, remove the runnerNode and continue iterating
  - This solution results in O(N^2) since you have to iterate over the linked list twice, however it's O(1) space complexity
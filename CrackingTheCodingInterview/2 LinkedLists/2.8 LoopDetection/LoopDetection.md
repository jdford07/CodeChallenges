# Loop Detection

## Challenge Details

- Source: Chapter 2, Question 8, Page 95
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists).
    - EXAMPLE:
      - Input : A -> B -> C -> D -> E -> C [the same C as earlier]
      - Output: C
  - Hints: #50, #69, #83, #90
  - Solution: Page 223

## Challenge Commentary

### Initial Thoughts

> From the question there are a couple things that are clear:
> 
> 1. The input list may NOT have a loop
> 2. We can easily get ourselves into an infinite loop by referencing Node.next if a loop does exist
> 3. We're comparing the Nodes themselves, not Node.data
>
> My first thought is to iterate through the list storing each unique Node in a hashtable and checking if the currentNode exists in the hashtable. This solution feels like it skirts the challenge however.
>
> In the past problems, when using recursion we reach the end of the linked list then start to recurse out. If we took that approach we'd get into an infinite loop as there's no end to a circular list
>
> You could copy the linked list to a new linked list and for each insertion you can check if the node to be inserted exists in the newly made linked list. I believe this would be O(N^2) which would be not good.
>
> I couldn't come up with a solution using recursion or the runner technique on my own. So I consulted the hints. The hints make it clear that using the runner technique is the way to solve the challenge. I'm still having trouble visualizing how the first pointer will always collide with the second pointer.
>
> In the runner technique you assign a slow and fast pointer. The fast pointer moves 2 nodes for every 1 node the slow pointer moves. 
>
> Why, if a loop exists, will they eventually collide?
>
> They eventually collide because the slow pointer goes over every node
>
> The fast pointer goes over every even node but will switch to every odd node depending on the loopback node
>
> EXAMPLE:
>
> - List = 1->2->3->4->5->6->7->8->9->10->?
>   - ? = 1
>     - Slow = 1->2->3->4->5 ->6->7->8->9->10->1
>     - Fast = 1->3->5->7->9->1->3->5->7->9->1
>     - Collision = 1, Fast = 1, Slow = 1
>   - ? = 2
>     - Slow = 1->2->3->4->5 ->6->7->8->9->10
>     - Fast = 1->3->5->7->9->2->4->6->8->10
>     - Collision = 10, Fast = 10, Slow = 1
>       - 10 -> 2
>       - 1 -> 2
>   - ? = 3
>     - Slow = 1->2->3->4->5 ->6->7->8->9
>     - Fast = 1->3->5->7->9->3->5->7->9
>     - Collision = 9, Fast = 9, Slow = 1
>       - 9->10->3
>       - 1->2->3
>
> Now, 2 challenging pieces remains: How to determine if a loop exists and how do we get to the first loop node? If a loop doesn't exist then we would get caught in an infinite loop if we niavely implemented just the runner technique.
>
> I couldn't figure out the logic so I read the solution. I would not have figured out the solution on my own.
>
> The solution is as follows:
>
> - Create a slow pointer set to list.head
> - Create a fast pointer set to list.head
> - Iterte through the linked list until they are equal or until fast is null
>   - Slow is iterated 1 place slow.next, fast is iterated 2 places fast.next.next
>   - If fast is null, there is no loop
> - When they are equal, keep fast pointer at collision spot
> - Set slow pointer to list.head
> - Iterate through list until both pointers are equal, return collision spot node
>   - Slow and fast are BOTH iterated 1 place until collision

### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N)`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> Things to remember for this implementation:
>
> - Runner technique: slow and fast both start at list.head
>   - Iterate slow by 1 place
>   - Iterate fast by 2 places
> - If a loop exists, the fast will never be null
> - If a loop exists, the slow and fast will eventually collide
> - If a loop exists:
>   - The head of the list and the collision node will be the SAME steps away from the start of the loop
> 

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

Reading the solution, the book points out

- I was completely off base and was not able to appropriately implement the runner technique
- The solution was a bit more math involved in order to determine that the slow and fast would eventually collide AND that the head and collision point are the same X nodes away from the loop start
  - I would not have ever figured this out on my own
- In an interview, I most likely would have tried to use a hashtable
  - If this would not have been allowed, I would have been screwed
- This solution is pointed out to be common for solving if a loop exists in a linked list
  - If we only care that a loop exists, we can implement the runner technique
  - If we care about the start, we need to involve keeping the collision node and setting the slow pointer to the list.head
# Rotate Matrix

## Challenge Details

- Source: Chapter 1, Question 7, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Given an image represented by an N x N matrix, where each pizel in the image is represented by and integer, write a method to rotate the image by 90 degrees. Can you do this in place?
  - Hints: #51, #100
  - Solution: Page 203

## Challenge Commentary

### Initial Thoughts

> "Oh shit"
>
> This is not only out of my comfort zone, but also an area i'm less practiced in and can have a hard time visualizing a programmatic solution
>
> First thing we can do it think about what the input data structure would look like
>
> - An N x N matrix
>   - We know each column and row will be the same size (size N)
>   - The input would be a parent array housing smaller array's
>     - Each parent array's index is an array representing a matrix row
>     - Each matrix column is then the ith index of each row
>   - input = [[1,2,3], [4,5,6], [7,8,9]]
>     - [1,2,3]
>     - [4,5,6]
>     - [7,8,9]
>   - This input example is intentionally small so as to not overwhelm myself when finding the brute-force, non-inplace solution
>
> Next, we think about what it means to rotate something by 90 degrees
> 
> - Each row becomes a column
> - Each column becomes a row
> It makes sense to me, to iterate through the input in reverse order. So we take the last row and make it the first column. We will still need to spend time complexity to find the last row but from there we can iterate positively to fill out each column
>   - We could take the first row and make it the last column, however, I don't see this as any better since we would still need to spend time complexity finding the Nth index
>
> For implementation, we will create a 2nd, empty array. We could find the size of the input array then create the 2nd array to-size OR we could create an empty 2nd arrayList and have it dynamically resize. The more time efficient solution would be to find the size of the input array, and create the 2nd array to-size.
>
> With the 2nd array created
>
> - Instantiate a count variable to represent the current column
> - Negatively loop through the input array
> - Positivley loop through the nested array at each input arrays index
>   - Move each nested input array's index value to the current column position in each nested 2nd array's index
>     - input[i[j]] = 2nd[i[currColumn]]
>   - We move positively over the 2nd array's indices
> 
### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(N^2)`\
**Completion Date:** `07\13\2024`\
**`Python3` Specific Notes:**
> For the brute force: I got a solution to be O (N+N^2) -> O(N^2)
>
> I implemented what was laid out in the initial thoughts section. I had to figure out the syntax for decrementing a for loop with range to be range(sizeOfInput, 0, -1) and then also instantiating an array of fixed size to be arr = [None]*size
>
> I overlooked that the outer for loop, when decrementing, would have an index of 1 larger than the input array size and had to correct array value retrieval from arry[i][j] to array[i-1][j]
>
> Overall, with instantiating a 2nd array, the solution works and i'm pleased to have found an implementation for what was initially a very daunting exercise
>
> For the in-place: I was not able to piece together the proper counting of N-1 when going 1 layer deeper. I couldn't get a solution to work on my own. 
>
> The idea is to swap each corner index with each other while holding the replaced value as temporary to move it to the next corner\
> 0,0 -> 0,N\
> 0,N -> N,N\
> N,N -> N,0\
> N,0 -> 0,0
> 
> 0,1 -> 1,N\
> 1,N -> N,N-1\
> N,N-1->N-1,0\
> N-1,0-> 0,1
> 
> 0,2-> 2,N\
> 2,N->N,N-2\
> N,N-2->N-2,0\
> N-2,0->0,2
> 
> 1,1 -> 1,N-1\
> 1,N-1->N-1,N-1\
> N-1,N-1->N-1,1\
> N-1,1-> 1,1

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

For the most part, my initial solution is performs as best as we can get time complexity wise at O(N^2), however, the extra O(N^2) space for the duplicated array is unneccesary

Reading the solution, the book points out

- For the inplace solution, I was close but couldn't get the index math figured out
  - The book implements a layer count where there are N/2 layers then also an offset
  - The offset is where I couldn't figure out how to get an N-1 index when in the 2nd layer
    - I was able to figure out the N-1 when going corner to corner in the first layer
  - This solution stores the topLeft value in a temp variable then goes backwards to prevent having to store mulitple temp variables
    - Going backwards means the index we're replacing will always have the value we're replacing it with in the corner - 1 spot until we reach back to the topLeft
      - When we get to the topRight, the reach back value in the topLeft  was replaced by the bottomLeft, so we reference the temporary stored topLeft variable 
- I failed to account for an edge case of a 0 index matrix being passed in or a non NxN matrix being passed in

# Zero Matrix

## Challenge Details

- Source: Chapter 1, Question 8, Page 91
- Difficulty: `undefined`
- Languages Completed: Python3, C#
- Synopsis
  - Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
  - Hints: #17, #74, #102
  - Solution: Page 204

## Challenge Commentary

### Initial Thoughts

> First, the input matrix is M x N so we can't make any size assumption. M could equal N, but most often it won't
>
> We'll need to check that both M and N are of length > 0
> If M > 0 and N == 0, we can iterate over M to find if there's any 0's, if there is the entire row will be turned into 0s
> 
> For solving, one of my first inclinations is we iterate over the matrix and keep a record of which indices are 0s. From there we can write a function to fill out each column and row from the (M,N) index with 0s
>
> We could check if the index is already set to 0 or we could simply overwrite it. I think the only time save would be if we could exit early by knowing all future replacement indices are set to 0. Which i'm not sure if we can do that
>
> - If we found a 0 when first iterating to find all 0 (M,N) indices
> - We could replace all following (M+N, N+M) indices with 0 and shorten the later replacement looping
> - This may add too much complexity however
> 
### `Python3` Solution

**Solution Status:** `Passed`\
**Solution Runtime:** `O(M*N)`\
**Completion Date:** `07\14\2024`\
**`Python3` Specific Notes:**
> For finding a brute force solution:
>
> - We instantiate 2 empty sets, 1 set for rows and 1 set for columns
>   - These sets keep track of whether the row # or col # has a 0 in it
> - We iterate over the entire M x N matrix and find the 0s
>   - Place the row # or col # in the row or col set when a 0 is found
> - We iterate over the entire matrix again
>   - Check for each index if the current row or col exist in either the row set or col set
>   - If so, replace the current index with a 0
> - This solution is O(N) to find M rows + O(M*N) for first iteration + O(M*N) for 2nd iteration over the matrix
>   - I blieve at worst this is O(M*N)
> - This solution is O(M+N) + O(M*N) space complexity 
>   - The additional O(M+N) is because of the 2 instantiated sets

### `C#` Solution

**Solution Status:** `Pass\Fail`\
**Solution Runtime:** `O()`\
**Completion Date:** `Month\Day\2024`\
**`C#` Specific Notes:**
> N/A

### Closing Thoughts

For the most part, my implemented solution performs as best as we can get time complexity wise at O(M*N), however, the extra O(M+N) space for the extra 2 sets can be eliminated with more advanced tactics

Reading the solution, the book points out

- The book takes an approach of replacing a whole row or column when needed where mine goes index by index
  - I don't think there's much of a difference here as the performance is still the same
  - 0ing a whole row/column in a separate function is cleaner and more readable
- One of the advnaced tactics the book uses it is uses the first row/column to track whether a column/row should be 0d
  - This makes it so the space complexity is O(1)
  - The first row/column are 0d if needed 
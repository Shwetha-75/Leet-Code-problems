'''
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104.
 

'''

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        numsArray=[grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        numsArray.sort()
        length=len(numsArray)
        median=numsArray[length//2]
        count=0 
        for num in numsArray:
            if num%x != median%x:
                return -1 
            else:
                count+=abs(median-num)//x 
        return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().minOperations([[2,4],[6,8]],2)==4 
      def testing_case_two(self):
          assert Solution().minOperations([[1,5],[2,3]],1)==5 
      def testing_case_three(self):
          assert Solution().minOperations([[1,2],[3,4]],2)==-1 
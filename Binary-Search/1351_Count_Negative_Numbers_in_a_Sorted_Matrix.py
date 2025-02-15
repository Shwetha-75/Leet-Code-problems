'''
vGiven a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 
'''

# linear Search 
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        row,col=len(grid),len(grid[0])
        counter=0 
        for i in range(row):
            for j in range(col-1,-1,-1):
                if grid[i][j]<0: counter+=1
                else: break 
        return counter 

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        j,i=0,len(grid)-1
        count=0 
        while i>=0 and j<len(grid[0]):
                if grid[i][j]<0:
                   count=count+len(grid[i])-j 
                   i-=1 
                else:
                    j+=1 
        return count
        
        pass
class TestApp:
    
        def testing_case_one(self):
            assert Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])==8 
          
        def testing_case_two(self):
            assert Solution().countNegatives([[3,2],[1,0]])==0
'''
Problem Statement 4
Given a n * m matrix of ones and zeros, where 0 denotes water and 1 denotes island now you have to count the number of square sub-island. 

Input Format
First line contains n and m, where n is the number of rows and m is the column.

Second line contains the element of the arr matrix.

Output Format
Print the count of the number of square sub-island. 

Constraints
1 <= arr.length <= 300

1 <= arr[0].length <= 300

0 <= arr[i][j] <= 1.

'''
class Solution:
    def calculateSubIsland(self,matrix:list[list[int]])->int:
        row=len(matrix)
        col=len(matrix[0])
        
        grid=[[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    grid[i][j]=1 if matrix[i][j]==1 else 0 
                else:
                    if matrix[i][j]==1:
                        grid[i][j]=min(grid[i-1][j-1],grid[i-1][j],grid[i][j-1])+1 
        squares=0 
        for i in grid:
            squares+=sum(i)
        return squares 


class TestApp:
    def testing_case_one(self):
        assert Solution().calculateSubIsland([[1, 1, 1 ,0],[1, 1, 1, 1],[1, 1 ,1 ,0]])==15
    def testing_case_two(self):
        assert Solution().calculateSubIsland([[1,1],[1,1]])==5 
    def testing_case_three(self):
        assert Solution().calculateSubIsland([[1,0,1],[0,1,0],[1,0,1]])==5
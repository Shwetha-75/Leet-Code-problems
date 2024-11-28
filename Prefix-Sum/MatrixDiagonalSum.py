'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100.

'''


class Solution:
    def diagonalSum(self,matrix:list[list:int])-> int:
        # Brute Force Approach 
        # row,col=len(mat),len(mat)
        
        # for i in range(row):
        #     for j in range(col):
        #         if i==j or (i+j+1)==col:
        #             sum_diagonal+=mat[i][j]
        sum_diagonal=0
        n=len(matrix)
        for i in range(n):
            sum_diagonal+=matrix[i][i]
            sum_diagonal+=matrix[n-1-i][i]
        if n%2!=0:
           sum_diagonal-=matrix[n//2][n//2] 
        return sum_diagonal 
def main():
    sol=Solution()
    result=sol.diagonalSum([[1,1,1],
                            [1,1,1],
                            [1,1,1]])
    print(result)
main()
        
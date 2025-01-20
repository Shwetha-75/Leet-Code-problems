'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n

'''

class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
         n=len(matrix)
         array=[i for i in range(1,n+1)]
         count=0
         for i in matrix:
             if set(array)==set(i):
                 count+=1
         for i in range(n):
             temp=[]
             for j in range(n):
                 temp.append(matrix[j][i])
             if set(array)==set(temp):
                 count+=1
         return count==2*n
class TestApp:
      def testing_case_one(self):
          assert Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]])==True 
      def testing_case_two(self):
          assert Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]])==False 



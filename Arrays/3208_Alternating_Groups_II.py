'''
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
'''

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        count=0 
        n=len(colors)
        colors+=colors
        for i in range(n):
            if self.helper(colors[i:i+k:]):
                count+=1 
        return count 
    def helper(self,color:list[int])->bool:
        n=len(color)
        for i in range(n-1):
            if color[i]==color[i+1]:return False 
        return True 
    
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        count=0 
        n=len(colors)
        left=0
        colors+=colors 
        print(colors)
        for i in range(1,n+k-1):
             print(i)
             if i>0 and colors[i]==colors[i-1]:
                 left=i
             if i-left+1>=k:
                 count+=1
        return count
class TestApp:
    def testing_case_one(self):
        assert Solution().numberOfAlternatingGroups([0,1,0,1,0],3)==3 
    def testing_case_two(self):
        assert Solution().numberOfAlternatingGroups([0,1,0,0,1,0,1],6)==2 
    def testing_case_three(self):
        assert Solution().numberOfAlternatingGroups([1,1,0,1],4)==0                                           
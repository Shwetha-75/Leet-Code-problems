'''
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
 

Example 1:

Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
Example 2:

Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105.

'''

import sys
import math
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        if len(nums)==1: return 0
        
        right_sum,n,min_value,left_sum,index=sum(nums),len(nums),sys.maxsize,0,0
     
        for i in range(n):
            left_sum+=nums[i]
            right_sum-=nums[i]
            value=abs(math.floor(left_sum/(i+1))-(0 if n-i ==1 else math.floor(right_sum/(n-i-1))))
            if value<min_value:
                min_value=value
                index=i 
        
        return index 
class TestApp:
    def testing_case_one(self):
        assert Solution().minimumAverageDifference([2,5,3,9,5,3])==3
        
    def testing_case_two(self):
        assert Solution().minimumAverageDifference([0])==0
    
    def testing_case_three(self):
        assert Solution().minimumAverageDifference([3,1,3,4,2])==3
    
    def testing_case_four(self):
        assert Solution().minimumAverageDifference([0,3])==1
    
    def testing_case_five(self):
        assert Solution().minimumAverageDifference([0,4,2,0,0])==0
    
    
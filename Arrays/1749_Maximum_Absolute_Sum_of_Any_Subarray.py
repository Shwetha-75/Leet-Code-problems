'''
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# class Solution:
#     def maxAbsoluteSum(self, nums: list[int]) -> int:
#         maximum_sum,n=0,len(nums) 
#         for i in range(n):
#             temp_sum=0
#             for j in range(i,n):
#                 temp_sum+=nums[j]
#                 maximum_sum=max(maximum_sum,abs(temp_sum))
#         return maximum_sum 

# Kadane's algorithm 
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        # maximum sum 
        maximumEnding,resultMaximum=0,0 
        for i in nums:
            if maximumEnding<0 and i>0:
                maximumEnding=i 
            else:
                maximumEnding+=i 
            resultMaximum=max(resultMaximum,maximumEnding)
            print(i,maximumEnding,resultMaximum)
        
        # minimum sum 
        minimumEnding,resultMinimum=0,float('inf')
        for i in nums:
            if minimumEnding>0 and i<0:
                minimumEnding=i 
            else:
                minimumEnding+=i 
            resultMinimum=min(resultMinimum,minimumEnding)
        return max(resultMaximum,abs(resultMinimum))
    
    
class TestApp:
        def testing_case_one(self):
            assert Solution().maxAbsoluteSum([1,-3,2,3,-4])==5 
        def testing_case_two(self):
            assert Solution().maxAbsoluteSum([2,-5,1,-4,3,-2])==8
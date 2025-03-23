'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left,right=0,0 
        n=len(nums)
        max_len=0
        count_zero=0
        while left<n and right<n:
              if nums[right]==0:
                  count_zero+=1 
              print(nums[right],count_zero)  
              if count_zero>k:
                  if nums[left]==0:
                      count_zero-=1 
                  left+=1 
              else:
                  max_len=max(max_len,right-left+1)
              right+=1 
              
        return max_len 
class TestApp:
      def testing_case_one(self):
          assert Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)==6 
      def testing_case_two(self):
          assert Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)==10 
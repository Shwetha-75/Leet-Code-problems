'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

'''


# Modifying the array
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count=0
        while nums and 0 in nums: 
              nums.remove(0)
              count+=1
        
        for i in range(count):
            nums.append(0)
        return nums


# Using Two pointers approach 
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:    
        non_zero,zero,n=0,0,len(nums)
        while non_zero<n:
              if nums[non_zero]!=0:
                  if zero<non_zero:
                     nums[zero],nums[non_zero]=nums[non_zero],nums[zero]
                  zero+=1 
              non_zero+=1 
        



class TestApp:
    def testing_case_one(self):
        assert Solution().moveZeroes([0,1,0,3,12])==[1,3,12,0,0] 
    
    def testing_case_two(self):
        assert Solution().moveZeroes([0,0,0,0])==[0,0,0,0]
    
    def testing_case_three(self):
        assert Solution().moveZeroes([0,1])==[1,0,1]
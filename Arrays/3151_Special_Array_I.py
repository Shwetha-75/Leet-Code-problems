'''
An array is considered special if every pair of its 
adjacent elements contains two numbers with different parity.

You are given an array of integers nums. 
Return true if nums is a special array, otherwise, return false.

 
Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums)==1 or not nums: return True 
        n=len(nums)
        for i in range(1,n):
            if nums[i]%2==nums[i-1]%2: return False
        return True 


class TestApp:
    def testing_case_one(self):
        assert Solution().isArraySpecial([1])==True
    
    def testing_case_two(self):
        assert Solution().isArraySpecial([2,1,4])==True 
    
    
    def testing_case_three(self):
        assert Solution().isArraySpecial([4,3,1,6])==False 
'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100.


'''
class Solution:
    def check(self, nums: list[int]) -> bool:
        temp=sorted(nums)
        index=0
        n=len(nums)
        # finding the pivot point
        pivot_index=0 
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                pivot_index=i+1
                break
        for i in range(pivot_index,n):
            if nums[i]==temp[0]:
                index=i 
                break
        for i in temp:
            if index==n:
                index=0
            if nums[index]!=i:
                return False 
            index+=1 
        return  True 


class TestApp:
    def testing_case_one(self):
        assert Solution().check([3,4,5,1,2])==True 
    
    def testing_case_two(self):
        assert Solution().check([2,1,3,4])==False 
    
    def testing_case_three(self):
        assert Solution().check([1,2,3])==True 
    
    def testing_case_four(self):
        assert Solution().check([6,10,6])==True
    
    def testing_cae_five(self):
        assert Solution().check([7,9,1,1,1,3])==True 
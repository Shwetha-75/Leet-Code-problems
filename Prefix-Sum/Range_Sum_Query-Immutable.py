'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
'''

# Brute Force Approach 
class NumArray:
    def __init__(self,nums:list):
        self.nums=nums  
    def sumRange(self,left:int,right:int):
        return sum(self.nums[left:right+1:])

# Optimal Approach 
class NumArray_1:
        # When we are creating an object for NumArray 
        def __init__(self,nums:list):
            # Initializing the array
            self.nums=nums 
            # calculate the previous index value and present index value ----> Update present index value
            for i in range(1,len(nums)):
                # prefix sum
                self.nums[i]+=self.nums[i-1] 
        # calculating the sum at sub array range 
        def sumRange(self,left:int,right:int):
            if left==0:
                return self.nums[right]
            return self.nums[right]-self.nums[left-1]   
def main():
    pass 
      
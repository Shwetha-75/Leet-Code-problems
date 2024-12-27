'''
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray
 of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Note that [2] is also a special subarray.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64,


'''
import sys
class Solution():
    def minimumSubarrayLength(self,nums: list[int], k: int) -> int:
        
        # traverse using nested for in brute force approach 
        # for each subarray take Xor of each element an d its adjacent 
        # check if the result is atleast k if the calculate its length and update minimum among all possible subarray length
        # return minimum length
        max_value,n=sys.maxsize,len(nums)
        for i in range(n):
            temp=nums[i]
            for j in range(i,n):
                temp|=nums[j]
                if temp>=k:
                    print(temp,nums[j],nums[i])
                    max_value=min(max_value,abs(i-j)+1)
        return max_value if max_value!=sys.maxsize else -1

class TestApp:
       
       def testing_minimumSubarrayLength_1(self):
           
               assert Solution().minimumSubarrayLength([1,2,3],2)==1
               
       def testing_minimumSubarrayLength_2(self):
               assert Solution().minimumSubarrayLength([2,1,8],10)==3
         
       def testing_minimumSubarrayLength_3(self):
               assert Solution().minimumSubarrayLength([1,2],0)==1

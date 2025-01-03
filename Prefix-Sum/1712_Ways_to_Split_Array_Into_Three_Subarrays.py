'''
Unsolved need to produce more efficiently
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 104.

'''

class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        count,n=0,len(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        
            
        # for i in range(n-2):
        #     left+=nums[i]
        #     mid=0
        #     right-=left
        #     for j in range(i+1,n-1):
        #         mid+=nums[j]
        #         print(left,mid,right-mid)
        #         if left<=mid and mid<=right-mid:
        #             count+=1
        #         else:
        #             right-=mid
        #             break
            
        #     right+=nums[i+2]
        #     print(right)
        for i in range(n-2):
            for j in range(i+1,n-1):
                print(nums[i],nums[j]-nums[i],nums[-1]-nums[j])
                if nums[i]<=nums[j]-nums[i] and nums[j]-nums[i]<=nums[-1]-nums[j]:
                    count+=1
                
            
        return count     
class TestApp:
    def testing_case_one(self):
         assert Solution().waysToSplit([1,1,1])==1
    def testing_case_two(self):
        assert Solution().waysToSplit([1,2,2,2,5,0])==3
    def testing_case_three(self):
        assert Solution().waysToSplit([3,2,1])==0
    def testing_case_four(self):
        assert Solution().waysToSplit([2,3,5,10])==3
    def testing_case_five(self):
        assert Solution().waysToSplit([2,8,10,0,2])==1
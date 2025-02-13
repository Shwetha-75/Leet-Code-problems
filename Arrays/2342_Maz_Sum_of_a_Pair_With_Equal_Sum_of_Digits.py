'''

You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, and the sum of 
digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you 
can obtain over all possible indices i and j that satisfy the 
conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

'''

# class Solution:
#     def maximumSum(self, nums: list[int]) -> int:
#         def digitSum(num:int):
#             sum=0
#             while num!=0:
#                   sum+=num%10 
#                   num//=10 
#             return sum 
#         max_value=-1
#         n=len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 d1,d2=digitSum(nums[i]),digitSum(nums[j])
#                 if d1==d2:
#                     max_value=max(max_value,nums[i]+nums[j])
#         return max_value 
class Solution:
      def maximumSum(self,nums:list[int])->int:
            def digitSum(num:int):
                sum=0 
                while num!=0:
                    sum+=num%10 
                    num//=10 
                return sum 
            hash_map={}
            max_value=-1 
            for i in nums:
                d1=digitSum(i)
                if d1 in hash_map:
                   max_value=max(max_value,i+hash_map[d1]) 
                   hash_map[d1]=max(hash_map[d1],i)
                else:
                    hash_map[d1]=i 
            return max_value 
                             
class TestApp:
        def testing_case_one(self):
            assert Solution().maximumSum([18,43,36,13,7])==54 
        def testing_case_two(self):
            assert Solution().maximumSum([10,12,19,14])==-1
        def testing_case_three(self):
            assert Solution().maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401])==973
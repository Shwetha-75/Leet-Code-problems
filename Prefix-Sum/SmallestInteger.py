'''

You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50.

'''

class Solution:
    def missingInteger(self,nums:list):
        # max_length,result,prefix_index,prefix_sum=0,0,0,nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i-1]+1==nums[i]:
        #         prefix_sum+=nums[i]
        #     else:
                
        #         length=i-prefix_index
        #         if length>max_length:
        #             max_length=length 
        #             while prefix_sum in nums:
        #                   prefix_sum+=1
        #             result=prefix_sum
        #         prefix_index=i-1 
        #         prefix_sum=0 
        # length=(len(nums)-1)-prefix_index
        # if length>max_length:
            
        #     max_length=length 
        #     while prefix_sum in nums:
        #           prefix_sum+=1
        #     return prefix_sum   
        # else: return result
        
        # 
        prefix_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefix_sum+=nums[i] 
            else:
                break 
        while prefix_sum in nums:
              prefix_sum+=1 
        return prefix_sum 
def main():
    sol=Solution()
    result=sol.missingInteger([3,4,5,1,12,14,13])
    print(result)
main()
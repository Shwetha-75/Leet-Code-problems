'''

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious 
subsequence
 among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109.

'''

class Solution:
    def findLHS(self,nums:list[int]):
        nums.sort()
        left,right,n,max_len=0,1,len(nums),0
        while left<n and right<n and left<right:
            while nums[right]-nums[left]>1: left+=1 
            if nums[right]-nums[left]==1: max_len=max(max_len,(right-left)+1)
            right+=1 
            # correct but one mistake 
            #   if nums[right]-nums[left]==1:
            #       max_len=max(max_len,(right-left)+1)
            #   else: left+=1 
            #   right+=1 
        return max_len 
def main():
    sol=Solution()
    result=sol.findLHS([1,2,2,1])
    print(result)
main()
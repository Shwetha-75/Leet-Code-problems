'''
2501. Longest Square Streak in an Array
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
Example 2:

Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
 

Constraints:

2 <= nums.length <= 105
2 <= nums[i] <= 105

'''

class Solution:
    def longestSquareStreak(self,nums:list):
        # subsequence=[]
        # for i in range(len(nums)):
        #     square=nums[i]**2
        #     if i==0:    
        #         if square in nums:
        #             temp=[nums[i],square]
        #             subsequence.append(temp)
        #         else:
        #             continue
        #     elif i>0:
        #         if square in nums:
        #             status=False
        #             for k in subsequence:
        #                 if square in k:
        #                     k.append(nums[i])
        #                     status=True 
        #                 else: continue 
        #             if not status:
        #                 temp=[nums[i],square]
        #                 subsequence.append(temp)
        #     else:
        #         continue
        # if not subsequence: return -1
        # max_len=-1
        # for i in subsequence:
        #     max_len=max((max_len,len(i)))
        # return max_len
        max_len=-1
        #set of elements
        nums_set=set(nums)
        nums=sorted(nums_set)
        
        for i in nums:
            count=0
            curr=i
            while curr in nums_set:
                  nums_set.remove(curr)
                  curr**=2
                  count+=1
            max_len=max(max_len,count)
        return max_len if max_len>1 else -1
        
      
def main():
    sol=Solution()
    result=sol.longestSquareStreak([2,3,5,6,7])
    print(result)
main()

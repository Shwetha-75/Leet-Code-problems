'''
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length

'''

from collections import Counter
class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if k==n:return max(nums)
        elif k==1:
             nums.sort(reverse=True)
             hash_map=list(Counter(nums).items())
             for i in hash_map:
                 if i[1]==1:
                    return i[0]
        else:
            last=nums[n-1]
            first=nums[0]
            count_first=nums.count(first)
            count_last=nums.count(last)
            if last>first and count_last==1:
                return last 
            if first>last and count_first==1:
                return first 
            if count_last==1 and count_first!=1:
                return last 
            if count_first==1 and count_last!=1:
                return first 
            
        return -1 
    
class TestApp:  
      def testing_case_one(self):
          assert Solution().largestInteger([3,9,2,1,7],3)==7 
      def testing_case_two(self):
          assert Solution().largestInteger([0,0],1)==-1
                
      def testing_case_three(self):
          assert Solution().largestInteger([3,9,7,2,1,7],4)==3  

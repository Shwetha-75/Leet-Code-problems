'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104.

'''

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # sort the array 
        nums.sort(reverse=True)  
        return nums[k-1]
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        result=[]
        for num in nums:
            heapq.heappush(result,num)
            if len(result)>k:
                heapq.heappop(result)
        return result[0]

class TestApp:
      def testing_case_two(self):
          assert Solution().findKthLargest([3,2,1,5,6,4],2)==5 
      def testing_cse_two(self):
          assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4)==4
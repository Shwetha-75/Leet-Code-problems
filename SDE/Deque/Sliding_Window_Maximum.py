'''

Given an array arr[] of integers and an integer k, your task is to 
find the maximum value for each contiguous subarray of size k. 
The output should be an array of maximum values corresponding to each contiguous subarray.

Examples : 

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6


Input: arr[] = [5, 1, 3, 4, 2, 6], k = 1
Output: [5, 1, 3, 4, 2, 6]
Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array.


Input: arr[] = [1, 3, 2, 1, 7, 3], k = 3
Output: [3, 3, 7, 7]



'''
class Solution:
      def findingMaximumNumber(self,nums:list[int],k:int):
          result=[]
          n=len(nums)
          for i in range(n-k+1):
              result.append(max(nums[i:i+k:]))
          return result 
import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        nums=[-1*(i) for i in nums]
        result=[]
        n=len(nums)
        for i in range(n-k+1):
            temp=nums[i:i+k]
            heapq.heapify(temp)
            result.append(-1*heapq.heappop(temp))
        
        return result 
import heapq   
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        result=[]
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        result.append(-heap[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            while heap[0][1]<=i-k:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
class TestApp:
        def testing_case_one(self):
            assert Solution().maxSlidingWindow( [1, 2, 3, 1, 4, 5, 2, 3, 6],3)==[3,3,4,5,5,5,6]
        def testing_case_two(self):
            assert Solution().maxSlidingWindow( [5, 1, 3, 4, 2, 6],1)== [5, 1, 3, 4, 2, 6]
            
        def testing_case_three(self):
            assert Solution().maxSlidingWindow([1, 3, 2, 1, 7, 3],3)==[3, 3, 7, 7]
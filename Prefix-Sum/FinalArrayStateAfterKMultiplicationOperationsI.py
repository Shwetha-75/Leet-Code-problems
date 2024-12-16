'''

You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

 

Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
Example 2:

Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:

Operation	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]

'''
import heapq
class Solution:
    def getFinalState(self,nums:list[int],k:int,multiplier:int):
        # Using Min Heap Algorithm
        nums=[(nums[index],index) for index in range(len(nums))]
        heapq.heapify(nums)
        while k!=0:
              value=heapq.heappop(nums)
              heapq.heappush(nums,(value[0]*multiplier,value[1]))
              k-=1
        nums.sort(key=lambda x:x[1])
        return [i[0] for i in nums] 
        # while k!=0:
        #     value=min(nums)
        #     index=nums.index(value)
        #     nums[index]=value*multiplier 
        #     k-=1
        # return nums 
def main():
    sol=Solution()
    result=sol.getFinalState([2,1,3,5,6], 5,2)
    print(result)
main()
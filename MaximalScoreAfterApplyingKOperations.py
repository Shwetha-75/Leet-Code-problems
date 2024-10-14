'''
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
 

Constraints:

1 <= nums.length, k <= 105
1 <= nums[i] <= 109

'''

import heapq
import math
class  Solution:
    def maximalScoreAfterApplyingKOperations(self,arr:list,k:int):
        total_sum=0
        # negating all the lements  
        # since if I use max function to get maximum element or heapq.nlargest it takes O(n)
        # to perform 
        # So negate all the elements
        # And heapify it internally uses priority queue
        
        arr=[-i for i in arr]
        
        heapq.heapify(arr)
        while k!=0:
            # pop the element from the heap and negate it 
              element=-heapq.heappop(arr)
            #   push the lement to the arr by dividing it by 3 and taking ceil of it
              heapq.heappush(arr,-math.ceil(element/3))
            # take the total_sum by taking largest element in the current list
              total_sum+=element
            #   decrement number of operations
              k-=1
        return total_sum
def main():
    sol=Solution()
    res=sol.maximalScoreAfterApplyingKOperations([1,10,3,3,3],3)
    print(res)
main()
    
'''

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all 
subarrays
 of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

Example 1:

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.
Example 2:

Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:

Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]

 

Constraints:

1 <= n == nums.length <= 500
1 <= nums[i] <= 105
1 <= k <= n.


---------------------------------------------------------------------------------------------
Intuition
Using two pointers and by taking sub array each of length k

Approach
-Initialize i=0, result=[] to store the result of each sub array, j=k-1.
-Traverse through array starting from 0 until len(nums)-l:
-for each sub array call the function to check the sub array satifies the contraints
       -checkPower(arr):
          -Travserse through each elements in linear fashion starting from 1 until last index.
          -check for false case where in present is not strictly greater than previous element and check for consecutive if the present element is not immediate next to previouse element.
               -return -1
          -default case return max among all the arr elements .
-Append the result from each function call to the result array.
-return the result.


Complexity
Time complexity:
O(N*K).

Space complexity:
O(1).


'''


class Solution:
      def resultsArray(self,nums:list,k:int):
        #   Brute Force Approach 
        #   def checkPower(arr:list):
        #       print(arr)
        #       for i in range(1,len(arr)):
        #           if not (arr[i-1] < arr [i] and arr[i-1]+1==arr[i]):
        #               return -1
        #       return max(arr)
        #   results=[]
        #   j=k-1 
        #   i=0
        #   remaining=len(nums)-k
        #   print(remaining)
        #   while i<=remaining:
        #       temp=nums[i:j+1:]
        #       temp=checkPower(temp)
        #       results.append(temp)
        #       i+=1
        #       j=k+i-1 
        #   return results 
        result=[-1]*(len(nums)-k+1)
        consecutiveCount=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                consecutiveCount+=1
            else:
                consecutiveCount=1
            if consecutiveCount>=k: result[i-k+2]=nums[i+1]
        return result
def main():
    sol=Solution()
    result=sol.resultsArray([2,2,2,2,2],4)
    print(result)
main()


     
              
              
              
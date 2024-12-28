'''
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the 
subarray
 nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

1 <= n == nums.length <= 50
1 <= nums[i] <= 50
1 <= x <= k <= nums.length.

'''

from collections import Counter
class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        def x_sum(arr:list[int],x:int)->int:
            
            # take the frequency count of every elements and convert that to list of tuples 
            h_map=list(dict(Counter(arr)).items())
            # Sort the list accordingly keys 
            h_map.sort(key=lambda x:x[0])
            # sort the h_map accordingly values
            h_map.sort(key=lambda x:x[1])
            # sum of all values 
            sum_val=0
            while x!=0:
                
                if h_map:
                    element=h_map.pop(-1)
                    sum_val+=element[0]*element[1]
                    x-=1
                else: 
                    break
            return sum_val
        # take the sub array of size k and take x_sum for every sub array 
        # and return the result and append it to result array 
        
        n=len(nums)
        result=[]
        for i in range(n-k+1):
            result.append(x_sum(nums[i:i+k],x))
        return result

class TestApp:
      def testing_case_1(self):
          assert Solution().findXSum([1,1,2,2,3,4,2,3],6,2)==[6,10,12]
      def testing_case_2(self):
          assert Solution().findXSum([3,8,7,8,7,5],2,2)==[11,15,15,15,12]               

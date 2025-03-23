'''
Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

Note: The elements after the distinct ones can be in any order and hold any value, as they don’t affect the result.

Examples: 

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: All the elements are 2, So only keep one instance of 2.


Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
Output: [1, 2, 3, 4, 5]

Input: arr[] = [1, 2, 3]
Output: [1, 2, 3]
Explanation : No change as all elements are distinct.

'''
# Using Stack 
class Solution:
      def removeDuplicatesFromSortedArray(self,nums:list[int]):
            stack:list[int]=[nums[0]]
            for i in nums:
                if stack[-1]!=i:
                   stack.append(i)
            return stack 
# optimized approach
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        valid,invalid,curr=0,-1,1 
        n=len(nums)
       
Solution().removeDuplicates([1,2,2,3,4,4,4,5,5])
    
         
         
         
# class TestApp:
#       def testing_case_one(self):
#           assert Solution().removeDuplicatesFromSortedArray([2,2,2,2,2,2])==[2]
#       def testing_case_two(self):
#           assert Solution().removeDuplicatesFromSortedArray([1,2,3,4,5])==[1,2,3,4,5]
#       def testing_case_three(self):
#           assert Solution().removeDuplicatesFromSortedArray([1,2,2,3,4,4,4,4,5,5,5])==[1,2,3,4,5]
             
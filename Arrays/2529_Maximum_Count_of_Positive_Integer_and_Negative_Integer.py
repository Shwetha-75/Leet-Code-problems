'''

Given an array nums sorted in non-decreasing order, 
return the maximum between the number of positive integers 
and the number of negative integers.

In other words, if the number of positive integers 
in nums is pos and the number of negative integers is neg, then return the 
maximum of pos and neg.
Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
 

'''

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        count_positive,count_negative=0,0 
        for i in nums:
            if i<0: count_negative+=1 
            if i>0: count_positive+=1 
        return max(count_negative,count_positive) 
# using Binary Search 
class Solution:
    def lowerBound(self,nums:list[int])->int:
        start,end=0,len(nums)-1 
        index=len(nums)-1 
        while start<=end:
            mid=(start+end)//2 
            if nums[mid]<0:
                start=mid+1 
            else:
                end=mid-1     
                index=mid 
        return index 
    def upperBound(self,nums:list[int])->int:
        start,end=0,len(nums)-1 
        index=len(nums)-1 
        while start<=end:
              mid=(start+end)//2 
              if nums[mid]<=0:
                  start=mid+1
              else:
                  end=mid-1 
                  index=mid 
        return index 
     
                     
    def maximumCount(self,nums:list[int])->int:
        n=len(nums)
        return max(n-self.upperBound(nums),self.lowerBound(nums))
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumCount([-2,-1,-1,1,2,3])==3
      def testing_case_two(self):
          assert Solution().maximumCount([-2,-1,-1,1,2,3])==3
      def testing_case_three(self):
          assert Solution().maximumCount([5,20,66,1314])==4
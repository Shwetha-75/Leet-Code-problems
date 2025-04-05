class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # liner approach 
        max_value=-1 
        i=0
        for index in range(len(nums)):
            if nums[index]>max_value:
                i=index 
                max_value=nums[index]
        return i
    
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left,right=0,len(nums)-1 
        while left<=right:
              mid=(left+right)//2 
              if nums[mid]>nums[mid+1]:
                  right=mid 
              else:
                  left=mid+1 
        return left
    
class Solution:
      def testing_case_one(self):
          assert Solution().testing_case_one([1,2,3,1])==2 
      def testing_case_two(self):
          assert Solution().testing_case_one([1,2,1,3,5,6,4])==5
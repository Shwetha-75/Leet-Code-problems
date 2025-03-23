class Solution:
      def peakIndexInMountainArray(self, arr: list[int]) -> int:
            def findPivotIndex(nums:list[int],n:int,left:int,right:int):
               mid=(left+right)//2
               if mid==0:
                   return 0 
               if mid==n-1:
                   return n-1
               while left<=right:
                     if nums[mid]>nums[mid-1] and nums[mid]> nums[mid+1]:
                         return mid 
                     elif nums[mid]>nums[mid-1] and nums[mid]< nums[mid+1]:
                         return findPivotIndex(nums,n,mid,right)
                     else:
                         return findPivotIndex(nums,n,left,mid)
            return findPivotIndex(arr,len(arr),0,len(arr)-1)
class TestApp:
      def testing_case_one(self):
          assert Solution().peakIndexInMountainArray([0,1,0])==1 
      def testing_case_two(self):
          assert Solution().peakIndexInMountainArray([0,2,1,0])==1         
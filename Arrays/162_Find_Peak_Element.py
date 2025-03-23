class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        left,right=0,len(arr)-1 
        while left<right:
              mid=(left+right)//2 
              if arr[mid]>arr[mid+1]:
                  right=mid
              else:
                  left=mid+1 
        return left 
    
class TestApp:
      def testing_case_one(self):
          assert Solution().findPeakElement([1,2])==1 
      def testing_case_two(self):
          assert Solution().findPeakElement([1,2,1,3,5,6,4])==5 
      def testing_case_three(self):
          assert Solution().findPeakElement([1,2,3,1])==2
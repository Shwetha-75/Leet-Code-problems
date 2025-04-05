class Solution:
      def findAKeyInSortedArray(self,arr:list[int],target:int)->int:
            left,right=0,len(arr)-1 
            while left<=right:
                  mid=(left+right)//2 
                  if arr[mid]==target:
                      return mid 
                  elif arr[mid]>target:
                      right=mid-1 
                  else:
                      left=mid+1 
            return -1 
        
class TestApp:
      def testing_case_one(self):
          assert Solution().findAKeyInSortedArray([1,2,3,4,5,6],6)==5 
      def testing_case_two(self):
          assert Solution().findAKeyInSortedArray([2,3,4,6,7,9],2)==0 
      def testing_case_three(self):
          assert Solution().findAKeyInSortedArray([3,4,5,6,7],5)==2 
      def testing_case_four(self):
          assert Solution().findAKeyInSortedArray([1,2,3,4,5,6,7,8],10)==-1
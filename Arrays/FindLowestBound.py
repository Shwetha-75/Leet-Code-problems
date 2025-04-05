class Solution:
     def findTheLowestBound(self,arr:list[int],target:int):
            left,right=0,len(arr)-1 
            ans=len(arr)
            while left<=right:
                  mid=(left+right)//2 
                  if arr[mid]>=target:
                      ans=mid
                      right=mid-1 
                  else:
                      left=mid+1 
            return ans 

class TestApp:
      def testing_case_one(self):
          assert Solution().findTheLowestBound([1,2,3,3,7,8,9,9,9,11],9)==6 
      def testing_case_two(self):
          assert Solution().findTheLowestBound([1,1,1,1,1,1,1,1,1],1)==0 
      def testing_case_three(self):
          assert Solution().findTheLowestBound([1,1,1,3,4,4,5,6,9],8)==8
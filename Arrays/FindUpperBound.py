class Solution:
      def findUpperBound(self,arr:list[int],target:int)->int:
            left,right=0,len(arr)-1 
            ans=-1
            while left<=right:
                  mid=(left+right)//2 
                  if arr[mid]>target:
                      ans=mid 
                      right=mid-1 
                  else:
                      left=mid+1 
            return ans-1 if ans>0 else -1 
class TestApp:
       def testing_case_one(self):
           assert Solution().findUpperBound([1,2,3,3,7,8,9,9,9,11],3)==3
       def testing_case_two(self):
           assert Solution().findUpperBound([1,2,3,3,7,8,9,9,9,11],9)==8
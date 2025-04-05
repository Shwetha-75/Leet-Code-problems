class Solution:
         def targetIndices(self, nums: list[int], target: int) -> list[int]:
            bound=[-1,-1]
            def helperTarget(arr:list[int],target:int)->int:
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
            temp=helperTarget(nums,target)
            if temp!=-1:
            #    finding the left bound 
                
                left,right=0,temp 
                while left<=right:
                      mid=(left+right)//2 
                      if nums[mid]==target:
                         bound[0]=mid
                         right=mid-1 
                      else:
                          left=mid+1 
                left,right=temp,len(nums)-1 
                while left<=right:
                      mid=(left+right)//2 
                      if nums[mid]==target:
                          bound[1]=mid 
                          left=mid+1 
                      else:
                          right=mid-1 
                if temp==0:
                    bound=[0,0]
                elif temp==len(nums)-1:
                    bound=[len(nums)-1,len(nums)-1]
            return bound
                
                
class TestApp:
      def testing_case_one(self):
          assert Solution().targetIndices([1,2,2,2,3,4,5,6],2) ==[1,3]          
      def testing_case_two(self):
          assert Solution().targetIndices([1,1,2,2,2,3,3],3)==[5,6]
      def testing_case_three(self):
          assert Solution().targetIndices([1,1,1,2,3,4,5],1)==[0,2]
      def testing_case_four(self):
          assert Solution().targetIndices([1,2,3,4,5,5,5,5],5)==[4,7]
      def testing_case_five(self):
          assert Solution().targetIndices([1,2,3,3,4,5,6],7)==[-1,-1]
      def testing_case_six(self):
          assert Solution().targetIndices([1,2,3,4,5],1)==[0,0]
      def testing_case_seven(self):
          assert Solution().targetIndices([1,2,3,4,5],5)==[4,4]
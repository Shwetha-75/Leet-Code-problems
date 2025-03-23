class Solution:
    def findAKey(self,nums:list[int],key:int):
        pivotIndex=self.findPivotIndex(nums,0,len(nums)-1)
        print(pivotIndex)
        if key>nums[pivotIndex]: return -1 
        if key==nums[pivotIndex]: return pivotIndex
        temp=self.leftSubArrayBinarySearch(nums,0,pivotIndex-1,key)
        if temp!=-1:
            return temp 
        else: return self.rightSubArrayBinarySearch(nums,pivotIndex+1,len(nums)-1,key)
            
        
    def findPivotIndex(self,nums:list[int],left:int,right:int):
        mid=(left+right)//2 
        if mid==0: return 0 
        if mid==len(nums)-1: return len(nums)-1 
        while left<right:
               if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                   return mid 
               elif nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                   return self.findPivotIndex(nums,mid,right)
               else:
                   return self.findPivotIndex(nums,left,mid)
    def leftSubArrayBinarySearch(self,nums:list[int],left:int,right:int,target:int):
        while left<=right:
              mid=(left+right)//2 
              if nums[mid]==target:
                  return mid 
              elif nums[mid]>target:
                  right=mid-1 
              else: 
                  left=mid+1 
        return -1
    def rightSubArrayBinarySearch(self,nums:list[int],left:int,right:int,target:int):
        while left<=right:
              mid=(left+right)//2 
              if nums[mid]==target:
                  return mid 
              elif target>nums[mid]:
                  right=mid-1
              else:
                  left=mid+1 
        return -1
                  
class TestApp:
      def testing_case_one(self):
          assert Solution().findAKey([1,10,5,4,3,2],10)==1 
      def testing_case_four(self):
          assert Solution().findAKey([10,5,4,3,2],10)==0 
      def testing_case_two(self):
          assert Solution().findAKey([1,2,3,4,5,10,7,6],6)==7 
      def testing_case_three(self):
          assert Solution().findAKey([1,2,5,4],1)==0 
      def testing_case_five(self):
          assert Solution().findAKey([1,2,3,4,6,5],5)==5
    
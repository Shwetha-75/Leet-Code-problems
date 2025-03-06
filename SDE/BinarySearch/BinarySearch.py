#Iterative 
class Solution:
    def binarySearch(Self,nums:list[int],target:int)->int:
        # Iterative 
        left,right=0,len(nums)-1 
        while left<=right: 
                mid=(left+right)//2 
                if target==nums[mid]:
                   return mid 
                elif nums[mid]>target:
                     right=mid-1 
                else:
                    left=mid+1 
        return -1 


# Recursive 
class Solution:
      def binarySearch(self,nums:list[int],target:int)->int:
          return self.helper(nums,target,0,len(nums)-1) 
      def helper(self,nums:list[int],target:int,left:int,right:int)->int:
          
          if left>right: return -1 
          mid=(left+right)//2 
          if nums[mid]==target:
              return mid 
          if nums[mid]>target:
              return self.helper(nums,target,left,mid-1)
          else:
              return self.helper(nums,target,mid+1,right)

class TestApp:
        def testing_case_one(self):
            assert Solution().binarySearch([1,2,3,4,5,6,7,8],5)==4 
        def testing_case_two(self):
            assert Solution().binarySearch([1,2,3,4,5],8)==-1 
        
        def testing_case_three(self):
            assert Solution().binarySearch([1,2,3,4,5,6,7,8],1)==0      
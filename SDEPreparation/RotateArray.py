class Solution:
      def rotateTheArray(self,nums:list[int]):
            def helper(i:int,j:int):
                while i<=j:
                     nums[i],nums[j]=nums[j],nums[i]
                     i+=1 
                     j-=1 
            n=len(nums)
            k%=n 
            helper(0,n-1)
            helper(0,k-1)
            helper(k,n-1)
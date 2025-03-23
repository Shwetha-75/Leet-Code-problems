class Solution:
      def minOperations(self,nums:list[int]):
            operations=0
            def helper(start:int):
                for i in range(start,start+3):
                    if nums[i]==0:
                        nums[i]=1 
                    else:
                        nums[i]=0 
            for i in range(len(nums)):
                if nums[i]==0:
                    helper(i)
                    operations+=1 
            return operations if nums.count(1)==len(nums) else -1
        
        
        
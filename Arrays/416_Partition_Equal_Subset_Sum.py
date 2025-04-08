class Solution:    
      def canPartition(self, nums: list[int]) -> bool:
            result=[[]]
            for num in nums:
                result+=[sub+[num] for sub in result]
            total_sum=sum(nums)
            for set in result:
                temp=sum(set)
                if temp==total_sum-temp:
                    return True 
            return False
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0: return False 
        target=total_sum//2 
        arr=set([0])
        for num in nums:
            for current_sum in list(arr):
                if current_sum+num==target: return True 
                arr.add(current_sum+num) 
        return False    
# dp approach 
class Solution:
      def canPartition(self, nums: list[int]) -> bool:
          total_sum=sum(nums)
          if total_sum%2!=0: return False 
          target=total_sum//2 
          dp=[False]*(target+1)
          dp[0]=True 
          for num in nums:
              for value in range(target,num-1,-1):
                  dp[value]=dp[value] or dp[value-num]
          return dp[target]

class TestApp:
      def testing_case_one(self):
          assert Solution().canPartition([1,2,3,5])==False
      def testing_case_two(self):
          assert Solution().canPartition([1,5,11,5])==True 

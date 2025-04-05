class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result=[0]*len(nums)
        for i in nums:
            if i!=0:
               result[i-1]=i 
        for i in range(len(result)):
            if result[i]==0:
                return i+1 


class TestApp:
      def testing_case_one(self):
          assert Solution().missingNumber([3,0,1])==2
      def testing_case_two(self):
          assert Solution().missingNumber([0,1])==2 
        
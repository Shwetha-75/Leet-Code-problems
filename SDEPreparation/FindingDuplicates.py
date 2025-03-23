class Solution:
    
      def findDuplicates(self, nums: list[int]) -> list[int]:
          result=[0]*len(nums)
          for i in nums:
            result[i-1]+=1 
          return [i+1 for i in range(len(result)) if result[i]>1]

class TestApp:
      def testing_case_one(self):
          assert Solution().findDuplicates([4,3,2,7,8,2,3,1])==[2,3]
      def testing_case_two(self):
          assert Solution().findDuplicates([1,1,2])==[1]
      def testing_case_three(self):
          assert Solution().findDuplicates([1])==[]
          
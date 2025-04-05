class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        sum_value=0 
        for i in range(len(nums)):
            sum_value+=nums[i]
            temp=nums[i]
            print(sum_value)
            for j in range(i+1,len(nums)):
                temp^=nums[j]
                sum_value+=temp
                print(sum_value) 
        print(sum_value)
        return sum_value 

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result=[[]]
        # forming the subset 
        for num in nums:
            result+=[sub+[num] for sub in result]
        sum_value=0
        for value in result:
            temp=0
            for i in value:
                temp^=i 
            sum_value+=temp 
        return sum_value 
# Optimized and better approach Using left shift operator
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        ans=0 
        for num in nums:
            ans|=num 
        return ans << len(nums)-1

class TestApp:
      def testing_case_one(self):
          assert Solution().subsetXORSum([5,1,6])==28 
      def testing_case_two(self):
          assert Solution().subsetXORSum([1,3])==6 
      def testing_case_three(self):
          assert Solution().subsetXORSum([3,4,5,6,7,8])==480
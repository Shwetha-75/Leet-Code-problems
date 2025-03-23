class Solution:
      def maximumProfit(self,nums:list[int])->int:
          minimum_element=min(nums)
          index=nums.index(minimum_element)
          if index==len(nums)-1:
              return 0 
          maximum_value=max(nums[index::])
          return maximum_value-minimum_element

class Solution:
    def maximumProfit(self, nums: list[int]) -> int:
        minimum_element=nums[0]
        profit=0 
        for i in range(1,len(nums)):
             if nums[i]<minimum_element:
                 minimum_element=nums[i]
             else:
                 profit=max(profit,nums[i]-minimum_element)
        return profit 
    
class TestApp:
    def testing_case_one(self):
        assert Solution().maximumProfit([7, 10, 1, 3, 6, 9, 2])==8 
    def testing_case_two(self):
        assert Solution().maximumProfit([7, 6, 4, 3, 1])==0 
    def testing_case_three(self):
        assert Solution().maximumProfit([1, 3, 6, 9, 11])==10
          
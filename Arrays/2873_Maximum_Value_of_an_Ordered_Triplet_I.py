class Solution: 
    def maximumTripletValue(self, nums: list[int]) -> int:
        value=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):  
                    value=max(value,(nums[i]-nums[j])*nums[k])
        return value 
    
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ans,diff,high=0,0,0 
        for num in nums:
            ans=max(ans,diff*num)
            diff=max(high-num,diff)
            high=max(high,num)
        return ans 

class TestApp:
      def testing_case_one(self):
          assert Solution().maximumTripletValue([12,6,1,2,7])==77 
      def testing_case_two(self):
          assert Solution().maximumTripletValue([1,10,3,4,19])==133 
      def testing_case_three(self):
          assert Solution().maximumTripletValue([1,2,3])==0 
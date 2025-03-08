class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left,right=0,0 
        n=len(nums)
        max_len=0
        count_zero=0
        while left<n and right<n:
              if nums[right]==0:
                  count_zero+=1 
              print(nums[right],count_zero)  
              if count_zero>k:
                  if nums[left]==0:
                      count_zero-=1 
                  left+=1 
              else:
                  max_len=max(max_len,right-left+1)
              right+=1 
              
        return max_len 
class TestApp:
      def testing_case_one(self):
          assert Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)==6 
      def testing_case_two(self):
          assert Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)==10 
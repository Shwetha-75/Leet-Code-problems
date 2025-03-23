class Solution:
      def longestNiceSubarray(self, nums: list[int]) -> int:
            length,start,used_bit=0,0,0
            for end in range(len(nums)):
                  while used_bit & nums[end]!=0:
                        used_bit^=nums [start]
                        start+=1 
                  used_bit|=nums[end]
                  length=max(length,end-start+1)
            return length 
      
                  
Solution().longestNiceSubarray([1,3,8,48,10])
class TestApp:
      def testing_case_one(self):
          assert Solution().longestNiceSubarray([1,3,8,48,10])==3 
      def testing_case_two(self):
         assert Solution().longestNiceSubarray([3,1,5,11,13])==1 
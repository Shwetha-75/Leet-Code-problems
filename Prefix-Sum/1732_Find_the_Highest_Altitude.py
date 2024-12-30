class Solution:
        def largestAltitude(self, gain: list[int]) -> int:
            gain.insert(0,0)
            n=len(gain)
            for i in range(1,n):
                gain[i]+=gain[i-1]
            return max(gain)
        
class TestApp:
      def testing_case_one(self):
          assert Solution().largestAltitude([-5,1,5,0,-7])==1
          
      def testing_case_two(self):
          assert Solution().largestAltitude([-4,-3,-2,-1,4,3,2])==0
          
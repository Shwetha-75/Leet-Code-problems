class Solution:
      def swapWithOutUsingThirdVariable(self,a:int,b:int):
          a^=b
          b^=a 
          a^=b 
          return [a,b]
class TestApp: 
        def testing_case_one(self):
            assert Solution().swapWithOutUsingThirdVariable(2,3)==[3,2]
        def testing_case_two(self):
            assert Solution().swapWithOutUsingThirdVariable(4,5)==[5,4]
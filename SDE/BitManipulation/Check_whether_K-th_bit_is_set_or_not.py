class Solution:
       
      def checkSetBit(self,number:int,k:int)->str:
        #   option 1 
        # shifting  1 by k towards left and do bitwise with number 
        # return "YES" if number & (1 << k) else "NO"
        # performing right shift towards right by k
        return "YES" if ((number>>k) & 1) else "NO"
      
class TestApp:
        def testing_case_one(self):
            assert Solution().checkSetBit(5,1)=="NO"
        def testing_case_two(self):
            assert Solution().checkSetBit(128,7)=="YES" 
        def testing_case_three(self):
            assert Solution().checkSetBit(2,3)=="NO"



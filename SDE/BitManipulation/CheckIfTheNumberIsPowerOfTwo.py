class Solution:
     def checkTheNumberISPowerOfTwo(self,n:int)->bool:
         return n==1 or (n&(n-1))==0


class TestApp:
        def testing_case_one(self):
            assert Solution().checkTheNumberISPowerOfTwo(8)==True 
        def testing_case_two(self):
            assert Solution().checkTheNumberISPowerOfTwo(2)==True 
        def testing_case_three(self):
            assert Solution().checkTheNumberISPowerOfTwo(10)==False
        
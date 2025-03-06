class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # by frequently multiplying the number 
        x=1 
        while x<n:
             x*=3 
             if x==n: return True 
        return False
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False 
        return  math.floor(math.log(n)/math.log(3)) == math.ceil(math.log(n)/math.log(3))
class TestApp:
        def testing_case_one(self):
            assert Solution().isPowerOfThree(27)==True 
        def testing_case_two(self):
            assert Solution().isPowerOfThree(-1)==False 

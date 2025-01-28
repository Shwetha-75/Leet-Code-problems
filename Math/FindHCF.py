class Solution:
    def findGCD(self,m:int,n:int):
        while m!=n:
              if m>n:
                  m-=n 
              else:
                  n-=m 
        return n 
class TestApp:
    def testing_case_one(self):
        assert Solution().findGCD(70,15)==5
    def testing_case_two(self):
        assert Solution().findGCD(1,3)==1 
    def testing_case_three(self):
        assert Solution().findGCD(5,6)==1 
    def testing_case_four(self):
        assert Solution().findGCD(2,4)==2
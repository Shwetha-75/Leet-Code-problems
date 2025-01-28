class Solution:
    def decimalToBinary(self,n:int):
        result=""
        while n!=0:
               rem=n%2
               result+=str(rem)
               n//=2 
        return int(result[::-1])
class TestApp:
    def testing_case_one(self):
        assert Solution().decimalToBinary(2)==10
    def testing_case_two(self):
        assert Solution().decimalToBinary(10)==1010
    def testing_case_three(self):
        assert Solution().decimalToBinary(5)==101
    def testing_case_four(self):
        assert Solution().decimalToBinary(6)==110
import math
class Solution:
    def calculateMaximumSum(self,array:list[int],k:int)->int:
        max_value=-math.inf
        n=len(array)
        for i in range(n-k+1):
            max_value=max(max_value,(array[i:i+k:]))
        return max_value 

class TestApp:
    def testing_case_one(self):
        assert Solution().calculateMaximumSum([2,3,-2,4],2)==5
    def testing_case_two(self):
        assert Solution().calculateMaximumSum([2,3,-4,5,-3,7],3)==9
    def testing_case_three(self):
        assert Solution().calculateMaximumSum([0,3,4,2,-1,6],4)==11
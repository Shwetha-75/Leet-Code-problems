from functools import reduce 
class Solution:
     
     def maximumCalculateProduct(self,array:list[int],k:int):
         max_value=float('-inf')
         n=len(array)
         for i in range(n-k+1):
            max_value=max(max_value,reduce(lambda x,y:x*y,array[i:i+k:]))
         return max_value 


class TestApp:
    def testing_case_one(self):
        assert Solution().maximumCalculateProduct([2,3,-2,4],2)==6
    def testing_case_two(self):
        assert Solution().maximumCalculateProduct([2,3,0,5,0,7],3)==0
    def testing_case_three(self):
        assert Solution().maximumCalculateProduct([0,3,4,2,-1,6],3)==24                                                                             
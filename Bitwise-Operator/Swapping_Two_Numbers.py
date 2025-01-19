class Solution:
    def twoSwapping(self,num_1:int,num_2:int):
        # Swapping tow numbers using third variable 
        # temp=num_1
        # num_1=num_2 
        # num_2=temp 
        
        # Swapping tow numbers without using third variable Using XOR operator 
        num_1^=num_2 
        num_2^=num_1 
        num_1^=num_2
        return [num_1,num_2]
class TestApp:
    def testing_case_one(self):
        assert Solution().twoSwapping(2,3)==[3,2]
    def testing_case_two(self):
        assert Solution().twoSwapping(4,5)==[5,4]


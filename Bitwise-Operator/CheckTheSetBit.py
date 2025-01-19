# Problem Statement : Check the set bit at given position if it it set or unset we have to return boolean value 
# 
# num=4, i=2
# |
# ---> 1 0 0 
#      2 1 0
#      i------> is set we can return true 
# 
# num=4, i=1
# |
# ---> 1 0 0 
#      2 1 0
#      i------> is unSet we can return false 

class Solution:
    def checkTheSetBit(self,num:int,i:int):
        # Brute Force Approach
        # binary_value=str(bin(num))[2::][::-1]
        # return binary_value[i]=='1'
        
        
        pass
    
class TestApp:
      def testing_case_one(self):
          assert Solution().checkTheSetBit(4,2)==True 
      def testing_two_case(self):
          assert Solution().checkTheSetBit(4,1)==False 
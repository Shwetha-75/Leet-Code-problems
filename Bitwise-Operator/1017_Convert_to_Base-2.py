'''
Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".

 

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4
 

Constraints:

0 <= n <= 109
'''

import math
class Solution:
    def baseNeg2(self, n: int) -> str:
        result=''
        while n!=0:
             rem=n%(-2)
             qu=n//(-2)
             if rem<0:
                 rem=rem+2 
                 n=qu+1 
             else:
                 n=qu   
             result+=str(rem)
             
        return result[::-1] 
class TestApp:
    def testing_case_one(self):
        assert Solution().baseNeg2(2)=="110"
    def testing_case_two(self):
        assert Solution().baseNeg2(3)=="111"
    
    def testing_case_three(self):
        assert Solution().baseNeg2(4)=="100"


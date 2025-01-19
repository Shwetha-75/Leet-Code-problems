'''
Given a positive integer, check whether it has alternating bits: namely, 

if two adjacent bits will always have different values.


Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 

Constraints:

1 <= n <= 231 - 1.

'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_value=str(bin(n))[2::]
        n=len(binary_value)
        for i in range(1,n):
            if binary_value[i-1]==binary_value[i]:
                return False 
        return True  

class TestApp:
    def testing_case_one(self):
        assert Solution().hasAlternatingBits(5)==True 
    def testing_case_two(self):
        assert Solution().hasAlternatingBits(7)==False 
    def testing_case_three(self):
        assert Solution().hasAlternatingBits(11)==False 
    def testing_case_four(self):
        assert Solution().hasAlternatingBits(10)==True 
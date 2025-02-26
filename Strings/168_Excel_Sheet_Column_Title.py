'''
Given an integer columnNumber, return its corresponding 
    column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
            result=""
            while columnNumber!=0:
                  columnNumber-=1
                  rem=columnNumber%26 
                  columnNumber//=26
                  result+=chr(65+rem)
            return result[::-1] 
class TestApp:
        def testing_case_one(self):
            assert Solution().convertToTitle(1)=="A"
        def testing_case_two(self):
            assert Solution().convertToTitle(701)=="ZY"
        def testing_case_three(self):
            assert Solution().convertToTitle(28)=="AB"
        def testing_case_four(self):
            assert Solution().convertToTitle(52)=="AZ"
 
  
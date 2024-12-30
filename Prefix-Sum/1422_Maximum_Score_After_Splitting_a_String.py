'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

'''
class Solution:
        def maxScore(self, s: str) -> int:
            max_value=0
            count_zero=0
            n=len(s)
            count_one=s.count('1')
            for i in range(n-1):
                if s[i]=='0':
                    count_zero+=1
                else:
                    count_one-=1 
                current_score=count_zero+count_one
                if max_value<current_score:
                    max_value=current_score
            # for i in range(1,n):
            #     max_value=max(max_value,s[:i:].count('0')+s[i::].count('1'))
            print(max_value)
            return max_value 

class TestApp:

      def testing_case_one(self):
          assert Solution().maxScore("011101")==5
      
      def testing_case_two(self):
          assert Solution().maxScore("00111")==5 
      
      def testing_case_three(self):
          assert Solution().maxScore("1111")==3
    
      def testing_case_four(self):
          assert Solution().maxScore("00")==1
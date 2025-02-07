'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
210.5K
Submissions
438.6K
Acceptance Rate
48.0%
Topics
Companies
Hint 1
The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
Hint 2
Check that these positions have the same set of characters.
Similar Questions
Discussion (158)


'''
# Brute Force Approach 

from collections import Counter 
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter_s1=Counter(s1)
        counter_s2=Counter(s2)
        for key in counter_s1:
            if key in counter_s2 and counter_s1[key]!=counter_s2[key]: return False
            if key not in counter_s2: return False   
        
        n=len(s1)
        count=0 
        for i in range(n):
            if s1[i]!=s2[i]: count+=1
            if count>2: return False 
            
        return False if count==1 else True 

# Keep tracking of each characters at s1 and s2 
class Solution:
      def areAlmostEqual(self, s1: str, s2: str) -> bool:
          numDiff=index_1=index2=0 
          n=len(s1) 
          for i in range(n):
              if s1[i]!=s2[i]:
                  numDiff+=1 
                  if numDiff>2: return False 
                  if numDiff==1: index_1=i 
                  else: index_2=i 
   
          return s1[index_1]==s2[index_2] and s1[index_2]==s2[index_1]
      
class TestApp:
    def testing_case_one(self):
        assert Solution().areAlmostEqual("bank","kanb")==True 
    def testing_case_two(self):
        assert Solution().areAlmostEqual("abcd","dcba")==False 
    def testing_case_three(self):
        assert Solution().areAlmostEqual("caa","aaz")==False 
    def testing_case_four(self):
   
        assert Solution().areAlmostEqual("attack","defend")==False 
    def testing_case_five(self):
      
        assert Solution().areAlmostEqual("bankb","kannb")==False 
        
s1="bank"
s2="kanb"



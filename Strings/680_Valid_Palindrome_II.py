'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        n=len(s) 
        for i in range(n):
            if i==0:
                
                if s[1::]==s[1::][::-1]:
                    return True 
            elif i==n-1:
                 if s[:i:]==s[:i:][::-1]:
                     print(s[:i:],s[:i:][::-1])
                     return True 
            else:
                if s[:i:]+s[i+1::]==(s[:i:]+s[i+1::])[::-1]:
                    return True 
        return False 
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag=False 
        left=0 
        right=len(s)-1
        def helper(index):
            temp=""
            temp+=s[:index:]+s[index+1::]
            return temp==temp[::-1]
        while left<=right:
              if s[left]==s[right]:
                  left+=1 
                  right-=1 
              else:
                  flag=True 
                  break 
        if flag:
            if helper(left):
                return True 
            elif helper(right):
                return True 
            return False
            
        else:
            return True     

class TestApp:
      def testing_case_one(self):
          assert Solution().validPalindrome("aba")==True 
      def testing_case_two(self):
          assert Solution().validPalindrome("abca")==True 
      def testing_case_three(self):
          assert Solution().validPalindrome("abcd")==False 
      def testing_case_four(self):
          assert Solution().validPalindrome("abc")==False
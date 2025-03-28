'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.istitle() or word.islower()

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.title(word) or self.upper(word) or self.lower(word) 
    def title(self,word:str)->bool:
        for i in range(len(word)):
            if i==0:
                if not (ord(word[i])>=65 and ord (word[i])<=90):
                    return False 
            else:
                if not(ord(word[i])>=97 and ord(word[i])<=122):
                    return False 
        return True 
    def upper(self,word:str)->bool:
        for i in word:
            if not(ord(i)>=65 and ord(i)<=90) : return False 
        return True 
    def lower(self,word:str)->bool:
        for i in word:
             if not(ord(i)>=97 and ord(i)<=122) : return False 
        return True          
       
class TestApp:
        def testing_case_one(self):
            assert Solution().detectCapitalUse("USA")==True 
        def testing_case_two(self):
            assert Solution().detectCapitalUse("leetcode")==True 
        def testing_case_three(self):
            assert Solution().detectCapitalUse("FlaG")==False
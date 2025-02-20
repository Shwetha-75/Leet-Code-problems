'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1 
        s=list(s)
        vowels=["a","e","i","o","u",'A',"E","I","O","U"]
        while left<=right:
                while s[left] not in vowels:
                      left+=1 
                while s[right] not in vowels:
                      right-=1 
                if left<=right:
                    s[left],s[right]=s[right],s[left]
                    left+=1 
                    right-=1
        return "".join(s)
class TestApp:
    
        def testing_case_one(self):
            assert Solution().reverseVowels("IceCreAm")=="AceCreIm"
        def testing_case_two(self):
            assert Solution().reverseVowels("leetcode")=='leotcede'
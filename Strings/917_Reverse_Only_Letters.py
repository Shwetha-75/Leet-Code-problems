class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        result=[0]*n
        
        string=''
        for i in range(n):
            if(ord(s[i])>=65 and ord(s[i])<=90) or(ord(s[i])>=97 and ord(s[i])<=122):
                string+=s[i]
            else:
                result[i]=s[i]
        string=list(string)
        for i in range(n):
            if result[i]==0:
                result[i]=string.pop()
        return ''.join(result)
class TestApp:
    def testing_case_one(self):
        assert Solution().reverseOnlyLetters("ab-cd")=="dc-ba"
    def testing_case_two(self):
        assert Solution().reverseOnlyLetters("a-bC-dEf-ghIj")=="j-Ih-gfE-dCba"
    def testing_case_three(self):
        assert Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")=="Qedo1ct-eeLg=ntse-T!"
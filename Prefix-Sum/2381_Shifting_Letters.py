class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        s=list(s)
        for shift in shifts:
            if shift[-1] ==0:
                for i in range(shift[0],shift[1]+1):
                    if s[i]=='a': s[i]='z'
                    else:
                        s[i]=chr(ord(s[i])-1)
            else:
                for i in range(shift[0],shift[1]+1):
                    if s[i]=='z':
                        s[i]='a'
                    else: s[i]=chr(ord(s[i])+1)
        return ''.join(s)
class TestApp:
    def testing_case_one(self):
        assert Solution().shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]])=="ace"
    def testing_case_two(self):
        assert Solution().shiftingLetters("dztz",[[0,0,0],[1,1,1]])=="catz"       
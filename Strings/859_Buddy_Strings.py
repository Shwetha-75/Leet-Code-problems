from collections import Counter 
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # consider the length of the two strings 
        if len(s)!=len(goal): return False 
        if s==goal and len(set(s))<len(s): return True 
        result=[(char_1,char_2) for char_1,char_2 in zip(s,goal) if char_1!=char_2]
        return len(result)==2 and result[0]==result[1][::-1]


class TestApp:
    def testing_case_one(self):
        assert Solution().buddyStrings("ab","ba")==True 
    def testing_case_two(self):
        assert Solution().buddyStrings("aa","aa")==True 
    def testing_case_three(self):
        assert Solution().buddyStrings("ab","ab")==False 
    def testing_case_four(self):
        assert Solution().buddyStrings("aab","baa")==True      
                 
        
           
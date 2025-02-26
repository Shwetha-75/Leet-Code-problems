class Solution:

    def bored_chef(self,k:int,s: str) -> int: 
        strings=list(s)
        strings.sort()
        def helper(string:list[str]):
            for i in range(len(string)-1):
                if string[i]!=string[i+1]:
                   return 0 
            return 1   
        for i in range(len(strings)-k+1):
            if helper(strings[i:i+k:])==1:
                return 1 
        return 0 
class TestApp:
    def testing_case_one(self):
        assert Solution().bored_chef(3,"abaa")==1 
    def testing_case_two(self):
        assert Solution().bored_chef(1,"fghe")==1
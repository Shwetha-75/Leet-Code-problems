class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        result=""
        for i in s:
            if i=="(":
                if stack: 
                    result+=i
                stack.append(i)
            else:
                stack.pop()
                if stack:
                   result+=i 
                
        return result 

class TestApp:
    def testing_case_one(self):
        assert Solution().removeOuterParentheses("(()())(())")=="()()()"
    def testing_case_two(self):
        assert Solution().removeOuterParentheses("(()())(())(()(()))")=="()()()()(())"
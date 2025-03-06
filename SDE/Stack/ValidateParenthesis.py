class Solution:
    def validateParenthesis(self,string:str)->bool:
        stack=[]
        closed_parenthesis=[')',']','}']
        for i in string:
            if i in closed_parenthesis:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                elif i==']' and stack[-1]=='[':
                    stack.pop()
                elif i=='}' and stack[-1]=='{':
                    stack.pop()   
            else:
                stack.append(i)
        return not stack 


class TestApp:
    def testing_case_ne(self):
        assert Solution().validateParenthesis("[{()}]")==True 
    def testing_case_two(self):
        assert Solution().validateParenthesis("[[(]]")==False 
        
    def testing_case_three(self):
        assert Solution().validateParenthesis("[[()")==False 
    def testing_case_four(self):
        assert Solution().validateParenthesis("[[]]{{()}}[][]")==True 
    def testing_case_five(self):
        assert Solution().validateParenthesis("([{]})")==False 
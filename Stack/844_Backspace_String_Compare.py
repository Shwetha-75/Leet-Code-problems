class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[] 
        for i in s:
            if i=="#":
                if stack_s:stack_s.pop()
                continue 
            stack_s.append(i)
        for i in t:
            if  i=="#":
                if stack_t: stack_t.pop()
                continue 
            stack_t.append(i)
        print(stack_s,stack_t)
        return "".join(stack_s) == "".join(stack_t)


class TestApp:
    def testing_case_one(self):
        assert Solution().backspaceCompare("ab#c","ad#c")==True
    def testing_case_two(self):
        assert Solution().backspaceCompare( "a#c", "b")==False 
    def testing_case_three(self):
        assert Solution().backspaceCompare("y#fo##f","y#f#o##f")==True
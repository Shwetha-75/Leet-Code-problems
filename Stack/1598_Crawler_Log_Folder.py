class Solution:
      def minOperations(self, logs: list[str]) -> int:
            stack=[]
            for i in logs:
                if stack and i=="../":
                   stack.pop()
                   continue 
                elif i=="./" or i=="../":
                     continue 
                stack.append(i)
            return len(stack)


class TestApp:
    def testing_case_one(self):
        assert Solution().minOperations(["d1/","d2/","../","d21/","./"])==2
    
    
    def testing_case_two(self):
        assert Solution().minOperations(["d1/","d2/","./","d3/","../","d31/"])==3 
    
    
    def testing_case_three(self):
        assert Solution().minOperations(["d1/","../","../","../"])==0 
                   
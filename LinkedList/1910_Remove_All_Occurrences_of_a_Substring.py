class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        length=len(part)
        for i in s:
            stack.append(i)
            if len(stack)>=length:
                print(stack)
                while "".join(stack[-length:])==part:
                     index=length 
                     while index!=0:
                           stack.pop()
                           index-=1 
            
        return "".join(stack)
    
class Solution:
      def removeOccurrences(self, s: str, part: str) -> str:
            while part in s:
                s=s.replace(part,"",1)
            return s
    
    
    
    
class TestApp:
        def testing_case_one(self):
            assert Solution().removeOccurrences("daabcbaabcbc","abc")=="dab"
          
        def testing_case_two(self):
            assert Solution().removeOccurrences("axxxxyyyyb","xy")=="ab"
            
            
            
print([1,2,3,4,5][-3::])
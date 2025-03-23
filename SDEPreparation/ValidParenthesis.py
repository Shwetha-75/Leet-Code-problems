class Solution:
      def validateParenthesis(self,string:str):
          stack=[]
         
          for i in string:
              if stack and i==')' and stack[-1]=='(' or i==']'and stack[-1]=='[' or i=='}' and stack[-1]=='{':
                  stack.pop()
                  continue
              
              stack.append(i)
          return not stack 
      

          
class TestApp:
     def testing_case_one(self):
         assert Solution().validateParenthesis("()[{}()]")==True 
     def testing_case_two(self):
         assert Solution().validateParenthesis("[][]{[]()")==False 
     def testing_case_three(self):
         assert Solution().validateParenthesis("[][[()]][[][][][](]")==False 
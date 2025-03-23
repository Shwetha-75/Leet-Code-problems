class Solution:
      def infixToPostFixConversion(self,string:str):
            operator_stack=[]
            hash_map={'%':2,'/':2,'*':2,'+':1,'-':1,'(':3}
            result=''
            
            for i in string:
                  if i=='-' or i=='+' or i=='*' or i=='/' or i=='%' or i=='(':
                    #   checking the priority 
                      
                      if operator_stack and  hash_map[i]<hash_map[operator_stack[-1]]:
                          result+=operator_stack.pop(-1)
                          operator_stack.append(i)
                      else:
                          operator_stack.append(i)
                  elif i==')':
                        while operator_stack and operator_stack[-1]!='(':
                              result+=operator_stack.pop()
                        if operator_stack: operator_stack.pop()
                  else:
                       result+=i 
            while operator_stack:
                  result+=operator_stack.pop()
            return result 

class TestApp:
      def testing_case_one(self):
          assert Solution().infixToPostFixConversion("a+b*(c+e)")=="abce+*+"
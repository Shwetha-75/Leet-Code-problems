import math
class Solution:
      def evalRPN(self, tokens: list[str]) -> int:
            valid_operators=['+','-','/','*']
            stack=[]
            for i in tokens:
                if i in valid_operators:
                    match i:
                        case '+':
                              op2=stack.pop()
                              op1=stack.pop()
                              val=(op2)+(op1)
                              stack.append(val)
                        case '-':
                               op2=stack.pop()
                               op1=stack.pop()
                               val=(op2)-(op1)
                               stack.append(val)
                        
                        case '*':
                               op2=stack.pop()
                               op1=stack.pop()
                               val=(op2)*(op1)
                               stack.append(val)
                        
                        case '/':
                            op2=stack.pop()
                            op1=stack.pop()
                            val=int(op1/op2)
                            stack.append(val)
                else:
                    
                    stack.append(int(i))
                print(stack)
            return stack.pop()
    
    
class TestApp:
        def testing_case_one(self):
          
            assert Solution().evalRPN(["2","1","+","3","*"])==9
        def testing_case_two(self):
            assert Solution().evalRPN(["4","13","5","/","+"])==6
        
        def testing_case_three(self):
            assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])==22
'''
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

'''
class Solution:
    def parsingBooleanExpression(self,string:str):
        # Approach 1
        # boolean_values=['f','t']
        # operators=['&','|','!']
        # operator_stack=[]
        # index=1
        # operator_stack.append(string[0])
        # final_result=False
        # exp_stack=[]
        # def helper(input,operator):
        #     print(input)
        #     input=list(input)
            
        #     print(operator)
        #     if operator=='&':
                
        #         if len(input)==input.count('t'):
        #             return True 
        #         else:
        #             return False 
        #     if operator=='|':
        #         print(input.count('|'))
        #         if input.count('t')>=1:
        #             return True 
        #         else:
        #             return False 
        #     if operator=='!':
        #         if input[0]=='f':
        #             return True 
        #         else:
        #             return False 
        # while operator_stack and index< len(string):
             
        #       if string[index]==')':
                 
        #           if helper(exp_stack,operator_stack.pop()):
        #               exp_stack.clear()
        #               exp_stack.append('t')
                     
        #               final_result=True  
        #           else:
        #               exp_stack.append('f')
                      
                      
        #               final_result=False 
        #       elif string[index] in boolean_values:
        #            first=index
        #            while string[index]!=')':
        #                index+=1
        #            index-=1
                   
        #            exp_stack.append(''.join(string[first:index+1:].split(',')))
                  
        #       else:
        #           if string[index] in operators:
        #              operator_stack.append(string[index])
             
        #       index+=1
        #       print(exp_stack)
        # return final_result
        # Approach 2
        stack=[]
        result=False
        for char in string:
            if char==')':
                temp=[]
                while stack[-1]!='(':
                      temp.append(stack.pop())
                stack.pop()
                operator=stack.pop()
                if operator=='!':
                    result=not bool(1 if temp[0]=='t' else 0)
                elif operator=='&':
                    result=all([bool(1 if val=='t' else 0) for val in temp])
                elif operator=='|':
                    result=any([bool(1 if val=='t' else 0) for val in temp])
                stack.append('t' if result else 'f')
            elif char not in (',',' '):
                stack.append(char)
        return result        
def main():
    sol=Solution()
    res=sol.parsingBooleanExpression("!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))")
    print(res)
main()

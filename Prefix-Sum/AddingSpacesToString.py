class Solution:
    def addSpaces(self,s:str,spaces:list[int]):
        string_result=[]
        for i in range(len(s)):
            if i in spaces:
                string_result.append(' '+s[i])
            else:
                string_result.append(s[i])
        return ''.join(string_result)
        
        # Approach 1
        # result=list(s)
        # print(result)
        # stack=[]
        # for i in spaces:
        #     stack.append(result[i])
        #     result[i]=-1 
        # for i in range(len(result)):
        #     if result[i]==-1:
                
        #         result[i]=' '+stack.pop(0)
                
                
        # print(''.join(result))
def main():
    sol=Solution()
    result=sol.addSpaces("LeetcodeHelpsMeLearn",[8,13,15])
    print(result)
main()
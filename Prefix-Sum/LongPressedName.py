from collections import Counter
class Solution:
    def isLongPressedName(self,name:str,typed:str):
        # hash_map_name=list(dict(Counter(name)).items())
        # hash_map_typed=list(dict(Counter(typed)).items())
        # for i in range(len(hash_map_name)):
        #     if hash_map_name[i][0]!=hash_map_typed[i][0] or hash_map_name[i][1]<hash_map_typed[i][1]:
        #         return False 
        # return True
        # stack=list(typed)
        # for i in range(len(name)-1,-1,-1):
        #     print(name[i],'-',stack[-1])
        #     while stack and stack[-1]==name[i]:
                
        #         stack.pop()
        # return True if not stack else False 
        pass
        
def main():
    sol=Solution()
    result=sol.isLongPressedName("alex","aaleex")
    print(result)
main()
import sys
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map=dict(Counter(t))
        count=sum(hash_map.values())
        def helper(subString:str):
            counter=0
            
            hash_map_2=dict(Counter(subString))
           
            for key,value in hash_map.items():
                if key in hash_map_2:
                    # atleast the value as to occur 
                    if value <=hash_map_2[key]:
                        counter+=value
            
            return True if counter==count else False 
        n=len(s)
        subString=''
        min_value=sys.maxsize
        for i in range(n):
            for j in range(i,n):
                if helper(s[i:j+1:]): 
                    if len(s[i:j+1:])<min_value:
                        min_value=len(s[i:j+1:])
                        subString=s[i:j+1:]
        return subString 
def main():
    sol=Solution()
    result=sol.minWindow("aa","aa")
    print(result)
main()
class Solution:
        def numberOfSubstrings(self, s: str) -> int:
            count=0 
            n=len(s)
            for i in range(n):
                hash_map={}
                for j in range(i,n):
                    if s[j]=='a':
                        hash_map[0]='a'
                    elif s[j]=='b':
                        hash_map[1]='b'
                    else:
                        hash_map[2]='c'
                    if len(hash_map)==3:
                        count+=1 
            return count
import sys
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        valid_substrings=0 
        hash_map={'a':-1,'b':-1,'c':-1}
        n=len(s)
        for i in range(n):
            hash_map[s[i]]=i 
            flag=True  
            for j in hash_map:
                if hash_map[j]==-1:
                    flag=False 
                    break
            print(hash_map)
            if flag:
                minimum_value=sys.maxsize
                for k in hash_map:
                    minimum_value=min(minimum_value,hash_map[k])
                valid_substrings+=minimum_value+1 
                print(valid_substrings,minimum_value)
                
        return valid_substrings 
                    
class TestApp:
    def testing_case_one(self):
        assert Solution().numberOfSubstrings("abcabc")==10
    def testing_case_two(self):
        assert Solution().numberOfSubstrings("aaacb")==3 
    def testing_case_three(self):
        assert Solution().numberOfSubstrings("abc")==1 
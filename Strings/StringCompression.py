class Solution:
    def compressString(self,s:str):
        s=sorted(s)
        hash_map=dict()
        for i in s:
            if i in hash_map:
                hash_map[i]+=1 
            else:
                hash_map[i]=1 
        result=""
        for i in hash_map:
            result+=f"{i}{hash_map[i]}"
        return result 


class TestApp:
    def testing_case_one(self):
        assert Solution().compressString("abbcggppbbddee")=="a1b4c1d2e2g2p2"
    def testing_case_two(self):
        assert Solution().compressString("abbbcccdddeefff")=="a1b3c3d3e2f3"
    

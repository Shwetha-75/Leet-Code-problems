class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # word1=list(word1)
        # word2=list(word2)
        # if len(set(word1))==len(word1) and len(set(word2))==len(word2): return True 
        # # Identify the indics of repeated character 
        # i=j=0
        # n=len(word1) 
        # m=len(word2)
        # while i<n-1:
        #     if word1[i]==word1[i+1]: break 
        #     i+=1 
        # while j<m-1:
        #     if word2[j]==word2[j+1]: break 
        #     j+=1 
        # # swapping 
        # word1[i],word2[j]=word2[j],word1[i]
        # return len(set(word1))==len(word1) and len(set(word2))==len(word2)
        n=len(word1)
        word1=list(word1)
        word2=list(word2)
        m=len(word2)
        for i in range(n):
            for j in range(m):
                # swapping 
                word1[i],word2[j]=word2[j],word1[i]
                print(word1,word2)
                if len(set(word1))==len(set(word2)): return True 
        return False 
  
            
class TestApp:
        def testing_case_one(self):
            assert Solution().isItPossible("ac","b")==False 
    
        def testing_case_two(self):
            assert Solution().isItPossible("abcc","aab")==True 
        def testing_case_three(self):
            assert Solution().isItPossible("abcde","fghij")==True 
        def testing_case_four(self):
            assert Solution().isItPossible("aab","bccd")==True 
        
        
        def testing_case_five(self):
            assert Solution().isItPossible("aa","bcd")==False 
class Solution:
    def longestCommonSupersequence(self, str1: str, str2: str) -> str:
        # finding the length of the longest common sequence 
        # find out the characters which is common among both and the minimum one 
        # using dynamic programming 
        row=len(str1)
        col=len(str2) 
        matrix=[[0]*(col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if str1[i-1]==str2[j-1]:
                   matrix[i][j]=1+matrix[i-1][j-1]
                else:
                    matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
        count=0 
        result=''
        i,j=row,col
        while i>0 and j>0:
                if str1[i-1]==str2[j-1]:
                  result+=str1[i-1]
                  print(result)
                  i-=1
                  j-=1 
                elif matrix[i-1][j]>matrix[i][j-1]:
                     
                     i-=1 
                else:
                    
                    j-=1 
    
        print(result)
        return len(result)

class TestApp:
        def testing_case_one(self):
            assert Solution().longestCommonSupersequence("abac","cab")==2 
        def testing_case_two(self):
            assert Solution().longestCommonSupersequence("brute","groot")==2
        def testing_case_three(self):
            assert Solution().longestCommonSupersequence("aaaa","aaaa")==4
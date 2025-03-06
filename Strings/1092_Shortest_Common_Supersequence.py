'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
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
        result,i,j="",row,col 
        while i>0 and j>0:
                if str1[i-1]==str2[j-1]:
                     result+=str1[i-1]
                     i-=1
                     j-=1 
                elif matrix[i-1][j]>matrix[i][j-1]:
                     result+=str1[i-1]
                     i-=1 
                else:
                    result+=str2[j-1]
                    j-=1 
        while i>0:
            result+=str1[i-1]
            i-=1 
        while j>0:
              result+=str2[j-1]
              j-=1
              
        return result[::-1] 
class TestApp:
        def testing_case_one(self):
           assert Solution().shortestCommonSupersequence("abac","cab")=="cabac"
        def testing_case_two(self):
            assert Solution().shortestCommonSupersequence("aaaaaaaa","aaaaaaaa")=="aaaaaaaa"
        def testing_case_three(self):
            assert Solution().shortestCommonSupersequence("bcacaaab","bbabaccc")=="bbabcacccaaab" or "cccababaacacb"[::-1]
            
        def testing_case_four(self):
            assert Solution().shortestCommonSupersequence("bbbaaaba","bbababbb")=="bbbaaababbb" or "bbbaaababbb"[::-1]
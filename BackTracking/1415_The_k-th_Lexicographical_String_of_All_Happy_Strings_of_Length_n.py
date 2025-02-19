'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100.

'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result=self.helper(n,"",[])
        return result[k-1] if k<=len(result) else ""
    def helper(self,n:int,currentString:str,generateString:list[str]):
        if n==len(currentString):
           generateString.append(currentString[::])
           return 
        for i in "abc":
            if currentString and currentString[-1]==i: continue 
            self.helper(n,currentString+i,generateString)
        return generateString


# Optimal Approach 
class Solution:
      def getHappyString(self, n: int, k: int) -> str:
            totalHappy=3*(2**(n-1))
            if k>totalHappy: return ""
            output,low,high="",1,totalHappy
            choices="abc"
            for i in range(n):
                partSize=(high-low+1)//len(choices)
                curr=low 
                for c in choices:
                    if k in range(curr,curr+partSize):
                        output+=c
                        low=curr 
                        high=curr+partSize-1 
                        choices="abc".replace(c,"")
                    curr+=partSize 
            return output
          
         
class TestApp:
    def testing_case_one(self):
        assert Solution().getHappyString(3,9)=="cab"
    def testing_case_two(self):
        assert Solution().getHappyString(1,3)=="c"
    def testing_case_three(self):
        assert Solution().getHappyString(1,4)==""
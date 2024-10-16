'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
'''

class Solution:
    def longestHappyString(self,a:int,b:int,c:int):
        countA,countB,countC=0,0,0
        ans=''
        total=a+b+c
        for i in range(total):
            if((a>=b and a>=c and countA!=2) or (countB==2 or countC==2) and a>0):
                a-=1
                ans+="a"
                countA+=1
                countB=0
                countC=0
            elif ((b>=c and b>=a and countB!=2) or (countA==2 or countC==2) and b>0):
                b-=1
                ans+="b"
                countB+=1
                countC=0
                countA=0
            elif ((c>=a and c>=b and countC!=2) or (countA==2 or countB==2) and c>0):
                c-=1
                ans+="c"
                countC+=1
                countB=0
                countA=0
        return ans 
def main():
    sol=Solution()
    res=sol.longestHappyString(a = 7, b = 1, c = 0)
    print(res)
main()
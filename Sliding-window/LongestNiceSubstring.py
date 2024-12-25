'''
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.


Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

'''

class Solution:
    def longestNiceSubstring(self,s:str):
        def niceCheck(sub_string:str):
            for i in sub_string:
                if i.swapcase() not in sub_string: return False
            return True 
        
        result,n,max_value,list_values='',len(s),0,list(s)
        
        for i in range(n):
           
            for j in range(i,n):
                
                if niceCheck(list_values[i:j+1:]):
                    if max_value<(j-i)+1:
                        max_value=(j-i)+1
                        result=list_values[i:j+1:]
                 
        return ''.join(result)
def main():
    sol=Solution()
    result=sol.longestNiceSubstring("YazaAay")
    print(result)
main()


'''
Given a string s, return the maximum length of a 
substring
 such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.

'''

from collections import Counter
class Solution:
    def maximumLengthSubstring(self,s:str):
        
        # Sliding window concept
        # take the sliding window of variable length by incrementing right pointer by 1 
        # if the condition holds true take the max_len of each substring possible 
        # if it holds false the we will shift to other window 
        # return max_value 
        def helper(string:str):
            h_map=dict(Counter(string))
            for value in h_map.values():
                if value>2: return False 
            return True 
        
        left,right,max_value,n=0,0,0,len(s)
        
        while right<n:
              if helper(s[left:right+1:]):
                  max_value=max(max_value,(right-left)+1)
              else:
                  left+=1
              right+=1
        return max_value 

def main():
    sol=Solution()
    result=sol.maximumLengthSubstring("aaaa")
    print(result)
main()
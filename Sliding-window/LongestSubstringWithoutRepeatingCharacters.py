'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self,s:str):
        
        # sliding window 
        
        # def helper(string:str):
        #     h_map=dict(Counter(string))
        #     for value in h_map.values():
        #         if value>1: return False 
        #     return True 
        # left,right,n,max_len=0,0,len(s),0
        # while right<n:
        #      if helper(s[left:right+1:]):
        #         max_len=max(max_len,right-left+1)
        #      else:
        #          left+=1 
        #      right+=1 
        # return max_len 
        
        char_set,n,max_len,l=[],len(s),0,0
        for i in range(n):
            while s[i] in char_set:
                  print(s[i],char_set)
                  char_set.remove(s[l])
                  l+=1
                  
            char_set.append(s[i])
            max_len=max(max_len,len(char_set))
        
        return max_len
def main():
    sol=Solution()
    result=sol.lengthOfLongestSubstring("bbbbbb")
    print(result)
main()
'''
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # n=len(s)
        # traversing through each character starting from 0 unit last 2nd character
        # second iteration starts from i+1 until lst character 
        # find if there any character in substring starting from j+1 and take te palindrome in set (to keep track of unique set)
        # Brute Force Approach
        # for i in range(n-3+1):
        #     temp_left_chr=s[i]
        #     for j in range(i+1,n-1):
        #         temp=temp_left_chr+s[j]
        #         if temp_left_chr in s[j+1::]:
        #             result.add(temp+temp_left_chr)
                    
        # return len(result)
        result=set(s)
        count=0
        # for ch in result:
        #     i,j=s.index(ch),s.rindex(ch)
        #     palindrome=len(set(s[i+1:j:]))
        #     for k in range(i+1,j):
        #         palindrome.add(s[k])
        #     count+=len(palindrome)
        # take unique characters in the same sequence 
        # keep track of each character at left most and right most (find their indices )
        # take unique character and keep track of length 
        for ch in result:
            count+=len(set(s[s.index(ch)+1:s.rindex(ch):]))
        return count
class TestApp:
    def testing_case_one(self):
        assert Solution().countPalindromicSubsequence("aabca")==3
    
    def testing_case_two(self):
        assert Solution().countPalindromicSubsequence("adc")==0
    
    def testing_case_three(self):
        assert Solution().countPalindromicSubsequence("bbcbaba")==4
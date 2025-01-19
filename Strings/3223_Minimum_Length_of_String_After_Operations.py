'''
You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.

 

Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
Example 2:

Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.

 

Constraints:

1 <= s.length <= 2 * 105
s consists only of lowercase English letters.


Hint 1
Only the frequency of each character matters in finding the final answer.
Hint 2
If a character occurs less than 3 times, we cannot perform any process with it.
Hint 3
Suppose there is a character that occurs at least 3 times in the string, we can repeatedly delete two of these characters until there are at most 2 occurrences left of it.

'''

from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        # Solution 2 : Counting Approach 
        # n=len(s)
        # h_map=list(dict(Counter(s)).values())
        # for i in range(len(h_map)):
        #     if h_map[i]>=3:
        #         h_map[i]-=2 
        # return sum(h_map)
        
        # Solution 1 : Brute Force Approach 
        # n=len(s)
        # result=[0]*n
        # for i in range(n):
        #     if i==0: continue 
        #     elif i==n-1: continue 
        #     else:
        #         if s[i] in s[:i+1:] and s[i] in s[i+1::]:
        #             index_1=s[:i+1:].index(s[i])
        #             index_2=s[i+1::].index(s[i])
        #             if result[index_1]!=-1: 
        #                 result[index_1]=-1 
        #             if result[index_2]!=-1:
        #                 result[index_2]=-1 
        # return result.count(0)
        
        #  Solution 3 : Counting Approach 
        # h_map=list(dict(Counter(s)).values())
        # for i in range(len(h_map)):
        #     if h_map[i]>=3:
        #         while h_map[i]>2:
        #               h_map[i]-=2
        # return sum(h_map)
        return sum([1 if val%2 else 2 for val in Counter(s).values()])
        pass
        
class TestApp:
    def testing_count_case(self):
        assert Solution().minimumLength("abaacbcbb")==5
    def testing_count_case(self):
        assert Solution().minimumLength("aa")==2

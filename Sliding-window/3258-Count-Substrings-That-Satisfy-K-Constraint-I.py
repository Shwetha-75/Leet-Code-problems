'''
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of 
substrings
 of s that satisfy the k-constraint.

 

Example 1:

Input: s = "10101", k = 1

Output: 12

Explanation:

Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

Example 2:

Input: s = "1010101", k = 2

Output: 25

Explanation:

Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:

Input: s = "11111", k = 1

Output: 15

Explanation:

All substrings of s satisfy the k-constraint.

 

Constraints:

1 <= s.length <= 50 
1 <= k <= s.length
s[i] is either '0' or '1'.

'''

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # Initialise the counter variable to 0 and n to hold the length of the string 
        # Traverse in the loop until last index 
        # Inner loop start from  i+1 and take the count in the substring either the count of 1 or 0 should be less than equal to k
        # Increment the counter 
        count,n=0,len(s)
        for i in range(n):
           for j in range(i+1,n+1):
               if s[i:j:].count('1')<=k or s[i:j:].count('0')<=k:
                   count+=1 
                   
        return count 

class TestApp:
    def test_case_1(self):
        assert Solution().countKConstraintSubstrings("10101",1)==12
    
    def test_case_2(self):
        assert Solution().countKConstraintSubstrings("1010101",2)==25
    
    def test_case_3(self):
        assert Solution().countKConstraintSubstrings("11111",1)==15

'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
145.6K
Submissions
196.9K
Acceptance Rate
73.9%
Topics
Hash Table
String
Bit Manipulation
Counting
Companies
Hint 1
Iterate through the string from left to right. Keep track of the elements you have already seen in a set.
Hint 2
If the current element is already in the set, return that element.
Similar Questions
Discussion (27)

'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        set_value=set()
        for i in s:
            if i in set_value:
                return i 
            set_value.add(i)
        
        return None 
class TestAPp:
      def testing_case_one(self):
          assert Solution().repeatedCharacter("abccbaacz")=="c"
      def testing_case_two(self):
          assert Solution().repeatedCharacter("abcdd")=="d"
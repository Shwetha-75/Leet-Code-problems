'''
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
          
'''
# Wrong Approach
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            count_zero,count_one=0,0 
            for j in range(i,len(s)):
                if s[j]=='0': 
                    count_zero+=1 
                if s[j]=='1':
                    count_one+=1 
                if count_zero==count_one:
                    count+=1 
                print(count_zero,count_one)
        print(count)
# Wrong Approach  
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=0 
        result=[]
        if s[0]=='1':
            result.append([0,1])
        else:
            result.append([1,0])
        for i in range(1,len(s)):
            if s[i]=='1':
                result.append([result[i-1][0],result[i-1][1]+1])
            else:
                result.append([result[i-1][0]+1,result[i-1][1]])
        
        
class Solution:
      def countBinarySubstrings(self, s: str) -> int:
          count,prev,cur=0,0,1 
          for i in range(1,len(s)):
              if s[i]!=s[i-1]:
                  count+=min(prev,cur)
                  prev=cur 
                  cur=1 
              else:
                  cur+=1 
          return count+min(prev,cur)
class TestApp:
      def testing_case_one(self):
          assert Solution().countBinarySubstrings("0011000")==4
      def testing_case_two(self):
          assert Solution().countBinarySubstrings("000111")==3 
      def testing_case_four(self):
          assert Solution().countBinarySubstrings("111000")==3    
          
Solution().countBinarySubstrings("0011000")
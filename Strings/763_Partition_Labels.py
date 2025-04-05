'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

'''
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        result=[]
        ending_index,starting_index=-1,0
        hash_map={}
        for i in range(len(s)):
            
            hash_map[s[i]]=[i] 
        
        for curr_index in range(len(s)):
            if ending_index==-1:
                ending_index=hash_map[s[curr_index]][-1]
                starting_index=curr_index 
                
            if hash_map[s[curr_index]][-1]>ending_index:
                  ending_index=hash_map[s[curr_index]][-1]
                 
            if curr_index == ending_index:
                result.append(ending_index-starting_index+1)
                
                ending_index=-1
        return result
    
class TestApp:
      def testing_case_one(self):
          assert Solution().partitionLabels("ababcbacadefegdehijhklij")==[9,7,8]
      def testing_case_two(self):
          assert Solution().partitionLabels("eccbbbbdec")==[10]

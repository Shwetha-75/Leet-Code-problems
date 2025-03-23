class Solution:
     def findLongestSubString(self,string:str)->int:
         longest_sum,left,right=1,0,0 
         hash_map={}
         while right<len(string):
               
               if string[right] in hash_map:
                   del hash_map[string[left]]
                   left+=1 
                   continue
               hash_map[string[right]]=1 
               right+=1 
               longest_sum=max(longest_sum,len(hash_map))
         
         return longest_sum 
Solution().findLongestSubString("") 
class TestApp:
      def testing_case_one(self):
          assert Solution().findLongestSubString("abcabcbb")==3 
      def testing_case_two(self):
          assert Solution().findLongestSubString("bbbbb")==1 
      def testing_case_three(self):
          assert Solution().findLongestSubString("pwwkew")==3 
      
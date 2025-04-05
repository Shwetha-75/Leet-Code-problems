class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        longest_length,left,right=0,0,0
        
        while right<len(s):
              if s[right] in hash_map:
                 del hash_map[s[left]]
                 left+=1 
                 continue 
              hash_map[s[right]]=1 
              right+=1 
              longest_length=max(longest_length,len(hash_map))
        print(longest_length)
Solution().lengthOfLongestSubstring("pwwkew")
                               
            
         
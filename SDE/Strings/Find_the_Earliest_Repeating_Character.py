'''
Given a string S of length n, the task is to find the earliest repeated character in it. The earliest repeated character means, the character that occurs more than once and whose second occurrence has the smallest index.

Example:

Input: s = “geeksforgeeks” 
Output: e 
Explanation: e is the first element that repeats


Input: s = “hello geeks” 
Output: l 
Explanation: l is the first element that repeats

'''

from collections import Counter
class Solution:
    def repeatedCharacter(self,string:str):
        hash_map,max_value,value={},float('inf'),"%"
        for i in range(len(string)):
            if string[i] in hash_map:
                if i-hash_map[string[i]]<max_value:
                    max_value=i-hash_map[string[i]]
                    value=string[i]
            hash_map[string[i]]=i 
        return value 
    
            
   
   
class TestApp:
    def testing_case_one(self):
           assert Solution().repeatedCharacter("geeksforgeeks")=="e"
      
    def testing_case_two(self):
            assert Solution().repeatedCharacter("hello geeks")=="l"
            
    def testing_case_three(self):
        assert Solution().repeatedCharacter("abcd")=="%"  


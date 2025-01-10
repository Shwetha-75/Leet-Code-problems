'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.

'''
class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        
        # def helper(word:str,words2:list)->bool:
        #     word=sorted(word)
        #     for set_word in words2:
        #         i,j=0,0
        #         set_word=sorted(set_word)
        #         while i<len(word) and j<len(set_word):
        #             if word[i]<set_word[j]:
        #                i+=1
        #             elif word[i]==set_word[j]:
        #                j+=1
        #                i+=1 
        #             else:return False 
        #         if j!=len(set_word): return False 
        #     return True 
        
        # result=[] 
        # for word in words1:
        #     if helper(word,words2):
        #         result.append(word)
        # return result
        alphabets=[0]*26
        # calculating frequencies of occurrences of each character in words2 
        
        for word in words2:
       
            temp=[0]*26
            # calculating frequencies of each character in each word 
            for char in word:
                temp[ord(char)-97]+=1
          
            # taking maximum occurrences of each character in each word   
            for i in range(26):
                alphabets[i]=max(alphabets[i],temp[i])
           
        result=[]
      
        for word in words1:
            temp=[0]*26
           
            for char in word:
               temp[ord(char)-97]+=1 
            flag=True 
           
            for i in range(26):
                if temp[i]<alphabets[i]: 
                    flag=False
                    break 
            if flag:
                result.append(word)
        return result 
                
       
class TestApp:
    def testing_case_one(self):
        assert Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"])==["facebook","google","leetcode"]
    def testing_case_two(self): 
        assert Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["l","e"])==["apple","google","leetcode"]
    def testing_case_three(self):
        assert Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["lo","eo"])==["google","leetcode"]
        
'''
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5

'''

class Solution:
    def __init__(self):
        self.vowels={'a':1,'e':2,'i':1,'o':1,'u':1}
    def countOfSubstrings(self, word: str, k: int) -> int:
        n=len(word)
        count=0
        for i in range(n-(5+k)+1):
            for j in range(i,n): 
               if self.helper(word[i:j+5+k:],k):
                  print(word[i:j+5+k:],j)
                  count+=1 
        return count 
    def helper(self,string:str,k:int):
      
        count_vowel=0 
        count_consonant=0 
        for i in string:
            if i in self.vowels:
                count_vowel+=1 
            else:
                count_consonant+=1 
        return count_vowel==5 and count_consonant==k 
class Solution:
    def __init__(self):
        self.vowels={'a':1,'e':2,'i':1,'o':1,'u':1}
    
    def countOfSubstrings(self, word: str, k: int) -> int:      
        return self.helper(word,k)-self.helper(word,k+1) 
    def helper(self,string:str,k:int):
        start,end=0,0 
        valid=0 
        vowel={}
        count_consonant=0 
        while end<len(string):
                new_letter=string[end]
                if new_letter in self.vowels:
                    if new_letter not in vowel:
                       vowel[new_letter]=1 
                    else:
                       vowel[new_letter]+=1 
                else:
                    count_consonant+=1
                while len(vowel)==5 and count_consonant>=k:
                      valid+=len(string)-end
                      start_letter=string[start]
                      if start_letter in vowel:
                            vowel[start_letter]-=1 
                            if vowel[start_letter]==0:
                                del vowel[start_letter]
                      else:
                          count_consonant-=1 
                      start+=1 
                end+=1 
        return valid 
    

class TestApp:
    def testing_case_one(self):
          assert Solution().countOfSubstrings("aeioqq",1)==0 
    def testing_case_two(self):
        assert Solution().countOfSubstrings("aeiou",0)==1
    def testing_case_three(self):
        assert Solution().countOfSubstrings("ieaouqqieaouqq",1)==3    
    def testing_case_four(self):
        assert Solution().countOfSubstrings("iqeaouqi",2)==3
'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.

'''

from collections import Counter
class Solution:
    def isLongPressedName(self,name:str,typed:str):
        # hash_map_name=list(dict(Counter(name)).items())
        # hash_map_typed=list(dict(Counter(typed)).items())
        # for i in range(len(hash_map_name)):
        #     if hash_map_name[i][0]!=hash_map_typed[i][0] or hash_map_name[i][1]<hash_map_typed[i][1]:
        #         return False 
        # return True
        # stack=list(typed)
        # for i in range(len(name)-1,-1,-1):
        #     print(name[i],'-',stack[-1])
        #     while stack and stack[-1]==name[i]:
                
        #         stack.pop()
        # return True if not stack else False 
        
        index1,index2=0,0
        prev=name[0]
                
        while index1<len(name) and index2<len(typed):
              print(index1,index2)
              if name[index1]==typed[index2]:
                  prev=name[index1]
                  index1+=1
                  index2+=1
                  
              elif typed[index2]==prev:
                   index2+=1 
                   
              else: 
                  return False 
        
        while index2<len(typed):
              if typed[index2]!=prev: return False 
              index2+=1 
        return True        
def main():
    sol=Solution()
    result=sol.isLongPressedName("saeed","ssaaedd")
    print(result)
main()
'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

'''

class Solution:
    def rotateString(self,string:str,goal:str):
        # rotate=list(string[::])
        # char=rotate.pop(0)
        # rotate.append(char)
        # rotate=''.join(rotate)
        # while rotate!=string:
        #       if rotate==goal: return True
        #       rotate=list(rotate)
        #       char=rotate.pop(0)
        #       rotate.append(char)
        #       rotate=''.join(rotate)
        # return False 
        return True if (string+string).find(goal)!=-1 and len(string)==len(goal) else False 
def main():
    sol=Solution()
    result=sol.rotateString( "abcde", "cdeab")
    print(result)
main()
'''

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
94.4K
Submissions
112.6K
Acceptance Rate
83.8%
Topics
Companies
Hint 1
With the constraints, could we generate every possible string?
Hint 2
Yes we can. Now we just need to check if the string meets all the conditions.
Similar Questions
Discussion (91)

'''

import sys
class Solution:
      def smallestNumber(self, pattern: str) -> str: 
            list_value=[i+1 for i in range(len(pattern)+1)]
            result=[]
            def helper(string:str,i):
                if i==len(string):
                    result.append(string[::])
                    return 
                for j in range(i,len(string)):
                    # swap 
                    string[i],string[j]=string[j],string[i]
                    helper(string,i+1)
                    string[i],string[j]=string[j],string[i]
            
            helper(list_value,0)
            res=sys.maxsize
            
            for num in result:
                valid=True 
                for j in range(len(pattern)):
                    if pattern[j]=='D':
                        if not num[j]>num[j+1]:
                            valid=False  
                    else:
                        if not num[j]<num[j+1]:
                            valid=False 
                if valid:
                    res=min(res,int("".join(map(str,num))))
            return str(res)              
        
        
# Using monotonic stack 
class Solution:
      def smallestNumber(self, pattern: str) -> str:
            stack,num,result=[],1,""
            
            for char in pattern+"I":
                stack.append(str(num))
                num+=1 
                if char=='I':
                    while stack:
                      result+=stack.pop()
            return result 
                
         
class TestApp:
        def testing_case_one(self):
            assert Solution().smallestNumber("IIIDIDDD")=="123549876" 
        def testing_case_two(self):
            assert Solution().smallestNumber("DDD")=="4321"
                    
 
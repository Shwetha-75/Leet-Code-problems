'''

Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

Example


Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return .

Given a string , convert it to the longest possible string  made up only of alternating characters. Return the length of string . If no string  can be formed, return .

Function Description

Complete the alternate function in the editor below.

alternate has the following parameter(s):

string s: a string
Returns.

int: the length of the longest valid string, or  if there are none
Input Format

The first line contains a single integer that denotes the length of .
The second line contains string .

Constraints

Sample Input

STDIN       Function
-----       --------
10          length of s = 10
beabeefeab  s = 'beabeefeab'
Sample Output

5
Explanation

The characters present in  are a, b, e, and f. This means that  must consist of two of those characters and we must delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b), and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are consecutive e's present. Removing them would leave consecutive b's, so this fails to produce a valid string .

Other cases are solved similarly.

babab is the longest string we can create.

'''

class Solution:
    def method(self,s:str):
        # function to check the function is alternative or not 
        def helper(string:str):
        
            n=len(string)
            for i in range(1,n):
                if string[i-1]==string[i]: return False 
            return True 
        # making the copy of string 
        temp=s[::]
        # converting it to set  
        temp=list(set(temp))
        max_value=0
        n=len(temp)
        pairs=[]
        # making the possible pairs 
        for i in range(n):
            for j in range(i+1,n):
                pairs.append([temp[i],temp[j]])
        # traverse through each pairs 
        for i in pairs:
            present=""
            # make the string by considering two characters
            for j in s:
                # either any one among them is present in any two selected pair character
                # prepare the string
                if j==i[0] or j==i[1]:
                    present+=j 
            # check if the string is valid    
            if helper(present):
                # maximum length among all
                max_value=max(max_value,len(present))
        return max_value 


sol=Solution()
result=sol.method("beabeefeab")
print(result)
    
temp=""
temp.swapcase
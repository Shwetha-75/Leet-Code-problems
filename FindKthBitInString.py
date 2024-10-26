'''
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
 

Constraints:

1 <= n <= 20
1 <= k <= 2n - 1

'''

class Solution:
    def findKThBitString(self,n:int,k:int):
        # Approach ! Brute Force Approach 
        # def invert(string:str):
        #     temp=""
        #     for i in string:
        #         if i=="0": temp+="1"
        #         else:
        #             temp+="0"
        #     return temp 
        # def generateString(n):
        #     s="0"
        #     for i in range(1,n):
        #         s=s+"1"+invert(s)[::-1]
        #     return s
        # string=generateString(n)
        # return string[k-1]
    # Approach 2
       s="0"
       map={"1":'0','0':'1'}
       for i in range(1,n):
           s=s+'1'+''.join([map[i] for i in s])[::-1]
       return s[k-1]
    
def main():
    sol=Solution()
    res=sol.findKThBitString(4,11)
    print(res)
main()
'''
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

 

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
 

Constraints:

1 <= num <= 1000.

'''

class Solution:
    def countEven(self,num:int):
        count=0
        def sumDigits(n:int):
            sum_value=0
            while n>0:
                  sum_value+=n%10 
                  n//=10 
            return True if sum_value%2==0 else False 
        for i in range(2,num+1):
            if sumDigits(i): count+=1 
        return count 
def main():
    sol=Solution()
    result=sol.countEven(30)
    print(result)
main()
    
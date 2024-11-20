'''
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

 

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


'''

class Solution:
    def prefixDivBy5(self,array:list):
        # Brute Force approach 
        # def binary_to_decimal(string:str):
        #     decimal,power=0,0
        #     n=len(string)
        #     for i in range(n-1,-1,-1):
        #         if str(string[i])=="1":
        #             decimal+=(2**power)
        #         power+=1 
        #     return decimal 
        # result=[]
        
        # for i in range(len(array)):
        #     result.append(binary_to_decimal(array[0:i+1:]))
        # for i in range(len(result)):
        #     if result[i]%5==0:
        #         result[i]=True
        #     else:
        #         result[i]=False
        # return result 
        # Optimal solution 
        x=0
        result=[]
        for i in range(len(array)):
            x=(x*2+array[i])%5
            result.append(x==0)
        return result
    
def main():
    sol=Solution()
    result=sol.prefixDivBy5([0,1,1])
    print(result)
main()
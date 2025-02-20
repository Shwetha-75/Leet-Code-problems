'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

'''

# simulating 

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # converting the binary into numbers
        if len(nums)==1: return "0" if nums[0]=="1" else "1"
        def binaryToNumbers(binary:str):
            pow,sum=0,0 
            for i in reversed(binary):
                sum+=int(i)*(2**pow) 
                pow+=1 
            
            return sum
        result=[0]*len(nums)
        # converting all binary string to decimal number 
        for i in range(len(nums)):
            result[i]=binaryToNumbers(nums[i])
            # sorting it 
        result.sort()
        # finding the pattern that doe not exist 
        temp=""
        # case 1 where in we say if we didn't find the sequence 
        
        for i in range(len(result)-1):
            # sequence breaking ru;e 
            if result[i]+1!=result[i+1]:
                temp=str(bin(result[i]+1))[2::]
                # matching with the original pattern length 
                
                while len(temp)<len(nums[0]):
                    # appending the zeros 
                    temp="0"+temp
                return temp 
        # if an way I we found the sequence but there is a corner case if the nums[0] is a zero then we have the consider 
        #  the last element number +1 else the 0th index element 
        temp=str(bin(result[0]-1 if result[0]!=0 else result[-1]+1))[2::]
        while len(temp)<len(nums[0]):
                temp="0"+temp
        return temp
# Backtracking 
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        # generating possible string pattern since the set characters is [0,1] 
        def helper(n:int,currentString,result:list):
            if n==len(currentString):
                result.append(currentString[::])
                return 
            for i in "01":
                helper(n,currentString+i,result)
            return result 
        result=helper(len(nums[0]),"",[])
        # check for which pattern does not exist 
        for i in result:
            if i not in nums:
                return i
              
                
          
    
# Since this output as multiple solutions we are not gonna consider the test cases
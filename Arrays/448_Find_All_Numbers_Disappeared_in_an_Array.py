
# Negating the present elements in the same array 
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1]*=-1 
        temp=[]
        for i in range(1,n+1):
            if nums[i]<0:
                temp.append(i+1)
        return temp
    
    
# Using pointers 
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        
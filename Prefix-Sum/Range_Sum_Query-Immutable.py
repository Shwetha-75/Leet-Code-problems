# Brute Force Approach 
class NumArray:
    def __init__(self,nums:list):
        self.nums=nums  
    def sumRange(self,left:int,right:int):
        return sum(self.nums[left:right+1:])

# Optimal Approach 
class NumArray_1:
        # When we are creating an object for NumArray 
        def __init__(self,nums:list):
            # Initializing the array
            self.nums=nums 
            # calculate the previous index value and present index value ----> Update present index value
            for i in range(1,len(nums)):
                # prefix sum
                self.nums[i]+=self.nums[i-1] 
        # calculating the sum at sub array range 
        def sumRange(self,left:int,right:int):
            if left==0:
                return self.nums[right]
            return self.nums[right]-self.nums[left-1]   
def main():
    pass 
      
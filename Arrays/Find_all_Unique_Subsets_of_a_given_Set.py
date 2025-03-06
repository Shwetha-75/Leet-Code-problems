class Solution:
    def __init__(self):
        self.result=[]
    def findSubset(self,nums:list[list[int]])->list[list[int]]:
        self.helper(nums,[],0,len(nums)) 
        print(self.result)
        return self.result[1::]
    def helper(self,nums:list[int],subset:list[int],index:int,n:int):
            if index==n:
               self.result.append(subset[:])
               return
        
            self.helper(nums,subset,index+1,n)
            subset.append(nums[index])
            self.helper(nums,subset,index+1,n)
            subset.pop()
        
       

class TestApp:
    def testing_case_one(self):
        assert Solution().findSubset([1,5,6])==[[6],[5],[5,6],[1],[1,6],[1,5],[1,5,6]]
    
        

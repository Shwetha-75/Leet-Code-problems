class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        for query in queries:
            for i in range(query[0],query[1]+1):
                if nums[i]!=0:
                    nums[i]-=1 
        
        for i in nums:
            if i>0 or i<0:
                return False 
        return True 
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        difference_array=[0]*(len(nums)+1)
        for query in queries:
            difference_array[query[0]]+=1
            difference_array[query[1]+1]-=1 
        # talking prefix sum 
        for i in range(len(nums)):
            difference_array[i]+=difference_array[i-1] if i>0 else 0 
            if difference_array[i]<nums[i]:
                return False 
        return True 

class TestApp:
     def testing_case_one(self):
         assert Solution().isZeroArray([1,0,1],[[0,2]])==True 
     def testing_case_two(self):
         assert Solution().isZeroArray([4,3,2,1],[[1,3],[0,2]])==False 
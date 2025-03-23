
# Wrong Approach 
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        for i in range(len(queries)):
            for j in range(queries[0],queries[1]+1):
                if nums[j]!=0:
                    nums[j]-=queries[i][2]
            if nums.count(0)==len(nums):
                return i+1 
        return -1 
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        k=0
        total_sum=0 
        difference_array=[0]*(len(nums)+1)
        
        for i in range(len(nums)):
            while total_sum+difference_array[i]<nums[i]:
                k+=1 
                if k>len(queries):
                    return -1 
                left,right,val=queries[k-1]
                if right>=i:
                    difference_array[left]+=val 
                    difference_array[right+1]-=val 
            total_sum+=difference_array[i]
        return k 
                    
class TestApp:
    def testing_case_one(self):
        assert Solution().minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]])==2 
    def testing_case_two(self):
        assert Solution().minZeroArray([4,3,2,1],[[1,3,2],[0,2,1]])==-1
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # Brute Force Approach 
        # n=len(nums)
        # for i in range(n):
        #     if sum(nums[:i:])==sum(nums[i+1::]):
        #         return i 
        # return -1 
        current_sum,total_sum,n=0,sum(nums),len(nums)
        for i in range(n):
            current_sum+=nums[i]
            if current_sum==total_sum:
                 return i 
            total_sum-=nums[i]
        return -1
class TestApp:
    def test_case_one(self):
        assert Solution().pivotIndex([1,7,3,6,5,6])==3
    def test_case_two(self):
        assert Solution().pivotIndex([1,2,3])==-1 
    def test_case_three(self):
        assert Solution().pivotIndex([2,-1,1])==0
        
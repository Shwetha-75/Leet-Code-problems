class Solution:
        def findMiddleIndex(self, nums: list[int]) -> int:
            # Approach 2
            # Pre-computing the the right-sum
            right_sum=sum(nums)
            n=len(nums)
            left_sum=0
            for i in range(n):
                if left_sum==right_sum-nums[i]:
                    return i 
                left_sum+=nums[i]
                right_sum-=nums[i]
            return -1
            
            # PRefix Sum 
            # n=len(nums)
            # for i in range(n):
            #     if i==0:
            #         if sum(nums[i+1::])==0: return 0
            #     elif i==n-1:
            #         if sum(nums[:n-1:])==0:return n-1 
            #     else: 
            #          if sum(nums[i+1::])==sum(nums[:i:]): 
            #              return i 
            # return -1 
class TestApp:
    def testing_case_one(self):
        assert Solution().findMiddleIndex([2,3,-1,8,4])==3
    def testing_case_two(self):
        assert Solution().findMiddleIndex([1,-1,4])==2
    def testing_case_three(self):
        assert Solution().findMiddleIndex([2,5])==-1
        
                    
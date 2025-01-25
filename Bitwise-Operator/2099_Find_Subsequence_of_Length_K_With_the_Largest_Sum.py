import heapq
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        # n=len(nums)
        # result=[[i,nums[i]] for i in range(n)]
        # result.sort(key=lambda x:x[1])
        # result=result[n-k::]
        
        # return [i[1] for i in result]
        n=len(nums) 
        queue=[]
        for i in range(n):
            heapq.heappush(queue,[nums[i],i])
            if len(queue)>k:
                heapq.heappop(queue)
        heapq.heapify(queue,key=lambda x:x[0])
        return sorted(queue,key=lambda x:x[1])
        
class TestsApp:
    def testing_case_one(self):
        assert Solution().maxSubsequence([2,1,3,3],2)==[3,3]
    def testing_case_two(self):
        assert Solution().maxSubsequence([-1,-2,3,4],3)==[-1,3,4]
    def testing_case_three(self):
        assert Solution().maxSubsequence([3,4,3,3],2)==[3,4]
        
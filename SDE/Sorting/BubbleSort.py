class Solution:
    def bubbleSort(self,nums:list[int]):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    # swap
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums 


class TestApp:
        def testing_case_one(self):
            assert Solution().bubbleSort([4,3,1,2,5])==[1,2,3,4,5]
        def testing_case_two(self):
            assert Solution().bubbleSort([1,2,3,4,5])==[1,2,3,4,5]
        def testing_case_three(self):
            assert Solution().bubbleSort([5,4,3,2,1])==[1,2,3,4,5]
class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        # nums3=[]
        # for i in nums1:
        #     for j in nums2:
        #         nums3.append(i^j)
        # value=nums3[0]
        # n=len(nums3)
        # for i in range(1,n):
        #     value^=nums3[i]
        # return value
        xor_1,xor_2,len_1,len_2=0,0,len(nums1),len(nums2) 
        if len_2 %2:
            for num in nums1:
                xor_1^=num 
        if len_1 %2:
            for num in nums2:
                xor_2^=num
        return xor_1^xor_2
class TestApp:
    def testing_case_one(self):
        assert Solution().xorAllNums([2,1,3],[10,2,5,0])==13
    def testing_case_two(self):
        assert Solution().xorAllNums([1,2],[3,4])==0
        
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        def helper(arr:list,value:int):
            for i in arr:
                if i>value:
                    return i 
            return -1 
        result=[]
        for i in nums1:
            index=nums2.index(i)
            result.append(helper(nums2[index+1::],i))
        return result

class TestApp:
    def testing_case_one(self):
        assert Solution().nextGreaterElement([4,1,2],[1,3,4,2])==[-1,3,-1]
    
    def testing_case_two(self):
        assert Solution().nextGreaterElement([2,4],[1,2,3,4])==[3,-1]
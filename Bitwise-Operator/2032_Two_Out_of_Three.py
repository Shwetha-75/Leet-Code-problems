class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        result=[]
        nums1,nums2,nums3=set(nums1),set(nums2),set(nums3)
        numbers=set()
        numbers=numbers.union(nums1).union(nums2).union(nums3)
        for i in numbers:
            if (i in nums1)and (i in nums2) or (i in nums2) and(i in nums3) or (i in nums1) and (i in nums3):
                result.append(i)
        return result 
            
        
        # for i in nums1:
        #     if i in nums2 or i in nums3:
        #         if i not in result:
        #            result.append(i)
        # for i in nums2:
        #     if i in nums1 or i in nums3:
        #         if i not in result:
        #            result.append(i)
        # for i in nums3:
        #     if i in nums1 or i in nums2:
        #         if i not in result:
        #            result.append(i)
        
                   
                   
        return result

class TestApp:
    def testing_case_one(self):
        assert Solution().twoOutOfThree([1,1,3,2],[2,3],[3])==[3,2]
    def testing_case_two(self):
        assert Solution().twoOutOfThree([3,1],[2,3],[1,2])==[2,3,1]
    def testing_case_three(self):
        assert Solution().twoOutOfThree([1,2,2],[4,3,3],[5])==[]
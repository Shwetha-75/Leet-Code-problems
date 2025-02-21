from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result=[]
        hash_map=Counter(nums)
        count=1
        while count<=len(nums):
              if count not in hash_map:
                  result.append(count)
              count+=1 
        return result 
# using set 

class Solution:
        def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            result=[0]*(len(nums))
            for i in nums:
                if result[i-1]==0:
                    result[i-1]=i 
            res=[]
            for i in range(len(nums)):
                if result[i]==0:
                    res.append(i+1)
            return res
                     
        
class TestApp:
        def testing_case_one(self):
            assert Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])==[5,6]
        def testing_case_two(self):
            assert Solution().findDisappearedNumbers([1,1])==[2]    



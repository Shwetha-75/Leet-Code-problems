# Brute Force Approach 
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Keep Tracking the count of every frequencies 
        for i in nums:
            count=0 
            for j in nums:
                if i==j:
                    count+=1 
            if count>len(nums)//2:
                return i 
        return -1
# Better Approach : Using hash_map 
from collections import defaultdict
class Solution:
      def majorityElement(self, nums: list[int]) -> int:
          hash_map=defaultdict(int)
          for i in nums:
              hash_map[i]+=1 
          for key,value in hash_map.items():
              if value>len(nums)//2:
                  return key 
          return -1 
# Boyer Moore Algorithm 
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Keep Track of majority element frequency 
        count,element=0,-1 
        for i in nums:
            if count==0:
                element=i 
                count=1 
            elif i==element:
                 count+=1 
            else:
                count-=1 
        ele_count=0
        for i in nums:
            if i==element:
                ele_count+=1 
        return element if ele_count>len(nums)//2 else -1 
class TestApp:
      def testing_case_one(self):
          assert Solution().majorityElement([3,2,3])==3 
      def testing_case_two(self):
          assert Solution().majorityElement([2,2,1,1,1,2,2])==2 
      def testing_case_three(self):
          assert Solution().majorityElement([1,1,1,2,2,5,5,6,6,6])==-1 
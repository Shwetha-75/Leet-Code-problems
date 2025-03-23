# Brute Force Approach 
class Solution:
      def twoSum(self, nums: list[int], target: int) -> list[int]:
       
          for i in range(len(nums)-1):
              for j in range(i+1,len(nums)):
                  if nums[i]+nums[j]==target:
                      return [i,j]
          return [-1,-1]
      
class Solution:
      def twoSum(self, nums: list[int], target: int) -> list[int]:
          hash_map={}
          for i in range(len(nums)):
              if target-nums[i] in hash_map:
                  return [hash_map[target-nums[i]],i]
              
              hash_map[nums[i]]=i 
          return [-1,-1]
class TestApp:
      def testing_case_one(self):
          assert Solution().twoSum([2,7,11,15],9)==[0,1]
      def testing_case_two(self):
          assert Solution().twoSum([3,2,4],6)==[1,2]
      def testing_case_three(self):
          assert Solution().twoSum([3,3],6)==[0,1]
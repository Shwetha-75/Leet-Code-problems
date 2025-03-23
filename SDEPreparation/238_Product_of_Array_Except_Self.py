from functools import reduce
class Solution:
          def productExceptSelf(self, nums: list[int]) -> list[int]:
            #   taking the count of zeros 
            count_zeros=nums.count(0)
            if count_zeros>1:
                return [0]*len(nums)
            elif count_zeros==1:
                 index=nums.index(0)
                 product=1
                 for i in range(len(nums)):
                     if i==index: continue
                     product*=nums[i]
                 result=[0]*len(nums)
                 result[index]=product 
                 return result 
            else:
                product=reduce(lambda x,y:x*y,nums)
                result=[]
                for i in nums:
                    result.append(product//i)
                return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().productExceptSelf([1,2,3,4])==[24,12,8,6] 
      def testing_case_two(self):
          assert Solution().productExceptSelf([-1,1,0,-3,3])==[0,0,9,0,0]
      def testing_case_three(self):
          assert Solution().productExceptSelf([1,1,0,9,6,0])==[0,0,0,0,0,0]


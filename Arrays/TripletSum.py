class Solution:
      def findAllTriplets(self,nums:list[int],sum:int):
            result=set()
            n=len(nums)
            for i in range(n-2):
              for j in range(i+1,n-1):
                  for k in range(j+1,n):
                      if nums[i]+nums[j]+nums[k]==sum:
                             result.add(nums[i])
                             result.add(nums[j])
                             result.add(nums[k])
                             
                               
            print(len(result))
            return result
    
class TestApp:
     def testing__case_one(self):
         assert Solution().findAllTriplets([10, 5,5,5,2],12)=={5,5,2}
     def testing_case_two(self):
         assert Solution().findAllTriplets([1,2,3,1,2,3],6)=={1,2,3}
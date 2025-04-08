class Solution:
        def minimumOperations(self, nums: list[int]) -> int:
            def helper(start:int):
                arr=set()
                for i in nums[start:]:
                    if i in arr:
                        return False 
                    arr.add(i)
                return True 
            count=0 
            for i in range(0,len(nums),3):
                if helper(i):
                    return count 
                count+=1 
            return count 

class TestApp:
      def testing_case_one(self):
          assert Solution().minimumOperations([1,2,3,4,2,3,3,5,7])==2 
      def testing_case_two(self):
          assert Solution().minimumOperations([4,5,6,4,4])==2 
      def testing_case_three(self):
          assert Solution().minimumOperations([6,7,8,9])==0
                    
      def testing_case_four(self):
          assert Solution().minimumOperations([1,2,2,2,2,2,1])==2
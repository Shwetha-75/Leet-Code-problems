class Solution:
    
     def findNumberOfOperations(self,nums:list[int],queries:list[list[int]])->int:
            count=0 
            if nums.count(0)==len(nums):
                    return count
            for query in queries:
                for i in range(query[0],query[1]+1):
                     nums[i]=nums[i]-query[2] if nums[i]>query[2] else 0
                count+=1 
                if nums.count(0)==len(nums):
                    return count 
                
            return -1 
class TestApp:
      def testing_case_one(self):
          assert Solution().findNumberOfOperations([2,0,2],[[0,2,1],[0,2,1],[1,1,3]])==2
          
      def testing_case_two(self):
          assert Solution().findNumberOfOperations([4,3,2,1],[[1,3,2],[0,2,1]])==-1 
          
      def testing_case_three(self):
          assert Solution().findNumberOfOperations([2],[[0,0,3],[0,0,3],[0,0,4],[0,0,1],[0,0,2],[0,0,5],[0,0,4],[0,0,5]])==1
          
      def testing_case_four(self):
          assert Solution().findNumberOfOperations([0],[[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]])==0
      def testing_case_five(self):
          assert Solution().findNumberOfOperations([0,8],[[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]])==3
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x:x[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1][1]>=intervals[i][0]:
               result[-1]=[result[-1][0],max(result[-1][1],intervals[i][1])]
            else:
                result.append(intervals[i])
        return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().merge([[1,3],[2,6],[8,10],[15,18]])==[[1,6],[8,10],[15,18]]
      def testing_case_two(self):
          assert Solution().merge([[1,4],[4,5]])==[[1,5]]
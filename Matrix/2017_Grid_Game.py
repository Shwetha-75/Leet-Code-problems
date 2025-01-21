import sys
class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        first_row_sum=sum(grid[0])
        second_row=0
        min_value=sys.maxsize 
        for i in range(len(grid[0])):
            first_row_sum-=grid[0][i]
            min_value=min(min_value,max(second_row,first_row_sum))
            second_row+=grid[1][i]
        return min_value


class TestApp:
    def testing_case_one(self):
        assert Solution().gridGame([[2,5,4],[1,5,1]])==4
    def testing_case_two(self):
        assert Solution().gridGame([[3,3,1],[8,5,2]])==4
    def testing_case_three(self):
        assert Solution().gridGame([[1,3,1,15],[1,3,3,1]])==7
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        row=len(grid)
        col=len(grid[0])
        ones_rows=[]
        one_columns=[] 
        for i in grid:
            ones_rows.append(i.count(1))
        for i in range(col):
            count=0
            for j in range(row):
                if grid[j][i]==1:
                 count+=1 
            one_columns.append(count)
        
        
        for i in range(row):
            for j in range(col):
                count_ones_rows=ones_rows[i]
                count_ones_col=one_columns[j]
                count_zeros_rows=col-count_ones_rows
                count_zeros_cols=row-count_ones_col 
                grid[i][j]=count_ones_rows+count_ones_col-count_zeros_rows-count_zeros_cols

        return grid 
class TestApp:
      def testing_case_one(self):
          assert Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])==[[0,0,4],[0,0,4],[-2,-2,2]]
      def testing_case_two(self):
          assert Solution().onesMinusZeros([[1,1,1],[1,1,1]])==[[5,5,5],[5,5,5]]                                                                                                       
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                
    
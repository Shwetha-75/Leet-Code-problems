class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter=0 
        # corner cases whe we have only on row and one col 
        if len(grid)==1 and len(grid[0])==1:
            return 4 
        # only one row and multiple columns 
        if len(grid)==1:
            return 2*grid[0].count(1)+2 
        if len(grid[0])==1:
            for i in grid:
                if i[0]==1:
                    perimeter+=1 
            return perimeter*2+2 
        row=len(grid)
        column=len(grid[0])
        for i in range(row):
            for j in range(column):
                if i==0 and grid[i][j]==1:
                    if j==0:
                        perimeter+=2 
                        if grid[i][j+1]==0:
                             
                            perimeter+=1 
                        if grid[i+1][j]==0:
                            perimeter+=1 
                    elif j==column-1:
                         perimeter+=2 
                         if grid[i+1][j]==0: 
                             perimeter+=1 
                         if grid[i][j-1]==0:
                             perimeter+=1 
                    else:
                        perimeter+=1 
                        if grid[i][j-1]==0:
                            perimeter+=1 
                        if grid[i][j+1]==0:
                            perimeter+=1    
                        if grid[i+1][j]==0:
                            perimeter+=1 
                elif i==row-1 and grid[i][j]==1:
                     if j==0:
                         perimeter+=2 
                         if grid[i-1][j]==0:
                             perimeter+=1 
                         if grid[i][j+1]==0:
                             perimeter+=1
                           
                     elif j==column-1:
                         perimeter+=2 
                         if grid[i-1][j]==0:
                             perimeter+=1 
                         if grid[i][j-1]==0:
                             perimeter+=1 
                     else:
                         perimeter+=1 
                         if grid[i][j-1]==0:
                             perimeter+=1 
                         if grid[i][j+1]==0:
                             perimeter+=1 
                         if grid[i-1][j]==0:
                             perimeter+=1 
                elif (j==0 or j==column-1) and (i<row-1 and i>0 ) and grid[i][j]==1:
                   
                    if j==0:
                        perimeter+=1 
                        if grid[i-1][j]==0:
                            perimeter+=1 
                        if grid[i+1][j]==0:
                            perimeter+=1 
                        if grid[i][j+1]==0:
                            perimeter+=1 
                    if j==column-1:
                        perimeter+=1 
                        if grid[i+1][j]==0:
                            perimeter+=1 
                        if grid[i-1][j]==0:
                            perimeter+=1 
                        if grid[i][j-1]==0:
                            perimeter+=1 
                else:
                    if grid[i][j]==1:
                       if grid[i-1][j]==0:
                           perimeter+=1 
                       if grid[i][j-1]==0:
                           perimeter+=1 
                       if grid[i][j+1]==0:
                           perimeter+=1 
                       if grid[i+1][j]==0:
                           perimeter+=1 
        
        return perimeter 
class TestApp:
      def testing_case_one(self):
          assert Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])==16 
      def testing_case_two(self):
          assert Solution().islandPerimeter([[1]])==4
      def testing_case_three(self):
          assert Solution().islandPerimeter([[1,1,0,0,0]])==6
      def testing_case_four(self):
          assert Solution().islandPerimeter([[1],[1],[1],[0],[0]])==8
                        
                
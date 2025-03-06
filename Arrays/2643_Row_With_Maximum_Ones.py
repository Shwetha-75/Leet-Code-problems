# Brute Force Approach 
class Solution:
        def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
            max_count,row,col=0,len(mat),len(mat[0])
            index=-1
            for i in range(row):
                count=0 
                for j in range(col):
                    if mat[i][j]==1:
                       count+=1 
                if max_count<count:
                    index=i 
                    max_count=count
            return index

# Optimized Approach using Binary Search 

class Solution:
        def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
            max_count=0
            index=-1 
            col=len(mat[0])
            row=len(mat)
            for i in range(row):
                temp=self.binarySearchApproach(mat[i],0,col-1)
                if temp!=-1:
                  count=col-temp
                  if max_count<count:
                      index=i 
                      max_count=count 
            return index
                   
                     
        def binarySearchApproach(self,nums:list[int],left:int,right:int)->int:
            index=-1 
            while left<=right:
                  mid=left+(right-left)//2 
                  if nums[mid]==1:
                      index=mid 
                      right=mid-1 
                  else:
                      left=mid+1 
            return index

class TestApp:
        def testing_case_one(self):
            assert Solution().rowAndMaximumOnes([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]])==2 
        def testing_case_two(self):
            assert Solution().rowAndMaximumOnes([[0,0,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,0]])==1
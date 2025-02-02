class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows==0: return []
        if numRows==1: return [[1]]
        result=[]
        for i in range(numRows):
            row=[1]*(i+1)
            if i>=2:
                for j in range(1,i):
                    row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result 

    
class TestApp:
    def testing_case_one(self):
        assert Solution().generate(5)==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
    def testing_case_two(self):
        assert Solution().generate(1)==[[1]]
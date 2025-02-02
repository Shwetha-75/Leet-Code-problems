class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1,1]
        result=[]
        for i in range(rowIndex+1):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result[rowIndex]
    
class TestApp:
    def testing_case_one(self):
        assert Solution().getRow(3)==[1,3,3,1]
    def testing_case_two(self):
        assert Solution().getRow(1)==[1,1]
    def testing_case_three(self):
        assert Solution().getRow(0)==[1]
    
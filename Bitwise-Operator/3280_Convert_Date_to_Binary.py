class Solution:
    def convertDateToBinary(self, date: str) -> str:
        array=date.split("-")
        for i in range(3):
            array[i]=str(bin(int(array[i])))[2::]
        return "-".join(array)
class TestApp:
    
    def testing_case_one(self):
        assert Solution().convertDateToBinary("2080-02-29")=="100000100000-10-11101"
    
    def testing_case_two(self):
        assert Solution().convertDateToBinary("1900-01-01")=="11101101100-1-1"
    
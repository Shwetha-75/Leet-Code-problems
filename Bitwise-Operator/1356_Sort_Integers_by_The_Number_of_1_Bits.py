class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        binary=[]
        for i in arr:
            binary.append([i,str(bin(i))[2::].count("1")])
        binary.sort(key=lambda x:(x[0]))
        binary.sort(key=lambda x:(x[1]))       
        result=[i[0] for i in binary]
        return result 

class TestApp:
    def testing_case_one(self):
        assert Solution().sortByBits([0,1,2,3,4,5,6,7,8])==[0,1,2,4,8,3,5,6,7] 
    
    def testing_case_two(self):
        assert Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1])==[1,2,4,8,16,32,64,128,256,512,1024]
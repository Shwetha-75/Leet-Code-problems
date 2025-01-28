class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        array=[0,0]
        # convert given number into binary
        result=""
        while n!=0:
            result+=str(n%2)
            n//=2 
        n=len(result)
        # counting at even length
        for i in range(0,n,2):
            if result[i]=="1": 
                array[0]+=1 
        for i in range(1,n,2):
            if result[i]=="1":
                array[1]+=1 
        return array 


class TestApp:
    def testing_case_one(self):
        assert Solution().evenOddBit(50)==[1,2]
    
    def testing_case_two(self):
        assert Solution().evenOddBit(2)==[0,1]
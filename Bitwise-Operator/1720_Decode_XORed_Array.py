class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        n=len(encoded)
        originalArray=[0]*(n+1)
        originalArray[0]=first 
        encoded.insert(0,0)
        for i in range(1,n+1):
            originalArray[i]=encoded[i]^originalArray[i-1]
        return originalArray


class TestApp:
    def testing_case_one(self):
        assert Solution().decode([1,2,3],1)==[1,0,2,1]
    def testing_case_two(self):
        assert Solution().decode([6,2,7,3],4)==[4,2,0,7,4]
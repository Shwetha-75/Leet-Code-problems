class Solution:
    def singleDigit(self,n:int):
        if n<10: return n 
        temp=n 
        sum=0
        while temp!=0:
              sum+=temp%10 
              temp//=10 
        return self.singleDigit(sum)
sol=Solution()
result=sol.singleDigit(777)
print(result)
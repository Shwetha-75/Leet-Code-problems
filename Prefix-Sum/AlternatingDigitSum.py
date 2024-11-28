class Solution:
    def alternateDigitSum(self,n:int):
        index=0 
        sum=0
        def reverse_digit(number):
            temp=0 
            while number!=0:
                  rem=number%10
                  number//=10
                  temp=temp*10+rem 
            return temp 
        n=reverse_digit(n)
        while n!=0:
            rem=n%10
            print(rem)
            n//=10 
            if index%2==0:
                sum+=rem 
            else: sum-=rem
            index+=1
        return sum 
def main() :
    sol=Solution()
    res=sol.alternateDigitSum(10)
    print(res)
main()
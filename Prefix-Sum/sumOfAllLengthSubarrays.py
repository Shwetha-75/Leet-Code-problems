class Solution:
    def sumOddLengthSubarrays(self,arr:list[int]):
        # Brute Force Approach 
        # sum_value=0
        # n=len(arr)
        # for i in range(n):
        #     for j in range(i,n):
        #         temp=arr[i:j+1:]
        #         if len(temp)%2!=0:
        #             sum_value+=sum(temp)
        
        # return sum_value 
        
        # Optimal Approach 
        sum_value=0
        n=len(arr)
        for i in range(n):
            value=arr[i]
            l,r=i,n-i-1
            sum_value+=value*(l//2+1)*(r//2+1)
            sum_value+=value*((l+1)//2)*((r+1)//2)
        return sum_value
            
def main():
    sol=Solution()
    result=sol.sumOddLengthSubarrays([10,11,12])
    print(result)
main()
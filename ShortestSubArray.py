import sys
class Solution:
    def shortestSubArray(self,nums:list,k:int):
        n=len(nums)
        min_len=sys.maxsize
        for i in range(n):
            temp=nums[i]
            for j in range(i,n):
                temp|=nums[j]
                print(temp)
                if temp>=k:
                    min_len=min(min_len,len(nums[i:j+1:]))
                    
        if min_len==sys.maxsize:
            return -1 
        else: return min_len
def main():
    sol=Solution()
    result=sol.shortestSubArray([1,2,32,21],55)
    print(result)
main()
class Solution:
    def isArraySpecial(self,nums:list[int],queries:list[list[int]]):
        def checkParity(arr:list[int]):
            n=len(arr)
            for i in range(1,n):
                
                if (arr[i-1]%2==0 and arr[i]%2==0) or (arr[i-1]%2!=0 and arr[i]%2!=0):
                    return False 
            return True 
        
        result=[]
        for query in queries:
            
            result.append(checkParity(nums[query[0]:query[1]+1:]))
        return result 
def main():
    sol=Solution()
    result=sol.isArraySpecial([3,4,1,2,6],[[0,4]])
    print(result)
main()
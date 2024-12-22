class Solution:
    def subarraySum(self,nums:list[int],k:int):
        
        sum,left,right,n,max_len=0,0,0,len(nums),0
        while left<=right and right<n and left<n:
            sum+=nums[right]
            print(sum)
            if sum==k: 
              
               max_len+=1
                  
            elif sum>k:
                sum-=nums[left]
                if  sum==k: max_len+=1
            
                left+=1
            
            right+=1   
            
                 
           
        return max_len
def main():
    sol=Solution()
    result=sol.subarraySum([1,2,3],3)
    print(result)
main()
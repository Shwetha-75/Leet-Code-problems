class Solution:
      def subarraySum(self,nums:list[int],k:int):
        #   Brute Force Approach
        #   count,n=0,len(nums)
        #   for i in range(n):
        #       temp=0
        #       for j in range(i,n):
        #           temp+=nums[j]  
        #           if temp==k:
        #               count+=1  
                  
        #   return count 
        # Prefix sum Approach 
        count=0
        # for i in range(1,len(nums)):
        #     nums[i]+=nums[i-1]
        # hash_map={0:1}
        # for i in nums:
        #     if i-k in hash_map:
                
        #         count+=1
        #     if i not in hash_map:
        #         hash_map[i]=1
        #     else: hash_map[i]+=1
        # return count
def main():
    sol=Solution()
    result=sol.subarraySum([1,2,3],3)
    print(result)
main()
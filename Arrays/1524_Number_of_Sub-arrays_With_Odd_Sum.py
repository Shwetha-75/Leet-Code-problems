class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        count=0
        result=[] 
        for i in range(len(arr)):
            currentSum=0
            for j in range(i,len(arr)):
                currentSum+=arr[j]
                if currentSum%2!=0:
                    count+=1 
        return count
    
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prefixSum,count,odd_count,even_count=0,0,0,1 
        for i in arr:
            prefixSum+=i 
            if prefixSum%2==0:
                count+=odd_count
                even_count+=1 
            else:
                count+=even_count
                odd_count+=1 
        return count
                
        
        
class  TestApp:
       def testing_case_one(self):
           assert Solution().numOfSubarrays([1,3,5])==4
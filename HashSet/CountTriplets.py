class Solution:
      def countTriplets(self,arr:list[int],r:int):
            count=0 
            for i in range(len(arr)):
                stack=[arr[i]]
                for j in range(i+1,len(arr)):
                    if arr[j]//stack[-1]==r:
                        stack.append(arr[j])
                        for k in range(j+1,len(arr)):
                           
                           if arr[k]//stack[-1]==r:
                               count+=1 
                        stack.pop()
            return count 
from collections import Counter
# Optimized Approach
class Solution:
      def countTriplets(self,arr:list[int],r:int):
            prev_hash={}
            current_hash=dict(Counter(arr))
            sum=0 
            for a in arr:
                current_hash[a]-=1 
                if (a//r) in prev_hash and a*r in current_hash:
                    sum+=prev_hash[a//r]*current_hash[a*r]
                if a in prev_hash:
                    prev_hash[a]+=1 
                else:
                    prev_hash[a]=1 
            return sum     
            
              
class TestApp:
        def testing_case_one(self):
            assert Solution().countTriplets([1,2,2,4],2)==2 
        def testing_case_two(self):
            assert Solution().countTriplets([1,5,5,25,125],5)==4   
                     
'''


You are given an array with unique elements of stalls[], which denote the position of a stall. 
You are also given an integer k which denotes the number of aggressive cows. 
Your task is to assign stalls to k cows such that the minimum distance 
between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.
Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.
Constraints:
2 <= stalls.size() <= 106
0 <= stalls[i] <= 108
2 <= k <= stalls.size()



'''

# Brute Force Approach 


class Solution:
      def findTheCows(self,arr:list[int],dist:int,cows:int):
          last=arr[0]
          count=1
          for i in range(1,len(arr)):
              if arr[i]-last>=dist:
                  count+=1 
                  last=arr[i]
              if count>=cows:
                  return True 
          return True if count>=cows else False 
      def findTheMaximumStall(self,stalls:list[int],cows:int):
          stalls.sort()
          n=len(stalls)
          if cows==2:
             return stalls[n-1]-stalls[0]
          maximum=stalls[n-1]
          min=stalls[0]
          max_value=float('-inf')
          for i in range(1,maximum-min+1):
              if self.findTheCows(stalls,i,cows):
                  max_value=max(max_value,i)
          return max_value 

class Solution:
      def findTheCows(self,arr:list[int],dist:int,cows:int):
            last=arr[0]
            count=1 
            for i in range(1,len(arr)):
                  if arr[i]-last>=dist:
                      count+=1 
                      last=arr[i] 
                  if count>=cows: return True 
            return True if count>=cows else False 
      def findTheMaximumStall(self,stalls:list[int],cows:int):
          stalls.sort()
          n=len(stalls)
          if cows==2: 
              return stalls[n-1]-stalls[0] 
          left,right=1,stalls[n-1] 
          max_value=0
          while left<=right: 
                mid=(left+right)//2 
                if self.findTheCows(stalls,mid,cows):
                    max_value=mid 
                    left=mid+1 
                else:
                    right=mid-1   
          return max_value  
class TestApp:
    def testing_case_one(self):
        assert Solution().findTheMaximumStall([0,3,4,7,9,10],4)==3
    def testing_case_two(self):
        assert Solution().findTheMaximumStall([2, 12, 11, 3, 26, 7],5)==1       
    def testing_case_three(self):
        assert Solution().findTheMaximumStall([1,5,17],2)==16
    def testing_case_four(self):
        assert Solution().findTheMaximumStall([40,47],2)==7
    
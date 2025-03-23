'''
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

 

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
 

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012
'''

class Solution:
      def maximumCandies(self, candies: list[int], k: int) -> int:
          
          max_element=max(candies)
          right=max_element 
          left=1 
          global tempArr
          while left<right:
                mid=((right-left)+left)//2 
                
                tempArr=self.helper(candies[::],[0]*k,mid)
              
                temp=tempArr.count(0)
                print(tempArr)
                if temp==0:
                    left=mid+1
                else:
                    right=mid-1
        
          return 0 if tempArr.count(0)!=0 else mid 

      def helper(self,nums:list[int],result:list[int],target:int):
          index=0 
          i=0
          while index<len(nums) and i<len(result):
              if nums[index]<target:
                  index+=1
             
              if index <len(nums) and nums[index]>=target and i<len(result):
                  nums[index]-=target 
                  result[i]=target 
                  
                  i+=1 
          return result 
class Solution:
        def maximumCandies(self, candies: list[int], k: int) -> int:
            left,right=1,max(candies)
            resultValue=0
            while left<=right:
                mid=(left+(right-left)//2)
                result=self.helper(candies[::],mid)
              
                if result>=k:
                    resultValue=mid 
                    left=mid+1
                else:
                    right=mid-1 
            print(resultValue)
            return resultValue  
        def helper(self,nums:list[int],target:int):
            index=0 
            count=0 
            while index<len(nums):
                    print(nums)
                    if nums[index]>=target:
                       count+=1 
                       nums[index]-=target 
                    else:
                        index+=1 
            return count    
class Solution:
        def maximumCandies(self, candies: list[int], k: int) -> int:
            left,right=1,max(candies)
            result=0 
            while left<=right:
                  mid=((right-left)//2+left)
                  if self.helper(candies,mid,k):
                      result=mid 
                      
                      left=mid+1 
                  else:
                      right=mid-1 
                
            return result
        def helper(self,candies:list[int],mid:int,k:int):
            count=0 
            for i in range(len(candies)):
                count+=candies[i]//mid 
                if count>=k:
                    return True 
            return count>=k
Solution().maximumCandies([5,6,4,10,10,1,1,2,2,2],9)
class TestApp:
    def testing_case_one(self):
        assert Solution().maximumCandies([5,8,6],4)==4
    def testing_case_two(self):
        assert Solution().maximumCandies([5,8,6],3)==5 
    def testing_case_three(self):
        assert Solution().maximumCandies([2,5],11)==0
    def testing_case_four(self):
        assert Solution().maximumCandies([1,2,3,4,10],5)==3
    def testing_case_fiev(self):
        assert Solution().maximumCandies([9,10,1,2,10,9,9,10,2,2],3)==10
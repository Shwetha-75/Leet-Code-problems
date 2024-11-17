'''
Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107.

'''

class PrefixSumSolution:
    def countOfSubArraySumEqualsToK(self,array:list,k:int):
        # Wrong Approach 
        # temp=array[::]
        # for i in range(1,len(array)):
        #     array[i]+=array[i-1]
        # # print(array)
        # print(array)
        # count=0 
        # for i in array:
            
        #     if abs(k-i) in temp:
        #         count+=1 
        # return count
        #  
        count=0
        prefixSum=0 
        hash_map={0:1}
        for i in array:
            prefixSum+=i 
            if prefixSum-k in hash_map:
                count+=hash_map[prefixSum-k]
            if prefixSum in hash_map: 
                hash_map[prefixSum]+=1
            else: hash_map[prefixSum]=1 
        return count
            

class Solution:
    def countOfSubArraySumEqualsToK(self,array:list,k:int):
        # Brute force Approach 
        # Time complexity: O(n^2)
        count=0
        for i in range(len(array)):   #O(N)
            for j in range(i,len(array)):  #O(N)
                if sum(array[i:j+1:])==k:
                    count+=1
        return count 
        
        
        
def main():
    sol=Solution()
    result=sol.countOfSubArraySumEqualsToK([1,2,3],3)
    # print(result)
    object=PrefixSumSolution()
    result=object.countOfSubArraySumEqualsToK([1,2,1,2,1],3)
    print(result)
main()
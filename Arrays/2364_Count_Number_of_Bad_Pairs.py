# class Solution:
#     def countBadPairs(self, nums: list[int]) -> int:
        
#         count,n=0,len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if j-i!=nums[j]-nums[i]: count+=1 
#         return count 
# Calculating the total number of good pairs 
'''
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a 
bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109.

'''
# Brute Force Approach: Time Complexity: O(n2) and space complexity: O(1) 
class Solution:
        def countBadPairs(self, nums: list[int]) -> int:
            count,n=0,len(nums)
            for i in range(n-1):
                for j in range(i+1,n):
                    if j-i!=nums[j]-nums[i]: count+=1 
            return count 
        
# Using hash_map: TC: O(n) and Space Complexity O(n)
 
 
#  Intuition is to find the total number of good pairs, since we have equation 
#  j-i !=nums[j]-nums[i]   
#  =>  nums[i]-i!=nums[j]-j
#  nums[i]-i we will be taking count of occurrences 
#  we subtract each number of good pairs with total 
#  total_pairs=n(n-1)//2, good_pairs=value(value-1)//2 value==> each value at values in hash_map 
# 


from functools import reduce
class Solution:
          def countBadPairs(self, nums: list[int]) -> int:
                hash_map={}
                n=len(nums)
                #calculating the good pairs
                for i in range(n):
                    if (i-nums[i])  not in hash_map:
                       hash_map[(i-nums[i])]=1 
                    else: hash_map[(i-nums[i])]+=1 
                #print(hash_map.values())
                #count the number of pairs 
                total_pairs=(n*(n-1))//2 
                for value in hash_map.values():
                    total_pairs-=value*(value-1)//2
                return total_pairs 
            

class TestApp:
    def testing_case_one(self):
        assert Solution().countBadPairs([4,1,3,3])==5 
    def testing_case_two(self):
        assert Solution().countBadPairs([1,2,3,4,5])==0
    def testing_case_three(self):
        assert Solution().countBadPairs([56,30,2,73,28,81,75,75,18,63,54,10,69,85,33,89,12,78,57,60,54,65,74,63,53,77])==322
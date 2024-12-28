'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105.
-109 <= nums[i] <= 109.
0 <= k <= 105.

'''
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # take the frequency count of each element 
        # Greedy algorithm 
        # Traverse in a for loop
        # check at each element if the present element is there in h_map 
        # take the value and take the abs difference among two and check if the differences is les than and equal to k
        # return True 
        # Default not found we will return False 
        h_map={}
        for index,element in enumerate(nums):
            if element in h_map and abs(h_map[element]-index)<=k:
                return True 
            else:
                h_map[element]=index 
        
        return False 
class TestApp:
    def test_case_1(self):
        assert Solution().containsNearbyDuplicate([1,2,3,1],3)==True 
    def test_case_2(self):
        assert Solution().containsNearbyDuplicate([1,0,1,1],1)==True 
        
    def test_case_3(self):
        assert Solution().containsNearbyDuplicate([1,2,3,1,2,3],2)==False  
        
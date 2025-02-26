'''
Count all elements in the array which appears at least K times after their first occurrence
Last Updated : 30 Mar, 2023
Given an array arr[] of N integer elements and an integer K. The task is to count all distinct arr[i] such that arr[i] appears at least K times in the index range i + 1 to n – 1.

Examples: 


Input: arr[] = {1, 2, 1, 3}, K = 1 
Output: 1 
arr[0] = 1 is the only element that appears at least once in the index range [1, 3] i.e. arr[2]


Input: arr[] = {1, 2, 3, 2, 1, 3, 1, 2, 1}, K = 2 
Output: 2  
'''
class Solution:
    def countOccurrence(self,arr:list[int],k:int):
        hash_map={}
        count=0
        for i in arr:
            if i in hash_map:
                if hash_map[i]+1>=k+1:
                    hash_map[i]=0 
                    count+=1 
                else:
                    hash_map[i]+=1
            else:
                hash_map[i]=1 
        return count 

class TestApp:
        def testing_case_one(self):
            assert Solution().countOccurrence([1, 2, 1, 3],1)==1 
        def testing_case_two(self):
            assert Solution().countOccurrence([1, 2, 3, 2, 1, 3, 1, 2, 1],2)==2
        def testing_case_three(self):
            assert Solution().countOccurrence([5,2,2,12,12,1],2)==0
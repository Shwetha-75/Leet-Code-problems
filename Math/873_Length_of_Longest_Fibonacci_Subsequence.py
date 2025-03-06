class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        hash_set=set(arr)
        max_len,n=0,len(arr)
        for i in range(n):
            for j in range(i+1,n):
                prev=arr[j]
                curr=arr[i]+arr[j]
                curr_len=2 
                while curr in hash_set:
                     temp=curr 
                     curr+=prev 
                     prev=temp 
                     curr_len+=1 
                     max_len=max(max_len,curr_len)
        return max_len 

class TestApp:
        def testing_case_one(self):
            assert Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8])==5 
        def testing_case_two(self):
            assert Solution().lenLongestFibSubseq([1,3,7,11,12,14,18])==3
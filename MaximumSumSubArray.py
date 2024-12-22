# Given an nums integer arra and k is of size of a subarray, return the maximum sum among all subarrays
#  0 1 2 3 4 5 6 7
# [1,2,3,4,5,6,7,8], k=4
#  |
#    |
#      | 
#        |
#          |
#            |
#              |
#                |
# 
# n=8, k=4 i=1, i=n-k+1=>8-4+1=>4+1=5
#  

class Solution:
    def maximumSum(self,array:list[int],k:int)->int:
        cur,n=sum(array[0:k:]),len(array)
        max_sum=cur 
        for i in range(1,n-k+1):
            cur=cur+array[i+k-1]-array[i-1]
            max_sum=max(max_sum,cur)
        return max_sum 
def main():
    sol=Solution()
    result=sol.maximumSum([3,8,2,5,7,6,1,2],4)
    print(result)
main()
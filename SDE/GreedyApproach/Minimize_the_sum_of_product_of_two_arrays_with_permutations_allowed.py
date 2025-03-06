'''
Given two arrays, A and B, of equal size n, the task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[n-1] * B[n-1]. Shuffling of elements of arrays A and B is allowed.

Examples : 

Input : A[] = {3, 1, 1} and B[] = {6, 5, 4}.
Output : 23
Minimum value of S = 1*6 + 1*5 + 3*4 = 23.

Input : A[] = { 6, 1, 9, 5, 4 } and B[] = { 3, 4, 8, 2, 4 }
Output : 80.
Minimum value of S = 1*8 + 4*4 + 5*4 + 6*3 + 9*2 = 80.
The idea is to multiply minimum element of one array to maximum element of another array. Algorithm to solve this problem:  

Sort both the arrays A and B.
Traverse the array and for each element, multiply A[i] and B[n – i – 1] and add to the total.

'''

class Solution:
    def minimizeSumOfProduct(self,nums1:list[int],nums2:list[int]):
        nums1.sort()
        nums2.sort(reverse=True)
        sum_value=0 
        n=len(nums1)
        for i in range(n):
            sum_value+=nums1[i]*nums2[i]
        return sum_value 


class TestApp:
        def testing_case_one(self):
            assert Solution().minimizeSumOfProduct([3, 1, 1],[6, 5, 4])==23 
        def testing_case_two(self):
            assert Solution().minimizeSumOfProduct([6, 1, 9, 5, 4],[3, 4, 8, 2, 4])==80 
            
            
    
        
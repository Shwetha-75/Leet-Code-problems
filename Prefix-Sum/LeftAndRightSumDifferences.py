'''
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105.

'''

class Solution:
    def leftRightSumDifference(self,array:list):
        left_sum_arr,right_sum_arr=[],[]
        left_sum,right_sum=0,0
        for i in range(len(array)):
            left_sum_arr.append(left_sum)
            left_sum+=array[i]
        for i in range(len(array)-1,-1,-1):
            right_sum_arr.insert(0,right_sum)
            right_sum+=array[i]
        
        for i in range(len(left_sum_arr)):
            left_sum_arr[i]=abs(left_sum_arr[i]-right_sum_arr[i])
        print(left_sum_arr)
def main():
    sol=Solution()
    sol.leftRightSumDifference([10,4,8,3])
main()
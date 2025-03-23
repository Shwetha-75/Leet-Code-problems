'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.6M
Submissions
2.5M
Acceptance Rate
61.9%
Topics
Array
Companies
Hint 1
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_length=0 
        start,end=-1,-1
        if len(nums)==1:
            return 1 if nums[0]==1 else 0
        for i in range(len(nums)):
            if nums[i]==1:
                if start==-1:
                    start=end=i 
                elif start!=-1:
                    end=i 
            else:
                if start!=-1 and end!=-1:
                    max_length=max(max_length,(end-start)+1)
                    start=end=-1
        if start!=-1 and end!=-1:
            max_length=max(max_length,(end-start)+1)
        return max_length 
class TestApp:
      def testing_case_one(self):
          assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])==3 
      def testing_case_two(self):
          assert Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])==2
      def testing_case_three(self):
          assert Solution().findMaxConsecutiveOnes([1])==1 
      def testing_case_four(self):
          assert Solution().findMaxConsecutiveOnes([1,0])==1 
      def testing_case_five(self):
          assert Solution().findMaxConsecutiveOnes([0,0])==0
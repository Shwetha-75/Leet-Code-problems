'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''
class Solution:
        def climbingStairsToReachTop(self,n:int):
            return self.helper(n)
        def helper(self,n:int):
            if n==0 or n==1: return 1
            
            return self.helper(n-1)+self.helper(n-2)

class Solution:
    def climbingStairsToReachTop(self,n:int):
        if n<=3: return n 
        prev_3,prev_2,curr=3,2,0
        for _ in range(3,n):
            curr=prev_2+prev_3 
            prev_2=prev_3 
            prev_3=curr 
        return curr
class TestApp:
      def testing_case_one(self):
          assert Solution().climbingStairsToReachTop(1)==1
      def testing_case_two(self):
          assert Solution().climbingStairsToReachTop(2)==2 
      def testing_case_three(self):
          assert Solution().climbingStairsToReachTop(3)==3 
      def testing_case_four(self):
          assert Solution().climbingStairsToReachTop(4)==5
      def testing_case_five(self):
          assert Solution().climbingStairsToReachTop(7)==21
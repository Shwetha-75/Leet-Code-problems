'''

Problem Statement 1
John works in a coin factory where each coin has an ID. He has an array 'nums' of size N. In the factory, coins are assigned to boxes based on the sum of the digits of their IDs. For example, if the ID of a coin is 321, the sum of its digits is 6 (since 3 + 2 + 1 = 6), so the coin will be placed in box 6.

John has been given a task to work with coins that have IDs in the range from the smallest number in 'nums', called the low limit, to the largest number in 'nums', called the high limit. For each number in this range (from low-limit to high-limit, inclusive), John needs to calculate the sum of the digits and place the coin in the corresponding box.

Help John determine which box contains the most coins and output the number of coins in that box.

Note: The factory has coins with IDs ranging from 0 to infinity, but John only needs to work with coins whose IDs lie between the low limit and high limit (inclusive).

Input Format
The first line contains an integer N, representing the number of elements in nums.

The second line contains n space-separated integers representing the elements of the array nums.

Output Format
Print a single integer representing the maximum number of coins placed in any one box.

Constraints
1 <=N <=10^5

0 <= nums[i] <= 10^4.


'''

from collections import Counter
class Solution:
 def calculateCoins(self,n,nums:list):
    nums.sort()
    h_map=dict()
    lower_limit=nums[0]
    upper_limit=nums[-1]
    n=len(nums)
    for i in range(lower_limit,upper_limit+1):
         sum_digit=0 
         temp=i
         while temp!=0:
              sum_digit+=temp%10
              temp//=10 
         if sum_digit not in h_map:
             h_map[sum_digit]=1 
         else:
             h_map[sum_digit]+=1 
    print(h_map)
    return max(h_map.values())


class TestApp:
    def testing_case_one(self):
        assert Solution().calculateCoins(5,[1, 12 ,23 ,34 ,45])==5
    def testing_case_two(self):
        assert Solution().calculateCoins(2,[1000,9999])==615
    def testing_case_three(self):
        assert Solution().calculateCoins(6,[10,20,30,40,50,60])==6
    def testing_case_four(self):
        assert Solution().calculateCoins(4,[5,55,505,5505])==409

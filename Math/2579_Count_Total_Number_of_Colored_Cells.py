'''
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes. 
                                                               __
                                                            __|__|__
            __                      __                   __|__|__|__|__
           |__|                  __|__|__               |__|__|__|__|__|
            n=1                 |__|__|__|                 |__|__|__|
                                   |__|                       |__|

                                   n=2                        n=3
Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 105


'''


# As we could see that there is equation if the polugon figure 
# n=1 1 box is colored           1^2 +0^0    =1
# n=2 5 boxes are colored        2^2+1^2     =5
# n=3 13 boxes are colored       3^2+2^2     =13
# n=4 25 boxes are colored       4^2+3^2     =25
class Solution:
        def coloredCells(self, n: int) -> int:
            return n**2+(n-1)**2 


class TestApp:
        def testing_case_one(self):
           assert Solution().coloredCells(1)==1 
        def testing_case_two(self):
            assert Solution().coloredCells(2)==5 
        def testing_case_three(self):
            assert Solution().coloredCells(3)==13
        def testing_case_four(self):
            assert Solution().coloredCells(4)==25 
            
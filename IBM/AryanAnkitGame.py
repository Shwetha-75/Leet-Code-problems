'''
Problem Statement 5
Aryan and Ankit play a game with N boxes. There are an even number of boxes arranged in a row, and each box has a positive integer number of stone balls, denoted by balls(i). The objective of the game is to end with the most balls. The total number of balls across all the boxes is odd, so there are no ties.

Rules:

Aryan and Ankit take turns picking all the balls from either the beginning or the end of the row of boxes. Aryan always plays first. Both players play optimally, meaning they make decisions to maximize their number of balls.

The game ends when there are no more boxes left. Assume Aryan and Ankit play optimally. Print Aryan if Aryan wins, and print Ankit if Ankit wins.

Input Format
The first line of input contains an integer N, representing the size of the array.

The second line of input contains N space-separated integers representing the number of balls in the boxes.

Output Format
Display "Aryan" if Aryan wins or Display"Ankit" if Ankit wins.

Constraints
1<=N<=10^2

Assuming Arr denotes the array and Arr(i) denotes array element at ith index of the array.

1<=Arr(i)<=10^4
'''
class Solution:
    def boxesGame(self,boxes:list[int]):
        player_1,player_2=0,0 
        while boxes:
              if boxes:
                  player_1+=boxes.pop(0)
              if boxes:
                  player_2+=boxes.pop(-1)
        return "Aryan" if player_1>player_2 else "Ankit"
class TestApp:
      def testing_case_one(self):
          assert Solution().boxesGame([2,4,7,1,3,4])=="Aryan"
      def testing_case_two(self):
          assert Solution().boxesGame([3,9,1,2])=='Aryan'
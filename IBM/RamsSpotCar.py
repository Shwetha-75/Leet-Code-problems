'''

Problem Statement 3
Ram spots a line of N cars on the busy street, each with a unique feature. You're provided with an array called "features," where features[i] represent a distinctive feature of the ith car. Ram's quest is to discover the widest separation between two cars with different features. Can you help Ram with his quest?

Remember, this distance is determined by the absolute difference in their positions (abs(i - j)).

Input Format
The first line contains an integer N, the number of cars.

The second line contains N space-separated integers, where each integer denotes the feature of the i-th car.

Output Format
Print a single integer, which is the widest separation between any two cars that have different features.

Constraints
2 <= N <= 10^2

0 <= features[i] <= 10^3.

'''

class Solution:
    def ramsSpotCar(self,n:int,features:list)->int:
        flag=False 
        n=len(features)
        value=features[0]
        for i in features:
            if value!=i: 
                flag=True 
                break 
        if flag:
             return abs(0-(n-1))
        else: return 0 
class TestApp:
    def testing_case_one(self):
        assert Solution().ramsSpotCar(7,[10,10,10,10,10,10,20])==6 
    def testing_case_two(self):
        assert Solution().ramsSpotCar(6,[10,10,10,10,10,10])==0
    def testing_case_three(self):
        assert Solution().ramsSpotCar(5,[7,8,9,8,7])==4
        

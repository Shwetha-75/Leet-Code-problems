'''
Note: please refer the leetcode question in official page to view thw images: https://leetcode.com/problems/alternating-groups-i/description/?envType=problem-list-v2&envId=sliding-window

There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:



Alternating groups:


Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1
'''
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        # to create a circular check we are adding last element to first of the array object and 0th index element ot last 
        # traversing in linear fashion we are taking prev element at i-1 th index, current element at ith index and next at i+1th index 
        # and checking either one case is possible i.e, 010 or 101 ]
        # next==prev and cure !=next or cur!=prev 
        # increment the counter 
        # return counter 
        temp_zero,n,temp_last,count=colors[0],len(colors),colors[len(colors)-1],0
        colors.insert(0,temp_last)
        colors.append(temp_zero)
        n=len(colors)
        print(colors)
        for i in range(1,n-1):
            prev=colors[i-1]
            next=colors[i+1]
            cur=colors[i]
            if prev==next and prev!=cur :
                count+=1
        return count 
class TestApp:
    
    def testing_numberOfAlternatingGroups_1(self):
        assert Solution().numberOfAlternatingGroups([1,1,1])==0
    def testing_numberOfAlternatingGroups_2(self):
        assert Solution().numberOfAlternatingGroups([0,1,0,0,1])==3
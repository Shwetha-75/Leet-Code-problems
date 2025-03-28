'''
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days

'''
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key= lambda x:x[0])
        stack=[meetings[0]]
        for i in range(1,len(meetings)):
            if stack[-1][1]>=meetings[i][0]:
                stack[-1][1]=max(meetings[i][1],stack[-1][1])
            else:
                stack.append(meetings[i])
        count=0 
        for meeting in stack:
            count+=(meeting[1]-meeting[0])+1
        return days-count


class TestApp:
        def testing_case_one(self):
            assert Solution().countDays(57,[[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]])==1 
        def testing_case_two(self):
            assert Solution().countDays(5,[[2,4],[1,3]])==1 
        def testing_case_three(self):
            assert Solution().countDays(6,[[1,6]])==0  
    
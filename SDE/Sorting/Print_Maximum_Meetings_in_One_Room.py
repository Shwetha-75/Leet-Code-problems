'''
Given n meetings in the form of start[] and end[], where start[i] is the start time of ith meeting and end[i] is the end time of ith meeting. The task is to print the meeting number of all the meetings which can be held in a single room such that total number of meetings held is maximized. The meeting room can have only one meeting at a particular time.

Note: The start time of one chosen meeting can’t be equal to the end time of any other chosen meeting.

Examples: 

Input: start[] = {1, 3, 0, 5, 8, 5}, end[] = {2, 4, 6, 7, 9, 9} 
Output: 1 2 4 5
Explanation: We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), and the 5th meeting from (8 to 9).


Input: start[] = {10, 12, 20}, end[] = {20, 25, 30}
Output: 1
Explanation: We can attend at most one meeting in a single meeting room.

'''

class Solution:
      def printMaximumMeetings(self,start:list[int],end:list[int])->int:
            # creating the pairs of start and end time elements 
            meetings=[(start[i],end[i],i+1) for i in range(len(start))]
            
            # then we sort according to their end time 
            meetings.sort(key=lambda x:x[1])
            
            #  wkt we have to schedule more meetings in a day with less time interval 
            # s1--------------e1
            #    s2----e2 s3------e3  we consider the smallest ending time 
            # finding the meetings which is not overlapping 
            #   [s1,e1] [s2,e2]  where in s2>e1 strictly or e1<s2 
            stack=[meetings[0]]
            
            for i in range(1,len(meetings)):
                if stack[-1][1]<meetings[i][0]:
                    stack.append(meetings[i])
            print(stack)
            return [i[2] for i in stack]
            
class TestApp:
      def testing_case_one(self):
          assert Solution().printMaximumMeetings([1,3,0,5,8,5],[2,4,6,7,9,9])==[1,2,4,5]
          
      def testing_case_two(self):
          assert Solution().printMaximumMeetings([10, 12, 20],[20, 25, 30])==[1]
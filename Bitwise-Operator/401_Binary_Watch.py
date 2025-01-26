'''
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []
 

Constraints:

0 <= turnedOn <= 10.


'''

class Solution:
    def __init__(self):
        self.h_map={}
        # creating the h_map to store THE COUNT OF SET BIT 
        for i in range(60):
            self.h_map[i]=(str(bin(i))[2::]).count("1")
        
        
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result=[]
        # creating pattern for hours
        for i in range(12):
        # creating patterns for minutes 
            for j in range(60):
                if (self.h_map[i]==turnedOn + self.h_map[j])==turnedOn:
                    if j<10:
                          result.append(f"{i}:0{j}")
                    else:
                          result.append(f"{i}:{j}")
     
        return result 
class TestApp:
     
    def testing_case_one(self):
         assert Solution().readBinaryWatch(1)==["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    
    def testing_case_two(self):
        assert Solution().readBinaryWatch(9)==[]

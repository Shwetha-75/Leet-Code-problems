'''
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
'''
class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        length_seq=n*2-1
        seq=[0]*length_seq
        used=set()
        
        def helper(index:int):
            if index==length_seq: return True 
            if seq[index]: return helper(index+1)
            for i in sorted(range(1,n+1),reverse=True):
                if i in used: continue 
                next=length_seq-1-i
                if next>=length_seq or seq[next]!=0: continue 
                seq[index]=seq[next]=i
                used.add(i)
                if helper(index+1):
                    return True 
                seq[index]=seq[next]=0 
                used.remove(i)
            return False 
        
        helper(0)
        return seq 


class TestApp:
    def testing_case_one(self):
        assert Solution().constructDistancedSequence(3)==[2,3,2,1,3]or[3,1,2,3,2]
        
    def testing_case_two(self):
        assert Solution().constructDistancedSequence(5)==[5,3,1,4,3,5,2,4,2]
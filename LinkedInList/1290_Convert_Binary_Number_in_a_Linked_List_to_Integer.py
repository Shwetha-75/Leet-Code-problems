'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
523.7K
Submissions
645.2K
Acceptance Rate
81.2%
Topics
Companies
Hint 1
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
Hint 2
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
Discussion (36)

'''

class Node:
    def __init__(self,val=0):
        self.val=val 
        self.next=None 
    
class LinkedList:
    def __init__(self):
        self.node=None 
    def insert(self,val:int)->None:
        if not self.node: 
            node=Node(val)
            self.node=node 
        else:
            temp=self.node
            while temp.next:
                temp=temp.next 
            node=Node(val)
            temp.next=node 
             
class Solution:
    def getDecimalValue(self, head:Node) -> int:
        # Traversing through linked list
        result=[]
        while head:
              result.append(head.val)
              head=head.next 
        power=0 
        value=0
        # converting binary to decimal 
        while result:
             value+=result.pop(-1)*(2**power)
             power+=1 
             
        return value
        
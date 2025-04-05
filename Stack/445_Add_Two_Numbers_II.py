'''

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

class ListNode:
      def __init__(self):
          self.val=0
          self.next=None 
          
class Solution:
    def __init__(self):
        self.node=None 
    def insert(self,val:int):
        node=ListNode(val)
        if not self.node:
            self.node=node
            return 
        temp=self.node 
        while temp.next:
            temp=temp.next 
        temp.next=node 
        
              
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        list_1,list_2=[],[]
        while l1:
             list_1.append(l1.val)
             l1=l1.next 
        while l2:
             list_2.append(l2.val)
             l2=l2.next 
        if len(list_1)>len(list_2):
           extra=[0]*(len(list_1)-len(list_2))
           list_2=extra+list_2 
        else:
           extra=[0]*(len(list_2)-len(list_1))
           list_1=extra+list_1
        result=[0]*(len(list_1))
        for i in range(len(list_1)-1,-1,-1):
            sum=list_1[i]+list_2[i]
            if sum>9 and i>0:
                result[i]=sum%10
                list_1[i-1]+=sum//10 
            else:
                result[i]=sum
        if result[0]>9:
            digit_2=result[0]%10 
            digit_1=result[0]//10 
            result[0]=digit_2 
            result=[digit_1]+result 
        
        for i in result:
            self.insert(i)
        list_1.clear()
        list_2.clear()
        result.clear()
        return self.node     
    
    
        
            
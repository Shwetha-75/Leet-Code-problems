'''
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105.

'''

class Node:
    def __init__(self,val:int=0):
        self.val=val
        self.next=None 
        pass
class LinkedList:
    def __init__(self):
        self.head=None 
    def insert(self,value:int):
        if not self.head:
            node=Node(value)
            self.head=node 
            return self 
        temp=self.head 
        while temp.next:
            temp=temp.next 
        node=Node(value)
        temp.next=node 
        return self 
    def display(self,temp:Node):
        array=[]
       
        while temp:
            array.append(temp.val)
            temp=temp.next 
        return array 
# Sorting the linked list using dummy node approach : insertion Sort 

    
# class Solution:
#     def sortList(self, head: Node) -> Node:
#         dummy=Node(0)
#         prev=dummy 
#         while head:
#              next=head.next 
#              if prev.val>=head.val:
#                  prev=dummy 
#              while prev.next and prev.next.val<head.val:
#                  prev=prev.next 
#              head.next=prev.next 
#              prev.next=head 
#              head=next 
#         return dummy.next 
   
        
    
# Merge Sort : divide and conquer approach 
class Solution:
        def sortList(self, head: Node) -> Node:
             return self.divide(head) 
        
        
        def divide(self,head:Node)->Node:
            if not head or not head.next: return head 
            # finding the mid node address 
            left=head
            right=self.findMid(head)
            temp=right.next 
            right.next=None 
            right=temp 
            
            left=self.divide(left)
            right=self.divide(right)
            return self.merge(left,right)

        def findMid(self,head:Node)->Node:
            slow:Node=head
            fast:Node=head.next 
            while fast and fast.next:
                  slow=slow.next 
                  fast=fast.next.next 
            return slow 
        def merge(self,list1:Node,list2:Node)->Node: 
            tail=dummy=Node(0)
            while list1 and list2: 
                    if list1.val<list2.val:
                        tail.next=list1 
                        list1=list1.next
                    else:
                        tail.next=list2 
                        list2=list2.next 
                    tail=tail.next
            tail.next=list1 if list1 else list2 
            return dummy.next 

class TestApp:
    def testing_case_one(self):
        node=LinkedList()
        node.insert(4)
        node.insert(2)
        node.insert(3)
        node.insert(1)
        sol=Solution()
        root=sol.sortList(node.head)
        assert node.display(root)==[1,2,3,4]
    def testing_case_two(self):
        node=LinkedList()
        node.insert(-1)
        node.insert(5)
        node.insert(3)
        node.insert(4)
        node.insert(0)
        sol=Solution()
        root=sol.sortList(node.head)
        assert node.display(root)==[-1,0,3,4,5]

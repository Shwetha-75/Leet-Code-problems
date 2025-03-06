class ListNode:
    def __init__(self,val:int=0):
        self.val=val 
        self.next=None        
class LinkedList:
        def __init__(self):
           self.head=None 
        def insert(self,value:int):
            node=ListNode(value)
            if not self.head:
                self.head=node 
            else:
                temp=self.head 
                while temp.next:
                    temp=temp.next 
                temp.next=node                 
class Solution:
      def findingOutMiddleNode(self,list:ListNode)->int:
            length=0 
            temp=list 
            while temp:
                length+=1 
                temp=temp.next 
            temp=list 
            count=1 
            while count<=length//2:
                  count+=1 
                  temp=temp.next 
            return temp.val 
# Hare and Tortoise Approach 
class Solution:
        def findingOutMiddleNode(self,list:ListNode)->int:
            slow=fast=list 
            while slow and fast and fast.next:
                  slow=slow.next
                  fast=fast.next.next 
            return slow.val     
class TestApp:
        def testing_case_one(self):
            root=LinkedList()
            root.insert(1)
            root.insert(2)
            root.insert(3)
            root.insert(4)
            root.insert(5)
            assert Solution().findingOutMiddleNode(root.head)==3 
        
        
        def testing_case_two(self):
            root=LinkedList()
            root.insert(10)
            root.insert(20)
            root.insert(30)
            root.insert(40)
            root.insert(50)
            root.insert(60)
            assert Solution().findingOutMiddleNode(root.head)==40
            
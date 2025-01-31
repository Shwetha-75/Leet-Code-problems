from LinkedList import *
class Solution:
    def __init__(self):
        self.node=None 
    def insert(self,array:list[int])->None:
        if not self.node:
            node=Node(array.pop(0))
            self.node=node 
        while array:
            temp=self.node 
            while temp.next:
                temp=temp.next 
            node=Node(array.pop(0))
            temp.next=node 
        
             
        pass
    def partition(self, head:Node, x: int) -> Node:
        queue_before=[] 
        queue_after=[]
        while head:
            if head.val<x:
                 queue_before.append(head.val)
            else:
                 queue_after.append(head.val)
            head=head.next 
        self.insert(queue_before)
        self.insert(queue_after)
        return self.node
        
class Node:
    def __init__(self,val=0):
        self.val=val 
        self.next=None 
    
class List:
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
class Node:
    def __init__(self,val:int=0):
        self.val=val 
        self.left=None 
        self.right=None 
    
    
class Tree:
    def __init__(self):
        self.root=None 
    
    def insert(self,value:int):
        if not self.root:
            node=Node(value)
            self.root=node 
            return self 
        temp=self.root 
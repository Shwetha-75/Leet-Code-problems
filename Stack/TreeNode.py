class Node:
    def __init__(self,val=0):
        self.val=0
        self.left=None 
        self.right=None 
        


class BinaryTree:
    def __init__(self):
        self.root=None 
    
    
    def insert(self,value:int):
        if not self.root:
            node=Node(value)
            self.root=node 
            return self 
        temp=self.root 
        while True:
            print("Hello")
            if value<temp.val:
                if not temp.left:
                    node=Node(value)
                    temp.left=node 
                temp=temp.left 
            elif value>temp.val:
                if not temp.right:
                    node=Node(value)
                    temp.right=node 
                temp=temp.right 
            else:
                break 
        return self 
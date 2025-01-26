class _Node:
    def __init__(self,val:int):
        self.val=val
        self.left=None 
        self.right=None 



class BinaryTree:
    def __init__(self):
        self.root=None 
    def insert(self,value:int):
        # check if the root is not initialized 
        if not self.root:
            node=_Node(value)
            self.root=node 
            return self 
        temp=self.root 
        while True:
            # whether insertion is at left node 
            if value<temp.val:
                # if the left node is empty insert it 
                if temp.left==None:
                    node=_Node(value)
                    temp.left=node 
                    return self 
                # keep on traversing towards left 
                temp=temp.left 
            elif value>temp.val:
                # if the right node is empty insert it 
                if temp.right==None:
                    node=_Node(value)
                    temp.right=node 
                    return self 
                # keep on traversing towards right 
                temp=temp.right 
    
    
    def find(self,value:int):
        if not self.root:
            return False 
        temp=self.root 
        while temp:
             # if the value is less than the current node value 
             if value<temp.val:
                 temp=temp.left 
             # if the value is greater than the current node value      
             elif value>temp.right:
                 temp=temp.right 
             # if the value is equal to the current node value 
             elif temp.val==value:
                 return temp 
        return False 

                 
    def remove(self,value:int,current=None,parent=None):
        if not self.root:
            return False 
        # check if current exist
        if not current:
            current=self.root
        while current:
              # 
             if value<current.val:
                 parent=current
                 current=current.left 
             elif value>current.val:
                 parent=current 
                 current=current.right 
             else:
                #  if the the node removable as two children 
                if current.left!=None and current.right!=None:
                    # successor value 
                    current.val=self.getMin(current.right)
                    # call recursively to remove the repeated node 
                    #                  10                                                                      14     
                    #                /    \                                                                  /     \         
                    #               7      15   remove 10 and assign 14 at root place                       7       15
                    #              / \     / \                                                             /  \    /  \
                    #             3   9   14  18                                                          3    9   14  18
                    # 
                    # 
                    self.remove(current.val,current.right,current)
                #        10      if we are removing 10 
                #       /  
                #      7 
                #     / \
                #    6   8
                # 
                elif parent==None:
                     if current.left!=None:
                         current.val=current.left.val 
                         current.left=current.left.left 
                         current.right=current.left.right 
                     elif current.right!=None:
                          current.val=current.left.val 
                          current.left=current.right.left 
                          current.right=current.right.right
                     else:
                         self.root=None 
                # if the node as single child 
                elif parent.left==current:
                     parent.left=current.left if current.left else current.right 
                elif parent.right==current:
                     parent.right=current.left if current.left else current.right 
                # break the loop if none of the cases are true 
                break
        return self   
    
    def getMin(self,node:_Node):
        
        while node.left:
            node=node.left 
        return node.val 

    def inOrder(self,node:_Node):
        if not node:
            return 
        print(node.val,end=' ')
        self.inOrder(node.left)
        self.inOrder(node.right)



root=BinaryTree()
root.insert(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(8)
root.insert(14)
root.insert(18)
root.inOrder(root.root)
root.remove(5)
print()
root.inOrder(root.root)

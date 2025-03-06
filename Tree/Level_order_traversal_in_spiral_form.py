class Tree:
      def __init__(self,val:int=0):
          self.val=val 
          self.left=None 
          self.right=None 


class BinaryTreeInsertion:
        def __init__(self):
            self.root=None 
        def insert(self,value):
            node=Tree(value)
            if not self.root:
               self.root=node 
               return self 
            temp:Tree=self.root
            while temp:
                    if value<temp.val:
                    #  go check on inserting it into left subtree 
                        if temp.left==None:
                           temp.left=node
                           return self
                        temp=temp.left
                    else:
                        if temp.right==None:
                            temp.right=node 
                            return self 
                        temp=temp.right 
                        
        
class Solution:
      def levelOrderTraversalSpiralForm(self,root:Tree):
            level=0 
            queue=[root]
            result=[]
            while queue:
                size=len(queue)
                if level%2==0:
                    temp=[]
                    for i in range(size):
                        node=queue.pop(0)
                        temp.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                    result+=temp[::-1]
                else:
                    for i in range(size):
                        node=queue.pop(0)
                        result.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                print(result,level)
                level+=1
            print(result)
            return result 


class TestApp:
      def testing_case_one(self):
          root=BinaryTreeInsertion()
          root.insert(5)
          root.insert(2)
          root.insert(7)
          root.insert(1)
        
          root.insert(6)
          root.insert(8)
          
          assert Solution().levelOrderTraversalSpiralForm(root.root)==[5,2,7,8,6,1]
            
                    
                 
          
class Tree:
    def __init__(self,val:int):
        self.val=val 
        self.left=None 
        self.right=None  
    def countingNodes(self,node):
        count=1
        if not node: return 0 
        else:
            count+=self.countingNodes(node.left)
            count+=self.countingNodes(node.right)
        return count 
  
class Solution:
   
    def binaryTreeIntoArray(self,root:Tree):
        result=[]
        queue=[(root,0)]
        while queue:
             node,index=queue.pop(0)
             if index>=len(result):
                 result.extend([None]*(index-len(result)+1))
             result[index]=node.val if node else None 
             if node:
                 queue.append((node.left,2*index+1))
                 queue.append((node.right,2*index+2))
        while result and not result[-1]:
            result.pop()
        return result 
    def checkComplete(self,array:list):
        return not None in array 


class TestApp:
      
    def testing_case_one(self):
          root=Tree(10)
          root.left=Tree(7)
          root.right=Tree(15)
          root.left.left=Tree(6)
          root.left.right=Tree(9)
          root.right.left=Tree(11)
          assert Solution().binaryTreeIntoArray(root)==[10,7,15,6,9,11]
    def testing_case_two(self):    
          root=Tree(10)
          root.left=Tree(7)
          root.right=Tree(15)
          root.left.left=Tree(6)
          root.left.right=Tree(9)
          root.right.right=Tree(17)
          assert Solution().binaryTreeIntoArray(root)==[10,7,15,6,9,None,17]
    def testing_case_complete(self):
          root=Tree(10)
          root.left=Tree(7)
          root.right=Tree(15)
          root.left.left=Tree(6)
          root.left.right=Tree(9)
          root.right.right=Tree(17)
          assert Solution().checkComplete(Solution().binaryTreeIntoArray(root))==False 
    def testing_case_complete_two(self):
          root=Tree(10)
          root.left=Tree(7)
          root.right=Tree(15)
          root.left.left=Tree(6)
          root.left.right=Tree(9)
          root.right.left=Tree(11)
          assert Solution().checkComplete(Solution().binaryTreeIntoArray(root))==True 
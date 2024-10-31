from collections import deque
class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def isCousin(self,root:TreeNode,x:int,y:int):
        def helper(root:TreeNode,x:int,y:int):
            queue=deque([(root,None)])
            while queue:
                  length=len(queue)
                  ans=[]
                  current_node,parent=queue.popleft()
                  for _ in range(length):
                      if current_node.val==x:
                          if parent: ans.append(parent.val)
                          
                      if current_node.val==y:
                          if parent: ans.append(parent.val)
                      
                      if current_node.left: 
                          queue.append([current_node.left,current_node])
                      if current_node.right:
                          queue.append([current_node.right,current_node])
                  if len(set(ans))==2:
                      return True 
            return False 
        return helper(root,x,y)
def main():
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(4)
    sol=Solution()
    result=sol.isCousin(root,2,3)
    print(result)
main()
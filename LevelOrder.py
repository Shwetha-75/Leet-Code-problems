class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def levelOrder(self,root:TreeNode):
        outer=[]
        level=[]
        if not root: return []
        level.append(root)
        while True:
             next_level=[]
             value=[]
             
             for i in level:
                 value.append(i.val)
             outer.append(value)
             
             for i in level:
                 if i.left: next_level.append(i.left)
                 if i.right: next_level.append(i.right)
             level=next_level
             if not next_level: break 
        return outer 
def main():
    sol=Solution()
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(7)
    result=sol.levelOrder(root)
    print(result)
main()
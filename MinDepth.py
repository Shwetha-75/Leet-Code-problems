import math
class TreeNode:
      def __init__(self,val:int):
          self.val=val
          self.left=None
          self.right=None
class Solution:
    def minDepth(self,root:TreeNode):
        if not root:
            return 0
        lh=self.minDepth(root.left)
        rh=self.minDepth(root.right)
        if lh==0 or rh==0: 
            1+max(lh,rh)
        return 1+min(lh,rh)
def main():
    sol=Solution()
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.right=TreeNode(3)
    root.left.left=TreeNode(10)
    root.left.right=TreeNode(11)
    res=sol.minDepth(root)
    print(res)
main()   
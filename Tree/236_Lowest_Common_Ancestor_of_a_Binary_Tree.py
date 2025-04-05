class TreeNode:
    def __init__(self,val:int=0):
        self.val=val 
        self.left=None 
        self.right=None 


class Solution:
          def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
                
                if root.val==p.val or root.val==q.val:
                    return root 
                if not root.left and root.right: return None 
                
                if root.left:
                   left=self.lowestCommonAncestor(root.left,p,q)
                if root.right:
                    right=self.lowestCommonAncestor(root.right,p,q)
                if left and right:
                    return root 
                return left if left else right
class TestApp:
      def testing_case_one(self):
          root=TreeNode(3)
          root.left=TreeNode(5)
          root.right=TreeNode(1)
          root.left.left=TreeNode(6)
          root.left.right=TreeNode(2)
          root.left.right.left=TreeNode(7)
          root.left.right.right=TreeNode(4)
          root.right.left=TreeNode(0)
          root.right.right=TreeNode(8)
          node:TreeNode=Solution().lowestCommonAncestor(root,TreeNode(5),TreeNode(1))
          assert node.val==3
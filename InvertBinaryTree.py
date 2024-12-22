class TreeNode:
       def __init__(self,val):
           self.val=val
           self.left=None 
           self.right=None 
class Solution:
      def invertBinaryTree(self,root:TreeNode):
          def helper(root:TreeNode):
              if not root: return 
              treeLeft=helper(root.left)
              
          
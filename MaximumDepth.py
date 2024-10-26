'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 

path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''

class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def maxDepth(self,root:TreeNode):
        def helper(root:TreeNode,height:int):
            if not root: return 0
            return max(helper(root.left,height),helper(root.right,height))+1
        return helper(root,0)
def main():
    sol=Solution()
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(7)
    result=sol.maxDepth(root)
    print(result)
main()
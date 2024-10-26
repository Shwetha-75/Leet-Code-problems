class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None 
class Solution:
    def flipEquivalentBinaryTrees(self,root1:TreeNode,root2:TreeNode):
        def checker(node1,node2):
            if not node1 and not node2:
                return True 
            if not node1 or not node2 or node1.val!=node2.val:
                return False 
            return ((checker(node1.left,node2.left) or checker(node1.left,node2.right)) and (checker(node1.right,node2.right) or checker(node1.right,node2.left)))
        
        return checker(root1,root2)
def main():
    root1=TreeNode(1)
    root1.left=TreeNode(2)
    root1.right=TreeNode(3)
    root1.left.left=TreeNode(4)
    root1.left.right=TreeNode(5)
    root1.left.right.left=TreeNode(7)
    root1.left.right.right=TreeNode(8)
    root1.right.right=TreeNode(6)
    
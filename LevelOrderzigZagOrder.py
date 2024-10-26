'''

Given the root of a binary tree, return the zigzag level order 
traversal of its nodes' values. (i.e., from left to right, 
then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100.

'''
class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def levelOrderZigZag(self,root:TreeNode):
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
        for i in range(len(outer)):
            if i%2!=0:
                temp=outer[i]
                outer[i]=temp[::-1]
            
        return outer 
def main():
    sol=Solution()
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(7)
    result=sol.levelOrderZigZag(root)
    print(result)
main()
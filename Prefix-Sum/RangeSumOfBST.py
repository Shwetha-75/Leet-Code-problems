'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.


'''

from collections import deque
class TreeNode:
      def __init__(self,val:int):
          self.val=val
          self.left=None 
          self.right=None 
class Solution:
      def __init__(self):
          self.sum_range=0
      def rangeSumBST(self,root:TreeNode,low:int,high:int):
        sum_range=0
        #   queue=deque()
        #   queue.append(root)
        #   while queue:
        #         temp=queue.popleft()
        #         if temp.val>=low and temp.val<=high:
        #             print(temp.val)
        #             sum_range+=temp.val
        #         if temp.left: queue.append(temp.left)
        #         if temp.right: queue.append(temp.right)
        #   return sum_range 
        def inOrderTraversal(root,low,high):
            if not root: 
                return 
            self.sum_range+=root.val if root.val>=low and root.val<=high else 0 
            inOrderTraversal(root.left,low,high)
            inOrderTraversal(root.right,low,high)
        inOrderTraversal(root,low,high)
        return self.sum_range
          
def main():
    sol=Solution()
    root=TreeNode(10)
    root.left=TreeNode(5)
    root.right=TreeNode(15)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(7)
    
    root.right.right=TreeNode(18)
    result=sol.rangeSumBST(root,7,15)
    print(result)
main()



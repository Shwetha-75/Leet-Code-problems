'''
Given the root of a binary tree, imagine yourself standing on 
the right side of it, return the values of the nodes you can 
see ordered from top to bottom.

 

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Explanation:



Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Explanation:


Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100.


'''

from TreeNode import *
class Solution:
      def __init__(self):
          self.stack=[]
          
    #   def inOrder(self,root:Node):
    #       if not root: return   
    #       self.inOrder(root.left)
    #       self.stack.append(root.val)
    #       self.inOrder(root.right)
      def rightSideView(self, root:Node) -> list[int]:
            queue=[root]
          
            # self.inOrder(root)
            
            result=[]
            while queue:
                    size=len(queue)
                    for i in range(size):
                        curr=queue.pop(0)
                        if i==size-1:
                           result.append(curr.val)
                        if curr.left:
                            queue.append(curr.left)
                        if curr.right:
                            queue.append(curr.right)
        
            return result 


class TestApp:
       def testing_case_one(self):
                root=Node(1)
                root.left=Node(2)
                root.right=Node(3)
                root.left.right=Node(5)
                root.right.right=Node(4)
                assert Solution().rightSideView(root)==[1,3,4]
          
        
        
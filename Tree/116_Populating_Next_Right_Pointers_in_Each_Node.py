'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

'''

from Stack.TreeNode import Node 



# Using the simple pointer approach 
#                          
#                          1                          cur-->     1
#                       /     \                                /   \
#                      2 -----> 3                   nextle--> 2     3
#                     / \      / \                           / \   / \
#                    4-> 5 -> 6--> 7                        4   5 6   7
#                                             
#                          
# 


class Solution:
    def connect(self, root:Node):
        current=root 
        nextLevel=current.left 
        while current and nextLevel:
            current.left.next=current.right 
            while current.next:
                  current.right.next=current.next.left 
                  current=current.next 
                  current.right.next=current.left 
            current=nextLevel 
            nextLevel=current.left
        return root 



# Intuition Using Queue 
# Initialize queue with root node
# Until the queue exists: 
#      take the size of present queue 
#      Iterate until the last range: 
#              current---> first element form the queue 
#              if it is last index :
#                 point the current node next field to null
#              else: current.next--->queue[0]
#              add the current node children 
#     
# 


class Solution:
    def connect(self, root:Node):
        queue=[] 
        queue.append(root)
        while queue:
            size=len(queue)
            for i in range(size):
                current=queue.pop(0)
                if i==size-1:
                   current.next=None 
                else:
                    current.next=queue[0]
                
                if current.left: 
                    queue.append(current.left)
                if current.right: 
                    queue.append(current.right)
          
class TestApp:
      def testing_case_one(self):
          pass
'''
Note Link: https://1drv.ms/o/c/e72d2f024dc534f0/EgGPhLf4PpdFr8VBkLukVCABjCj9cauvIIrz_nhnd98NwA?e=hEyd6A
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

from Stack.TreeNode import *



# Using nextLevel node with  O(n) and O(1)
class Solution:
    
    def __init__(self):
        self.hash_map={}
    def connect(self, root:Node):
        # Intition is wrong 
        # storing all the elements in array 
        # Traversing through array and checking its parent 
        # if the parent.right==current : then current.next-->null 
        # else current.left--> current.right 
        # level order traversal 
        current=root 
        nextLevel=current.left 
        while current and nextLevel:
            current.left.next=current.right 
            while current.next:
                  current.right.next=current.next.left 
                  current=current.next 
                  current.left.next=current.right 
            current=nextLevel 
            nextLevel=current.left 
        return root 
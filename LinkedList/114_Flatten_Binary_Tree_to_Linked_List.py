'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

'''

from TreeNode import * 

# Approach 1 : Using Recursion Time Complexity O(n) Space Complexity O(n)
        # pseudo code 
        # prev--->null
        # func: root 
        #     if root not exist return; 
        #     recursively call right subtree 
        #     recursively call left subtree 
        #     swapping : 
        #     root.right--->prev 
        #     root.left--->null 
        #     prev--->root 
class Solution:
    def __init__(self):
        self.prev=None 
          
    def flatten(self, root:Node) -> None:
        
        # Wrong Approach 
        # self.preOrder(root)
        # root=None 
        # for value in self.array:
        #     if not root:
        #         node=Node(value)
        #         root=node 
        #     else:
        #         temp=root 
        #         node=Node=(value)
        #         while temp.right:
        #              temp=temp.right
        #         temp.right=node 
        #         temp.left=None 
        
        self.helper(root)

    def helper(self,root:Node):
            if not root: return 
            self.helper(root.right)
            self.helper(root.left)
            root.right=self.prev 
            root.left=None 
            self.prev=root  
            
# Approach 2 : Stack  Time Complexity: O(n) Space Complexity: O(n) 

# Initialize the stack with root 
# Iterate until stack exists: 
#        current--->top stack & pop it 
#        if their children exist push to stack
#        if the stack is not empty: assign current right to hold top of the stack  
#        assign current left to hold None 


class Solution:
    def flatten(self, root:Node) -> None:
        stack=[]
        stack.append(root)
        while stack:
              current=stack.pop(0)
              if current.left:
                  stack.append(current.left)
              if current.right:
                  stack.append(current.right)
              if stack:
                  current.right=stack[-1]
              current.left=None 
        
# Approach 3 : Using two pointers 
class Solution:
    def flatten(self, root:Node) -> None:
        current=root 
        while current:
              if current.left:
                  prev=current.left 
                  while prev.right:
                       prev=prev.right
                  prev.right=current.right 
                  current.right=current.left 
                  current.left=None 
              current=current.right 
        
   
array=[]
def preOrderTraversal(root:Node):
    if not root:
        array.append("null")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    

# Testing 
class TestApp:
    def testing_case_one(self):
        pass
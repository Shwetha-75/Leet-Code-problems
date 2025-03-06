'''
Given the root of a binary tree. Check whether it is a Binary Search Tree or not. A Binary Search Tree (BST) is a node-based binary tree data structure with the following properties. 

All keys in the left subtree are smaller than the root and all keys in the right subtree are greater.
Both the left and right subtrees must also be binary search trees.
Each key must be distinct.

'''

class Tree:
      def __init__(self,val:int=0):
          self.val=val 
          self.left=None 
          self.right=None 
class BinaryTree:
        def __init__(self):
            self.root=None 
        def insert(self,value:int=0):
            node=Tree(value)
            if not self.root:
                self.root=node 
                return self 
            current=self.root 
            while current:
                if value<current.val:
                    if not current.left:
                        current.left=node 
                        return self 
                    current=current.left 
                else:
                    if not current.right:
                        current.right=node 
                        return self 
                    current=current.right 
               
    
class Solution: 
        def __init__(self):
            self.stack=[]
        def checkIfTheTreeIsBST(self,root:Tree):
          self.inOrder(root)
          return len(self.stack)==1 
        
        
        def inOrder(self,root:Tree):
            if not root: return 
            self.inOrder(root.left)
            if self.stack and self.stack[-1]<=root.val:
                self.stack.pop()
            self.stack.append(root.val)
            self.inOrder(root.right)
            
class TestApp:
      def testing_case_one(self):
          root=BinaryTree()
          root.insert(5)
          root.insert(1)
          root.insert(8)
          root.insert(7)
          root.insert(9)
          assert Solution().checkIfTheTreeIsBST(root.root)==True 
          
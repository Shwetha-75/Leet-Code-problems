from TreeNode import * 

class Solution:
      def __init__(self):
          self.stack=[]
      def increasingBST(self, root:Node):
            def inOrder(rootNode:Node):
                if not rootNode: return 
                inOrder(rootNode.left)
                self.stack.append(rootNode)
                inOrder(rootNode.right)
            inOrder(root)
            arr=self.stack[::-1]
            dummy=Node(0)
            curr=self.stack.pop(0)
            dummy.right=curr
            
            while self.stack:
                  node=self.stack.pop(0)
                  node.left=None 
                  curr.right=node 
                  curr=node 
            curr.right=None 
            return dummy.right
                  

class TestApp:
      def testing_case_one(self):
          root=BinaryTree()
          root.insert(5)
          root.insert(3)
          root.insert(6)
          root.insert(2)
          root.insert(4)
          root.insert(1)
          root.insert(8)
          root.insert(7)
          root.insert(9)
          assert Solution().increasingBST(root.root)==[1,2,3,4,5,6,7,8,9]
          
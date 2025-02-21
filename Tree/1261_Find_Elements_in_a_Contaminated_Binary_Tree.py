'''
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]

      -1                  0
        \                  \  
         -1                  2
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 



Example 2:

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]

          -1                             0 
        /     \                        /   \ 
       -1     -1                     1      2
      /  \                         /   \ 
    -1   -1                       3     4
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False


Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]



Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106

'''

class Tree:
      def __init__(self):
          self.val=0 
          self.left=None 
          self.right=None 
class FindElements:
        def __init__(self, root:Tree):
           self.root=root
           if root:
               root.val=0
               queue=[root]
               self.array=[]
               while queue:
                    node=queue.pop(0)
                    self.array.append(node.val)
                    if node.left:
                         node.left.val=2*node.val+1 
                         queue.append(node.left)
                    if node.right:
                        node.right.val=2*node.val+2 
                        queue.append(node.right) 
            
        def find(self, target: int) -> bool:
            return target in self.array
        
class Elements:
    
        def __init__(self,root):
            self.root=root 
            #   contaiminated 
            root.val=0 
            queue=[root]
            while queue:
                   node=queue.pop(0)
                   if node.left:
                       node.left.val=2*node.val+1 
                   if node.right:
                       node.right.val=2*node.val+2
        def traversal(self,root,target):
              if not root:
                  return False 
              if root.val==target:
                  return True 
              return self.traversal(root.left,target) or self.traversal(root.right,target)
        def find(self,target:int)->bool:
            return self.traversal(self.root,target)
    
class FindElements:
    
        def __init__(self,root):
            self.root=root 
            self.map={}
            root.val=0 
            
            # BFS
            queue=[root] 
            while queue:
                  node=queue.pop(0)
                  self.map[node.val]=1 
                  
                  if node.left:
                      node.left.val=2*node.val+1 
                      queue.append(node.left)
                  if node.right:
                      node.right.val=2*node.val+2 
                      queue.append(node.right)
            
        def find(self,target:int)->bool:
                return target in self.map   
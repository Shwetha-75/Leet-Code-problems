'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109    

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Traversal:
      def __init__(self):
          self.array=[]
      def inOrderTraversal(self,root:TreeNode):
          if not root:
              return 
          self.inOrderTraversal(root.left)
          self.array.append(root.val)
          self.inOrderTraversal(root.right)
          
          
          
# This approach was totally wrong 

# 
#                          <- 1
#                         /     \
#                      <-2      <-5
#                      /  \     /  \ 
#                    <-3  <-4  <-6  <-7
# 
#                   "1-2--3--4-5--6--7"
#            
#              the initial approach I have considered like this 
#               By calculating their depths 
#               array= [[0,1],[1,2],[2,3],[2,4],[1,5],[2,6],[2,7]]
# 
# 
#                -> Incorrect splitting the binary tree 
#                -> As I encounter the 1 in between the array I splitting the binary the tree to assign it to the right side for the root node
# 
#                   
#                -> incorrect in calculating the parent index where in we can see
#                               in below example 

# 
#                           "1-401--349--90---88"
# 
#                                    <- 1
#                                     /   
#                                 <- 401
#                                  /    \
#                              <-349   <-90
#                                         \
#                                        <- 88
#                            0      1      2       3      4
#                         [[0,1],[1,401],[2,349],[2,90],[3,88]]
#                        for this above array if we try to construct a tree                
#            ❌                  <-  1
#                                 /  
#                        <-     401
#                             /    \    
#                        <-  349 <- 90        
#                           /
#                       <-  88
# 
#                          

class Solution:
    def recoverFromPreorder(self, traversal: str):
        # constructing the left subtree array 
        left_subtree,right_subtree=[],[]
        count=0
        replaced_string=[i for i in traversal.split("-") if i!='']
        # Pseudo code 
        # if the present character is not equal to '-' and next character is equal to '-'
        index=-1
        prev=count
        left_subtree.append([0,traversal[0]])
        for i in range(len(traversal)-1):
            if traversal[i]!='-' and traversal[i+1]=='-':
                
                if count==1 and prev!=0:
                    index=i 
                    break
                left_subtree.append([count,replaced_string.pop(0)])
                prev=count
                count=0
            elif traversal[i]!='-' and traversal[i+1]!='-':
                continue 
            else:
                count+=1             
        if count!=0:
            left_subtree.append([count,replaced_string.pop(0)])
        
        
        if index!=-1:
            left_subtree.pop(0)
            right_subtree.append(left_subtree.pop(-1))
            
            count=0
           
            for i in range(index+1,len(traversal)-1):
                if traversal[i]!='-' and traversal[i+1]=='-': 
                   right_subtree.append([count,replaced_string.pop(0)])
                   count=0
                elif traversal[i]!='-' and traversal[i+1]!='-':
                    continue 
                else:
                    count+=1
            if count!=0:
               right_subtree.append([count,replaced_string.pop(0)])
        else:
            left_subtree.pop(0)
        if left_subtree:
            node=TreeNode(left_subtree[0][1])
            left_subtree[0][1]=node 
            for i in range(1,len(left_subtree)):
                index,value=left_subtree[i]
                node=TreeNode(value)
                print(f"i-------->{i}",left_subtree)
                if not left_subtree[index-1][1].left:
                    left_subtree[index-1][1].left=node 
                else:
                    left_subtree[index-1][1].right=node
                left_subtree[i][1]=node 
        print(left_subtree)
        if right_subtree:
            node=TreeNode(right_subtree[0][1])
            left_subtree[0][1].right=node
            right_subtree[0][1]=node 
            for i in range(1,len(right_subtree)):
                index,value=right_subtree[i]
                node=TreeNode(value)
                print(f"i-----{i}",right_subtree)
                if not right_subtree[index-2][1].left:
                    right_subtree[index-2][1].left=node 
                else:
                    right_subtree[index-2][1].right=node 
                right_subtree[i][1]=node 
        return left_subtree[0][0]
   
   
   
# ✅ 
# Use stack 
#                          - 1
#                         /     \
#                      - 2    -  5
#                      /  \     /  \ 
#                  -  3   -4  -6  - 7
# 
#           " 1-2--3--4-5--6--7 "
#            
# 

class Solution:
    def recoverFromPreorder(self, traversal: str):
        stack:list[TreeNode]=[]
        index:int=0 
        while index<len(traversal):
              #
                depth=0 
                while index<len(traversal) and traversal[index]=='-':
                        depth+=1 
                        index+=1 
                # we have to consider the numeric value 
                value=0 
                while index<len(traversal) and traversal[index].isdigit():
                        value=10*value+int(traversal[index]) 
                        index+=1 
                node=TreeNode(value)
                # we gonna assign it as first node in the level 
                # or to the right side 
                if depth==len(stack):
                    if stack:
                        stack[-1].left=node 
                else:
                    while len(stack)>depth:
                        stack.pop()
                    stack[-1].right=node 
                stack.append(node)
        return stack[0]


class TestApp:
    
    
    def testing_case_one(self):
        result=Traversal()
        result.inOrderTraversal(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))
        
        assert result.array==[3,2,4,1,6,5,7]
    def testing_case_two(self):
        result=Traversal()
        result.inOrderTraversal(Solution().recoverFromPreorder("1-401--349--90---88"))==[349,401,90,88,1]
        
    def testing_case_three(self):
        result=Traversal()
        result.inOrderTraversal(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))==[4,3,2,1,7,6,5]
    
    def testing_case_four(self):
        result=Traversal()
        result.inOrderTraversal(Solution().recoverFromPreorder("1-401--349---90--88"))==[90,349,401,88,1]
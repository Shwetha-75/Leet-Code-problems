class TreeNode:
      def __init__(self,val:int=0):
          self.val=val
          self.left=None 
          self.right=None 
          
          
class Solution:
        def __init__(self):
            self.array=[]
        def preorder(self,root:TreeNode):
            if not root:
                return 
            self.array.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
            
        def constructFromPrePost(self, preorder: list[int], postorder: list[int]) :
            return self.constructBinaryTree(preorder,postorder,[0],0,len(postorder)-1)

        def constructBinaryTree(self,preorder:list,postorder:list,pre_index:list,length:int,height:int):
            if pre_index[0]>=len(preorder) or length>height:
                return None 
          
            root=TreeNode(preorder[pre_index[0]])
            pre_index[0]+=1
           
           
            if length==height:
                return root 
            
            
            i=0 
            for i in range(length,height+1):
                print("hello",i)
                if preorder[pre_index[0]]==postorder[i]:
                    break 
            
            if i<=height:
                # call left tree 
                root.left=self.constructBinaryTree(preorder,postorder,pre_index,length,i)
                root.right=self.constructBinaryTree(preorder,postorder,pre_index,i+1,height-1)
                
            return root 
        


class TestApp:
    
    
    def testing_case_one(self):
        solution=Solution()
        root=solution.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])
        solution.preorder(root)
        print(solution.array)
        assert solution.array==[1,2,4,5,3,6,7]
        
    def testing_case_two(self):
        solution=Solution()
        root=solution.constructFromPrePost([1],[1])
        solution.preorder(root)
        assert solution.array==[1]
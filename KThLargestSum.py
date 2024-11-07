    class TreeNode:
        def __init__(self,val:int):
            self.val=val
            self.left=None
            self.right=None
    class Solution:
        def KThLargestSum(self,root:TreeNode):
            outer_level=[]
            level=[]
            if not root: None
            level.append(root)
            
            while True:
                next_level=[]
                value=[]
                for i in level:
                    value.append(i.val)
                outer_level.append(value)
                for i in level:
                    if i.left:
                        next_level.append(i.left)
                    if i.right:
                        next_level.append(i.right)
                level=next_level
                if not next_level:
                    break
            for i in range(len(outer_level)):
                outer_level[i]=sum(outer_level[i])
            outer_level.sort(reverse=True)
            print(outer_level)
            return outer_level[1] if len(outer_level)>1 else outer_level[0]
    def main():
        sol=Solution()
        root=TreeNode(5)
        root.left=TreeNode(8)
        root.right=TreeNode(9)
        root.left.left=TreeNode(2) 
        root.left.right=TreeNode(1)
        root.right.left=TreeNode(3)
        root.right.right=TreeNode(7)
        root.left.left.left=TreeNode(4)
        root.left.left.right=TreeNode(6)
        res=sol.KThLargestSum(root)
        print(res)
    main()
from TreeNode import *
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
        temp=root 
        def helper(root,level=0):
            if level not in    
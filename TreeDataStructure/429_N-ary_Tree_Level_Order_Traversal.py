from NaryTree import *

class Solution:
    def __init__(self):
        self.hash_map={}
    def traversal(self,root:Node,level:int):
        if level not in self.hash_map:
            self.hash_map[level]=[root.val]
        else:
            self.hash_map[level].append(root.val)
        for node in root.children:
            self.traversal(node,level+1)
        
    def levelOrder(self, root:Node) -> list[list[int]]:
        self.traversal(root,0)
        return self.hash_map.values()
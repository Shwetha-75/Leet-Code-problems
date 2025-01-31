from NaryTree import * 
class Solution:
    def __init__(self):
        self.array=[]
        
    def traversal(self,root:Node,level:int):
        self.array.append(root.val)
        for node in root.children:
            self.traversal(node,level+1)
    def preorder(self, root:Node) -> list[int]:
        self.traversal(root,0)
        return self.array
    
    
class TestApp:
    def testing_case_one(self):
        node=Node(1)
        child1=Node(3)
        child2=Node(2)
        child3=Node(4)
        node.add_child(child1)
        node.add_child(child2)
        node.add_child(child3)
        subChild1=Node(5)
        subChild2=Node(6)
        child1.add_child(subChild1)
        child1.add_child(subChild2)
        
        assert Solution().preorder(node)==[1,3,5,6,2,4]
    
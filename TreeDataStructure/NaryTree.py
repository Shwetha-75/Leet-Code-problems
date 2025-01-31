class Node:
    def __init__(self,val:int=0):
        self.val=val
        self.children=[] 

    # insertion    
    def add_child(self,children):
        self.children.append(children)

    # Level order Traversal (BFS)
    
def traversal(root:Node,level:int):
        print("",level,"",root.val)
        for node in root.children:
            traversal(node,level+1)



node=Node(10)
child1=Node(12)
child2=Node(30)
sub_child1=Node(16)
sub_child2=Node(15)

node.add_child(child1)
node.add_child(child2)

child2.add_child(sub_child1)
child2.add_child(sub_child2)
    


traversal(node,0)

    
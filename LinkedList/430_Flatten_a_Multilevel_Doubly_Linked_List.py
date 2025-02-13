'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

 

Example 1:


Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:


Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:

Input: head = []
Output: []
Explanation: There could be empty list in the input.
 

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
 

How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
'''
class Node:
    def __init__(self,val:int=0):
        self.val=val 
        self.prev=None 
        self.next=None 
        self.child=None 


class DoublyLinkedList:
    def __init__(self):
        self.head=None 
    def insert(self,val:int=0):
        if not self.head:
            node=Node(val)
            self.head=node 
            return self 
        temp=self.head 
        while temp.next:
            temp=temp.next 
        node=Node(val)
        temp.next=node 
        node.prev=temp 
        return self 
    def connectChild(self,node_1:Node,node_2:Node):
        node_1.child=node_2 
    
    def display(self,node:Node):
        array=[]
        while node:
              array.append(node.val)
              node=node.next 
        return array
class Solution:
    def __init__(self):
        self.temp=None 
    def flatten(self, head:Node):
        self.temp=head 
        def helper(root:Node):
            if not root or root.next==None :
                return root 
            while root.next:
                if root.child:
                    next=root.next 
                    childNode=helper(root.child)
                    childNode.next=next 
                    next.prev=childNode
                    root.next=root.child 
                    root.child.prev=root 
                    root.child=None 
                root.child=None 
                root=root.next
            return root 
        helper(head)
        dd=DoublyLinkedList()
        return dd.display(self.temp)
        


class Solution:
    def __init__(self):
        self.temp=None 
    def flatten(self, head:Node):
        
        self.temp=head 
        def helper(root:Node):
            curr=root 
            last=None 
            
            while curr:
                  next_ptr=curr.next 
                  if curr.child:
                      tail_ptr=helper(curr.child)
                      tail_ptr.next=next_ptr 
                      if next_ptr:
                          next_ptr.prev=tail_ptr 
                      curr.next=curr.child
                      curr.child.prev=curr
                      curr.child=None 
                      last=tail_ptr 
                  else:
                      last=curr 
                  
                  curr=curr.next 
            return last                           
        helper(head)
        return DoublyLinkedList().display(self.temp)

class TestApp:
    
    def testing_case_one(self):
        doubleLinkedList=DoublyLinkedList()
        doubleLinkedList.insert(1)
        doubleLinkedList.insert(2)
        doubleLinkedList.insert(3)
        doubleLinkedList.insert(4)
        doubleLinkedList.insert(5)
        doubleLinkedList.insert(6)
        temp=doubleLinkedList.head
        while temp.next:
              if temp.val==3: break 
              temp=temp.next 
        dd_2=DoublyLinkedList()
        dd_2.insert(7)
        dd_2.insert(8)
        dd_2.insert(9)
        dd_2.insert(10)
        temp.child=dd_2.head
        temp=dd_2.head
        while temp.next:
              if temp.val==8: break 
              temp=temp.next 
        dd_3=DoublyLinkedList()
        dd_3.insert(11)
        dd_3.insert(12)
        temp.child=dd_3.head

        assert Solution().flatten(doubleLinkedList.head)==[1,2,3,7,8,11,12,9,10,4,5,6]
        
        # 1->2->3->4->5->6->x
        #       |                       ==>1->2->3->7->8->11->12->9->10->4->-5>-6->x
        #       7->8->9->10->x
        #             |
        #             11->12->x
        #             
        
        
        


    def testing_case_two(self):
        dd_1=DoublyLinkedList()
        dd_1.insert(1) 
        dd_2=DoublyLinkedList()
        dd_2.insert(2)
        dd_1.head.child=dd_2.head 
        dd_3=DoublyLinkedList()
        dd_3.insert(3)
        dd_2.head.child=dd_3.head 
        assert Solution().flatten(dd_1.head)==[1,2,3]
        
        #   1->x
        #   | 
        #   2->x           ==> 1->2->3->x
        #   |
        #   3->x
        #   |
        #   x
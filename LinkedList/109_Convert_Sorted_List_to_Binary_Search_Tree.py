'''

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
'''

from Stack.TreeNode import Node 
from LinkedListNode import Root as ListNode 
class Solution:
    def __init__(self):
        self.root=None 
    # insertion of binary tree 
    def insert(self,value:int):
        # check if the root exist or not 
        if not self.root:
            node=Node(value)
            self.root=node 
            return self 
        # create temp variable
        temp=self.root 
        node=Node(value)
        # traverse until value is been inserted
        while True:
            # checking if the node as to be inserted at left binary tree or right
            # insertion at left binary tree
            if value<temp.val:
                if not temp.left:
                    temp.left=node 
                temp=temp.left
            # insertion at right binary tree 
            elif value>temp.val:
                if not temp.right:
                    temp.right=node  
                temp=temp.right 
            else: break 
    
    
    #  taking the id element at each recursive call and sub array   
    def insertionFrommArray(self,array:list):
        if not array: return 
        # taking mid index to insert the value 
        mid=len(array)//2 
        self.insert(array[mid])    
        # left subtree
        self.insertionFrommArray(array[:mid])
        self.insertionFrommArray(array[mid+1::])
        return self 
    def sortedListToBST(self, head:ListNode):
        array=[]
        # creating list 
        while head:
            array.append(head.val)
            head=head.next 
        self.insertionFrommArray(array,0,len(array)-1)
        return self.root 
    
    

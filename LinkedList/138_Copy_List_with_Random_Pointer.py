class Node:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 
          self.random=None
          
#  Approach : Creating the copy of the LL
#  Pseudo Code: 
#  Making the copy of each list node into array 
#  Traversing through each array element using for loop 
#             performing insert operation on each value 
#  Making the copy of present LL into array (another)
#  Assign the random pointer to newly created linked list 
#  Since the array contains the list of nodes and we have to find the element by their random address in the array 
#  Assigning the random of present temp pointer to the index matching node 




class Solution:
    def __init__(self):
        self.array:list[Node]=[]
        self.head_copied=None 
        self.array_copy:list[Node]=[]
    def insert(self,val):
        if not self.head_copied:
               node=Node(val)
               self.head_copied=node 
               return self 
        temp=self.head_copied 
        while temp.next:
              temp=temp.next 
        node=Node(val)
        temp.next=node 
        return self 
    def copyRandomList(self, head:Node):
        while head:
              self.array.append(head)
              head=head.next 
        # inserting all the linked list elements 
        for i in self.array:
              self.insert(i.val)
        # assigning the random pointer 
        temp=self.head_copied
        
        while temp:
              self.array_copy.append(temp)
              temp=temp.next 
        temp=self.head_copied
        
        n=len(self.array)
        for i in range(n):
            if self.array[i].random:
                index=self.array.index(self.array[i].random)
                temp.random=self.array_copy[index]
            temp=temp.next 
        return self.head_copied  
    
    
# Approach : Using Hash Map 

class Solution:
    
    def copyRandomList(self, head:Node):
        hash_map={None:None}
        temp=head 
        while temp:
              node=Node(temp.val)
              hash_map[temp]=node 
              temp=temp.next 
        # assigning the random pointer 
        current_head=Node(0)
        temp=head 
        while temp:
              copy=hash_map[temp]
              copy.next=hash_map[temp.next]
              copy.random=hash_map[temp.random]
              current_head.next=copy 
              temp=temp.next 
        return current_head.next 
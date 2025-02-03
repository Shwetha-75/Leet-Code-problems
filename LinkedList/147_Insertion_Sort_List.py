'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000.



'''

class Node:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 
        
        
# Approach by creating array  
class Solution:
    def insertionSortList(self, head:Node)->Node:
        array:list[Node]=[]
        temp=head
        while temp:
              array.append(temp)
              array[-1].next=None
              temp=temp.next 
        # Insertion sort 
        n=len(array)
        for i in range(1,n):
            temp=array[i].val
            j=i-1 
            while j>=0 and temp<array[j].val:
                  array[j+1]=array[j]
                  j-=1 
            array[j+1].val=temp
        for i in range(n-1):
            array[i].next=array[i+1]
        return array[0]


# Optimized code than before 
class Solution:
    def insertionSortList(self, head:Node)->Node:
        array:list[int]=[]
        temp=head 
        while temp:
            array.append(temp.val)
        # insertion sort 
        n=len(array)
        for i in range(1,n):
            j=i-1 
            temp=array[i]
            while j>=0 and temp<array[j]:
                array[j+1]=array[j]
                j-=1 
            array[j+1]=temp 
        
        current=head 
        while current:
            current.val=array.pop(0)
            current=current.next 
        return head 
    
# Using Dummy ptr Approach 
class Solution:
    def insertionSortList(self, head:Node)->Node:
        dummy=Node(0)
        prev:Node=dummy 
        while head:
            # holding the head at next 
            next:Node=head.next 
            # 
            while prev.next and prev.next.val<head.val:
                  prev=prev.next 
            head.next=prev.next 
            prev.next=head 
            head=next  
        return dummy.next 
    
            
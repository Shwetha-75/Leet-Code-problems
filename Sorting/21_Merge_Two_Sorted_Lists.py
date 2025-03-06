class ListNode:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) ->ListNode:
        
        left,right=list1,list2 
        dummy=ListNode(0)
        head=dummy 
        while left and right:
                if left.val<right.val:
                   head.next=left 
                   left=left.next 
                else:
                    head.next=right 
                    right=right.next 
                head=head.next 
        while left:
              head.next=left 
              left=left.next
              head=head.next 
        while right:
              head.next=right 
              right=right.next
              head=head.next
        return dummy.next 
    
'''
Add two numbers
Given two linked list l1=1->2->3,   l2=1->2
reverse the numbers 321+21=342
return the newly created linked list = 2->4->3
'''






class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def addAtTail(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
            self.tail=self.head 
        else:
            self.tail.next=node 
            self.tail=node 
        self.size+=1
        return self.head
   
   
def reverse(list1):
    #observations
    if list1==None: return 0
    num1=0
    while list1:
        num1=num1*10+list1.value
        list1=list1.next
    #observations
    if num1==0:
        return 0
    result=0
    while num1!=0:
        result=result*10+num1%10 
        num1=num1//10 
    return result

def addNumber(list1,list2):#                      returns
    #reverse function returns the number 1->2->3  -----> 321
    
    result=reverse(list1)+reverse(list2)
    #observations
    
    root=None
    ll=LinkedList()
    
    if result==0: 
        return ll.addAtTail(result)
    #insertion at tail
    while result !=0:
        root=ll.addAtTail(result%10)
        result=result//10
    return root


def main():
    node=Node(0)
    node.next=Node(0)
    node.next.next=Node(0)
    node1=Node(0)
    node1.next=Node(0)
    
    root=addNumber(node,node1)
    while root:
        print(root.value,end="")
        root=root.next
main()
  
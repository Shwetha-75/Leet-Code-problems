class Node:
      def __init__(self,value:int):
          self.value=value
          self.next=None 

class Stack:
      def __init__(self):
          self.stack=None 
          self.length=0
      def push(self,value):
          node=Node(value)
          if not self.stack:
               self.stack=node 
               self.length+=1
               return self
          temp=self.stack 
          while temp.next:
                temp=temp.next 
                
          temp.next=node 
          self.length+=1 
          
          return self 
      def pop(self):
          if not self.stack:
              return None 
          
        #   if you have only one element 
          if not self.stack.next:
              self.length-=1 
              self.stack=None 
              return 
          prev=None 
          curr=self.stack
          while curr.next:
                prev=curr 
                curr=curr.next 
          value=curr.value 
          prev.next=None 
          self.length-=1 
          return value 
      def size(self):
          return self.length 
      def __str__(self):
          if not self.stack:
              print("[]")
              return 
          print("[",end='')
          temp=self.stack
          while temp.next:
              print(temp.value,end=', ')
              temp=temp.next 
          print(temp.value,end=']')
          print()

class Activity:
      def methodActivity(self):
          stack=Stack()
          stack.push(10)
          stack.push(1)
          stack.push(20)
          stack.push(30)
          stack.push(40)
          stack.push(50)
          stack.push(60)
          stack.__str__()
          stack.pop()
          stack.pop()
          stack.pop()
          stack.pop()
          stack.pop()
          stack.pop()
          stack.pop()
          print(stack.size())
          stack.__str__()

Activity().methodActivity()
               
      
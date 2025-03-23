class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val:int):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop(-1)
    def last(self):
        return self.stack[-1] if self.stack else None 
    def size(self):
        return len(self.stack)


class Activity:
      def methodActivity(self):
          stack=Stack()
          stack.push(10)
          stack.push(12)
          stack.push(13)
          stack.push(14)
          stack.push(15)
          stack.push(10)
          print(stack.stack)
          stack.pop()
          print(stack.stack)
          print(stack.size())
Activity().methodActivity()
from collections import deque
class Stack:
        def __init__(self):
            self.q1=deque()
            self.q2=deque()
        def push(self,number):
            self.q2.append(number)
            while self.q1:
                  self.q2.append(self.q1.popleft())
            self.q1,self.q2=self.q2,self.q1 
        def pop(self):
            if self.q1:
                return self.q1.popleft()
            return None 
        def top(self):
            if self.q1:
                return self.q1[0]
            return None 


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())

    
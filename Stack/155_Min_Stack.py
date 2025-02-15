import heapq
class MinStack:

    def __init__(self):
        self.stack=[]  

    def push(self, val: int) -> None:
        heapq.heappush(self.stack,val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[0]


# Keeping Track of the minimum value for each push element

class Solution:
      
    def __init__(self):
        self.stack=[] 
    
    
    def push(self,val:int):
        temp_min=self.getMin()
        if temp_min is not None or temp_min>val:
            temp_min=val 
        self.stack.append([val,temp_min]) 
    
    def top(self):
        return self.stack[-1][0]
    
    def pop(self):
        self.stack.pop()
    
    def getMin(self)->int:
        return self.stack[-1][1] if self.stack else None 
        
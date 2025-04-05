class MyCircularQueue:
        def __init__(self,k:int):
            self.array=[]
            self.size=k 
           
        def enQueue(self,value:int)->bool:
            if self.size==len(self.array):
               return False 
            else:
                self.array.append(value)
            return True 
        def deQueue(self)->bool:
            if len(self.array)==0:
                return False 
            else:
                self.array.pop(0)
            return True 
        def Front(self)->int:
            if len(self.array)==0:
                return -1 
            else:
                return self.array[0]
        def Rear(self)->int:
            if len(self.array)==0:
                return -1 
            else:
                return self.array[-1]
        def isEmpty(self)->bool:
            return len(self.array)==0 
        def isFull(self)->int:
            return len(self.array)==self.size 
        


          
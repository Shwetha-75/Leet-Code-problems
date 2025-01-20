class MinHeap:
    def __init__(self):
        self.array=[]
    
    def heapify_up(self,index):
         parent=(index-1)//2 
         if index>0 and self.array[index]<self.array[parent]:
             self.array[index],self.array[parent]=self.array[parent],self.array[index]
             self.heapify_up(parent)
           
        
    def insert(self,value):
        self.array.append(value)
        self.heapify_up(len(self.array)-1)
    
    
    def display(self):
        for i in self.array:
            print(i,end=' ')


minHeap=MinHeap()
minHeap.insert(5)
minHeap.insert(6)
minHeap.insert(7)
minHeap.insert(8)
minHeap.insert(4)
minHeap.insert(3)
minHeap.insert(2)
minHeap.insert(-1)
minHeap.display()
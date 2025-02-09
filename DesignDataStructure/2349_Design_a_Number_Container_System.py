class NumberContainers:

    def __init__(self):
        self.array=[]

    def change(self, index: int, number: int) -> None:
        if index>=len(self.array):
            self.array=self.array+[0]*(index-(len(self.array)-1))
        self.array[index]=number 
        
        pass
    def find(self, number: int) -> int:
        return self.array.index(number) if number in self.array else -1 
    
    
# Using priority queue 
import heapq
class NumberContainers:

    def __init__(self):
        self.array=[]

    def change(self, index: int, number: int) -> None:
        if not self.array:
            self.array.append([index,number])
        else:
            # find the index 
            flag=False 
            for i in self.array:
                if i[0]==index :
                    flag=True
                    self.array[i][1]=number 
                    break 
            if not flag:
                self.array.append([index,number])
        self.array.sort(key=lambda x: x[0])
        
       
        
    def find(self, number: int) -> int:
        for i in self.array:
            if i[1]==number:
                return i[0]
        return -1
    
    
from collections import OrderedDict
import heapq
hash_map=OrderedDict()

hash_map[0]=1
hash_map[-1]=10 



from queue import PriorityQueue 

class Solution:
      def __init__(self):
          self.array=PriorityQueue()
      def change(self, index: int, number: int) -> None:
          if not self.array:
                 self.array.put([index,number])
          else:
              pass 
    
    
# Using hash_map
class Solution:
        def __init__(self):
            self.hash_map={}
            self.color={}
        def insert(self,index:int,number:int)->None:
            # insertion 
            if index not in self.hash_map:
                # painting intially 
                self.hash_map[index]=number
                if number in self.color:
                  self.color[number].append(index)
                else:
                    self.color[number]=[index]
                heapq.heapify(self.color[number])
            else:
                # repainting 
                self.color[self.hash_map[index]].remove(index)
                if len(self.color[self.hash_map[index]])==0:
                    del self.color[self.hash_map[index]]
                    # repainting 
                hash_map[index]=number 
                
                if number in self.color:
                   self.color[number].append(index)
                
                else:
                    self.color[number]=[index]
                    
                heapq.heapify(self.color[number])
        def find(self,number:int):
            if number in self.color:
                return min(self.color[number])
            else:
                return -1 
            
            
# Using : Approach Using two hash_map 
class Solution:
        
        def __init__(self):
             self.hash_map={}
             self.color={}
        # repainting the value or 
        def change(self,index:int,number:int)->None:
            if number not in self.color:
                self.color[number]=[] 
            heapq.heappush(self.color[number],index)
            self.hash_map[index]=number 
        
        # finding the the value 
        def find(self,number:int):
            if number not in self.color:
                return -1 
            heap=self.color[number]
            while heap:
                  index=heapq.heappop(self.color[number])
                  if self.hash_map[index]==number:
                      heapq.heappush(self.color[number],index)
                      return index 
            return -1 
        
        





class MyHashSet:
    def __init__(self):
        self.hashSet=[]
         
    def add(self,key:int)->None:
        if key not in self.hashSet:
            self.hashSet.append(key) 
    
    def remove(self,key:int)->None:
        if key in self.hashSet:
            self.hashSet.remove(key) 
    
    def contains(self,key:int)->bool:
        return True if key in self.hashSet else False 
# using set 

class HashSet:
    def __init__(self):
        self.hashSet=set()
    def add(self,key:int)->None:
        if key not in self.hashSet:
            self.hashSet.add(key)
    def remove(self,key:int)->None:
        if key in self.hashSet:
            self.hashSet.remove(key)
    def contains(self,key:int)->bool:    
        return True if key in self.hashSet else False 
    
    
class TestApp:
    def testing_case_one(self):
        query=["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        query_set=[[], [1], [2], [1], [3], [2], [2], [2], [2]]
        result=[]
        n=len(query)
        object=None 
        for i in range(n):
            if query[i]=="MyHashSet":
                object=MyHashSet()
                result.append("null")
            elif query[i]=="add":
                object.add(query_set[i])
                result.append("null")
            elif query[i]=="remove":
                object.remove(query_set[i])
                result.append("null")
            elif query[i]=="contains":
                result.append(object.contains(query_set[i]))
        print(result)
        assert result==["null", "null", "null", True, False, "null", True, "null", False]
      
      
    
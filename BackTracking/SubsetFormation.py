class Solution:
    
    def formTheSubSet(self,s:str):
         
     
        return self.helper(s)
        pass 
    
    def helper(self,s:str,index=0,current=None,result=None):
        if current==None: current=[]
        if result==None: result=[] 
        
        
        if index==len(s):
            result.append(current[:])
            return 
        
        for i in range(index,len(s)):
            part=s[index:i+1:]
            current.append(part)
            self.helper(s,i+1,current,result)
            current.pop()
        return result 


class TestApp:
    
    
    def testing_case_one(self):
        assert Solution().helper("1296")==[["1","2","9","6"],["1","2","96"],["1","29","6"],["1","296"],["12","9","6"],['12',"96"],["129","6"],["1296"]]
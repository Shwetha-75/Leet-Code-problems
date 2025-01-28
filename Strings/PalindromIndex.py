class Solution:
    def palindromeIndexMethod1(s:str):
        n=len(s)
        def checkPalindrome(input:str):
            return input==input[::-1]
        # Exceeding the time limit 
        for i in range(n):
            if i==0:
                if not checkPalindrome(s[i+1::]):
                     return i 
                elif not checkPalindrome(s[:i:]):
                    return i 
                else:
                    if not(checkPalindrome(s[:i:]+s[i+1::])):
                        return i 
        return -1 
    def palindromeIndexMethod2(s:str):
        
        pointer_1,pointer_2=0,len(s)-1 
        
        while pointer_1<=len(s)-1 and pointer_2>=0:
              if s[pointer_1]!=s[pointer_2]:
                  break 
              pointer_1+=1 
              pointer_2+=1 
        
        if pointer_1>=len(s):
           return -1 
        # excluding the pointer 1
        if pointer_1==0: 
            if s[pointer_1+1::]==s[pointer_1+1::-1]:
                return pointer_1 
        if s[:pointer_1:]==s[pointer_1+1::-1]:
            return pointer_1 
        
        # excluding the pointer 2 
        
        if pointer_2==len(s)-1:
            if s[:pointer_2:]==s[:pointer_2:-1]:
                return pointer_2 
        return -1 
    
    def palindromeIndexMethod3(self,s:str):
        def helper(input:str):
            return input==input[::-1]
        
        left,right=0,len(s)-1 
        while left<right:
              if s[left]!=s[right]:
                #   exclude the character at left 
                if helper(s.replace(s[left],"")):
                    
                   return right 
                elif helper(s[::-1].replace(s[right],"")):
                   return left
                else: return -1 
              left+=1 
              right-=1 
        return -1  
                      

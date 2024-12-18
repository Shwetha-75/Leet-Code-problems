# Brute Force Approach 

# from collections import Counter
# class Solution:
#     def __init__(self):
#         self.stack=''
#     def helper(self,list_string:list):
#             n=len(list_string)
#             for i in range(n):
#                 if self.stack[-1]!=list_string[i]:
#                    print(self.stack[-1],list_string[i])
#                    self.stack+=list_string[i]
#                    print("I'm printing :",self.stack,list_string[i])
#                    list_string.remove(self.stack[-1])
#                    return True 
#             return False 
#     def repeatLimitedString(self,s:str,repeatLimit:int)-> str:
#       if repeatLimit==1:
#             hash_map=list(dict(Counter(s)).items())
#             def helper(list_item:list):
#                 if list_item[0][1]==0 or list_item[0][1]==0:
#                     return 
#                 self.stack+=list_item[0][0]+list_item[1][0]
#                 list_item[0][1]-=1
#                 list_item[1][1]-=1
#                 helper(list_item)
            
#             while hash_map:
#                   list=[]
#                   if len(hash_map)>=2:
#                       list.append(hash_map.pop(0))
#                       list.append(hash_map.pop(0))
#                       helper(list)
                  
#             return self.stack+hash_map[0][0] if hash_map else ''
#       else:      
#         list_string=list(s)
#         list_string.sort(reverse=True)
       
#         count=0
        
#         while list_string:
#               if count>=repeatLimit:
                 
#                   if self.helper(list_string):
#                       count=1
                      
#                   else:
#                       return self.stack 
#               elif self.stack and self.stack[-1]!=list_string[0]:
#                    count=1
#                    self.stack+=list_string.pop(0)
                 
#               else:
#                   self.stack+=list_string.pop(0)
#                   count+=1 
              
#         return self.stack 
# def main():
#     sol=Solution()
#     result=sol.repeatLimitedString("cczazcc",1)
#     print(result)
# main()

class Solution:
     def repeatLimitedString(self,s:str,repeatLimit:int):
         current_index=25
         freq=[0]*26 
         for i in s:
             freq[ord(i)-ord('a')]+=1
         print(freq)
         stack=''
         while current_index>=0:
              
               if freq[current_index]>0:
                  stack+=chr(current_index+ord("a"))*min(freq[current_index],repeatLimit)
                  freq[current_index]-=repeatLimit 
                #   if still the characters are there but we have break the subsequence 
                  
                  if freq[current_index]>0:
                    if current_index-1>=0:
                      small_index=current_index-1 
                      while small_index>=0:
                            if freq[small_index]>0:
                                break 
                            small_index-=1 
                      if small_index==-1: break 
                      stack+=chr(small_index+ord('a'))
                      freq[small_index]-=1 
                    else:
                      break 
               else:
                   current_index-=1 
         return stack 

def main():
    sol=Solution()
    result=sol.repeatLimitedString("aababab",2)
    print(result)
main()
                    
                      

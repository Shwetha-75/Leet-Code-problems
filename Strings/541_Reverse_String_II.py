class Solution:
    
     def reverseStr(self, s: str, k: int) -> str:
         if len(s)<=k: return s[::-1]
         list_string=list(s)
         for i in range(0,len(s),2*k):
             j=min(i+k-1,len(s)-1)
             while i<j:
                   list_string[i],list_string[j]=list_string[j],list_string[i]
                   j-=1
                   i+=1 
         return "".join(list_string)    

class TestApp:
      def testing_case_one(self):
          assert Solution().reverseStr("abcdefg",2)=="bacdfeg"
      def testing_case_two(self):
          assert Solution().reverseStr("abcd",2)=="bacd"   
      def testing_case_three(self):
          assert Solution().reverseStr("abc",4)=="cba"          
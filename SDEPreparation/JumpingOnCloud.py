class Solution:
      def jumpingOnClouds(self,c:list[int])->int:
          result=[]
          for i in range(len(c)):
              if c[i]==0:
                  result.append(i)
        
          
          for i in range(1,len(result)-1):
              if result[i]-result[i-1]==result[i+1]-result[i]==1:
                  result[i]=-1 
          count=0 
        
          for i in result:
              if i!=-1:
                  count+=1 
          return count-1
class TestApp:
     def testing_case_one(self):
         assert Solution().jumpingOnClouds([0 ,0 ,1 ,0, 0 ,1,0])==4
     def testing_case_two(self):
         assert Solution().jumpingOnClouds([0,0,0,0,1,0])==3
     def testing_case_three(self):
         assert Solution().jumpingOnClouds([0,1,0,0,0,1,0])==3
     def testing_case_four(self):
         assert Solution().jumpingOnClouds([0,0,0,0,0])==2
     def testing_case_five(self):
         assert Solution().jumpingOnClouds([0,1,0,1,0,1,0])==3
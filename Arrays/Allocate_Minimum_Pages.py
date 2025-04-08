class Solution:
      def numberOfStudents(self,arr:list[int],value:int):
          count_student,pages=1,0 
          for i in range(len(arr)):
              if pages+arr[i]>value:
                  count_student+=1 
                  pages=arr[i]
              else:
                  pages+=arr[i]
          return count_student
      def findPages(self, arr:list[int], k:int):
          if len(arr)<k: return -1  
          maximum,total=max(arr),sum(arr)
          for i in range(maximum,total+1):
              if self.numberOfStudents(arr,i)<=k:
                  return i 
          return -1 
# Using Binary Search     
class Solution:
      def numberOfStudents(self,arr:list[int],value:int):
          count_student,pages=1,0 
          for i in range(len(arr)):
              if pages+arr[i]>value:
                  count_student+=1 
                  pages=arr[i]
              else:
                  pages+=arr[i]
          return count_student
      def findPages(self, arr:list[int], k:int):
          if len(arr)<k: return -1   
          left,right,result=max(arr),sum(arr),-1
          while left<=right:
                mid=(left+right)//2 
                if self.numberOfStudents(arr,mid)<=k:
                    result=mid
                    right=mid-1
                else:
                    left=mid+1 
          return result

       

class TestApp:
    def testing_case_one(self):
        assert Solution().findPages([12,34,67,90],2)==113 
    def testing_case_two(self):
        assert Solution().findPages([15,17,90],5)==-1 
    def testing_case_three(self):
        assert Solution().findPages([22,23,67],1)==112
    def testing_case_four(self):
        assert Solution().findPages([15 ,10 ,19 ,10 ,5 ,18,7],5)==25
          
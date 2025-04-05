class Solution:
      def merge(self, nums1: list[int], nums2: list[int],m: int=0, n: int=0) -> None:
            result=[0]*(len(nums1)+len(nums2))
            index_1,index_2,index=0,0,0
            while index_1<len(nums1) and index_2<len(nums2):
                
                  if nums1[index_1] <nums2[index_2]:
                     result[index]=nums1[index_1]
                     index_1+=1
                  else:
                      result[index]=nums2[index_2]
                      index_2+=1 
                  index+=1 
            while index_1<len(nums1):
                  result[index]=nums1[index_1]
                  index_1+=1
                  index+=1  
            while index_2<len(nums2):
                  result[index]=nums2[index_2]
                  index_2+=1
                  index+=1  
            return result 


class Solution:
      def merge(self, nums1: list[int], nums2: list[int],m: int=0, n: int=0) -> None:
            if n==0: return  nums1 
            if m==0: return nums2
            index_1,index_2=0,0
            while index_1<m:
                  if nums1[index_1] > nums2[index_2]:
                     temp=nums1[index_1]
                     nums1[index_1]=nums2[index_2]
                     nums2[index_2]=temp
                     index_2+=1 
                 
                  index_1+=1 
            index_2=0
            while index_1<len(nums1):
                  nums1[index_1]=nums2[index_2]
                  index_2+=1 
                  index_1+=1 
            return nums1
# reverse order 
class Solution:
      def merge(self, nums1: list[int], nums2: list[int],m: int=0, n: int=0) -> None:
            index_1,index_2,index_3=m-1,n-1,len(nums1)-1 
            while index_1>=0 and index_2>=0:
                  print(nums1)
                  if nums1[index_1]>nums2[index_2]:
                     
                     nums1[index_3]=nums1[index_1]
                     index_1-=1 
                  else:
                      nums1[index_3]=nums2[index_2]
                      index_2-=1 
                  index_3-=1 
                 
            while index_2>=0:
                  nums1[index_3]=nums2[index_2]
                  index_2-=1 
                  index_3-=1 
            return nums1
        
class TestApp:
      def testing_case_one(self):
          assert Solution().merge([1,2,3,0,0,0],[2,5,6],3,3)==[1,2,2,3,5,6]
      def testing_case_two(self):
          assert Solution().merge([0],[1],0,1)==[1]
      def testing_case_three(self):
          assert Solution().merge([4,5,6,0,0,0],[1,2,3],3,3)==[1,2,3,4,5,6]
          
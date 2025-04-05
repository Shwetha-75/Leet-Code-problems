class Solution:
        def findKeyInRotatedSortedArray(self,array:list[int],target):
          #   finding the pivot index 
            pivot=0 
            for i in range(len(array)-1):
                if array[i]>array[i+1]:
                    pivot=i 
                    break 
          
            #    left array 
            def helper(left,right,target):
              
                while left<=right:
                      mid=(left+right)//2 
                      if array[mid]==target:
                         return mid 
                      elif array[mid]>target:
                           right=mid-1 
                      else:
                          left=mid+1 
                return -1 
           
            temp=helper(0,pivot,target)
            if temp!=-1:
                return temp
            temp=helper(pivot+1,len(array)-1,target)
            if temp!=-1:
                return temp 
            return -1 


class TestApp:
       def testing_case_one(self):
           assert Solution().findKeyInRotatedSortedArray([3,4,5,1,2],2)==4    
       def testing_case_two(self):
           assert Solution().findKeyInRotatedSortedArray([1,2,3,4,5],5)==4
       def testing_case_three(self):
           assert Solution().findKeyInRotatedSortedArray([2,3,4,5,1],2)==0
       def testing_case_four(self):
           assert Solution().findKeyInRotatedSortedArray([5,1,2,3,4],1)==1
       def testing_case_five(self):
           assert Solution().findKeyInRotatedSortedArray([2,3,4,5,6,7,1],7)==5
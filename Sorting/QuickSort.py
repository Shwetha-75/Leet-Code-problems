class Solution:
    def quickSortMethod(self,array:list):
        # function: find the pivot index 
        def findPivotIndex(array:list,low:int,high:int):
            pivot=array[high]
            i=low-1 
            for j in range(low,high):
                  if array[j]<=pivot:
                      i+=1
                      array[i],array[j]=array[j],array[i]
            array[i+1],array[high]=array[high],array[i+1]
            return i+1 
             
        def divideArray(array:list,low=0,high=None):
            if high is None:
                high=len(array)-1 
            if low<high:
                pivot_index=findPivotIndex(array,low,high)
                #  divide the array 
                divideArray(array,low,pivot_index-1)
                divideArray(array,pivot_index+1,high)
                
            
        
        divideArray(array) 
        return array


class TestApp:
    def testing_case_one(self):
        assert Solution().quickSortMethod([4,1,2,3])==[1,2,3,4]
    def testing_case_two(self):
        assert Solution().quickSortMethod([5,4,3,2,1,-1,10,19])==[-1,1,2,3,4,5,10,19]
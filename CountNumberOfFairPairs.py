class Solution:
      def countNumberOfFairPairs(self,array:list,lower:int,upper:int):
        #   time limit Exceeded
        #   count=0
        #   array.sort()
          
        #   for i in range(len(array)):
        #       if array[i]>lower: continue 
        #       for j in range(i+1,len(array)):
        #           if lower<=(array[i]+array[j]) and (array[j]+array[i]<=upper):
        #               count+=1 
        #   return count 
        def binarySearch(array:list,target:int):
            left,right,result=0,len(array)-1,0
            while left<right:
                  sum=array[left]+array[right]
                  
                  if sum<target:
                     result+=right-left 
                     left+=1
                  else:
                      right-=1 
            return result 
        return binarySearch(array,upper+1)-binarySearch(array,lower)
def main():
    sol=Solution()
    result=sol.countNumberOfFairPairs([1,7,9,2,5],11,11)
    print(result)
main()
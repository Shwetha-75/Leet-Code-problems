# Brute Force Approach 

class Solution:
      def findTwiceAndMissingElement(self,array:list[int])->list[int]:
        #   sort the array 
        array.sort()
        frequency=1 
        missingElement=-1
        twice=-1
        for i in range(len(array)-1) :
            if frequency not in array:
                missingElement=frequency 
            if array[i]==array[i+1]:
                twice=array[i]
            frequency+=1 
        if missingElement==-1:
            missingElement=frequency
        return [missingElement,twice]


from collections import Counter
# By counter 
class Solution:
        def findTwiceAndMissingElement(self,array:list[int])->list[int]:
            hash_map=dict(Counter(array))
            item=[key for key,value in hash_map.items() if value==2]
            frequency=1 
            n=len(array)
            while frequency<=n:
                    if frequency not in hash_map:
                       return [frequency,item[0]]
                    frequency+=1 
            
# optimized approach 
class Solution:
        def findTwiceAndMissingElement(self,array:list[int])->list[int]:
            result=[-1]*(len(array))
            twice=0
            for i in array:
                if result[i-1]==-1:
                    result[i-1]=i 
                else:
                    twice=i 
            for i in range(len(array)):
                if result[i]==-1:
                    return [i+1,twice]

class TestApp:
        def testing_case_one(self):
            assert Solution().findTwiceAndMissingElement([3,1,3])==[2,3]
        def testing_case_two(self):
            assert Solution().findTwiceAndMissingElement([1,2,1])==[3,1]
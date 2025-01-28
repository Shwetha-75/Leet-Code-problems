class Solution:
    def findOriginalArray(self,array:list[int],n)->list[int]:
        def calculateXOROfNNaturalElements(n:int):
            if n&3==0:
                return n
            elif n&3==1:
                return 1 
            elif n&3==2: 
                return n+1 
            else:
                return 0 
        originalArray=[] 
       
        xor_all=calculateXOROfNNaturalElements(n)
        xor_adjacent=0 
        for i in range(0,n-1,2):
            xor_adjacent=xor_adjacent^array[i]
        last_element=xor_all^xor_adjacent
        
        originalArray.append(last_element)
        
        for i in range(n-2,-1,-1):
            last_element=last_element^array[i]
            originalArray.insert(0,last_element)
        return originalArray 


class TestApp:
    
    def testing_case_one(self):
        assert Solution().findOriginalArray([7, 5, 3, 7],5)==[3 ,4 ,1 ,2, 5 ]
    
    
    def testing_case_two(self):
        assert Solution().findOriginalArray([3,1],3)==[1,2,3]
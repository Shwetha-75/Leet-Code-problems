import sys
from sympy import *
class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        result=[] 
        for i in range(left,right+1):
            if isprime(i):
               result.append(i)
        if len(result)>=2:
            res=[]
            closest_gap=sys.maxsize
            for i in range(len(result)-1):
               gap=result[i+1]-result[i]
               if gap<closest_gap:
                  res=[result[i],result[i+1]]
                  closest_gap=gap 
            return res    
            
            
        else:
            return [-1,-1]

    # def checkPrime(self,number:int)->bool:
    #     if number==1 or number==2: return True 
    #     for i in range(2,number):
    #         if number%i==0:
    #             return True 
    #     return False +
    
class Solution:
      def closestPrimes(self, left: int, right: int) -> list[int]:
        #   marking all the prime number 
        prime_numbers=[1]*(right+1)
        # traverse through to find out the prime number 
        for i in range(2,right+1):
            if prime_numbers[i]==1:
               for j in range(i*2,right+1,i):
                   prime_numbers[j]=0 
        result=[]
        if left==1:
            left+=1
        for i in range(left,len(prime_numbers)):
            if prime_numbers[i]==1:
                result.append(i)
        if len(result)>=2:
            res=[]
            closest_gap=sys.maxsize
            for i in range(len(result)-1):
               gap=result[i+1]-result[i]
               if gap<closest_gap:
                  res=[result[i],result[i+1]]
                  closest_gap=gap 
            return res    
            
            
        else:
            return [-1,-1]
        
class Solution:
      def closestPrimes(self, left: int, right: int) -> list[int]:
            prime=[1]*(right+1)
            for i in range(2,right+1):
              if prime[i]==1:
                 for j in range(i**2, right+1,i):
                     prime[j]=0 
            result=[]
            if left==1:
                left+=1 
            for i in range(left,right+1):
                if prime[i]==1:
                    result.append(i)
            if len(result)>=2:
                res=[]
                closest_gap=sys.maxsize
                for i in range(len(result)-1):
                  gap=result[i+1]-result[i]
                  if gap<closest_gap:
                     res=[result[i],result[i+1]]
                     closest_gap=gap 
                return res    
            
            
            else:
                 return [-1,-1]
                   
        

class TestApp:
        def testing_case_one(self):
            assert Solution().closestPrimes(10,19)==[11,13]
        def testing_case_two(self):
            assert Solution().closestPrimes(4,6)==[-1,-1]

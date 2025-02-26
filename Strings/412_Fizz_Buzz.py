class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        array=[0]*n
        
        for i in range(n):
            # if it is divisible by 3 and 5 
            if (i+1)%5 ==0 and (i+1)%3==0:
                array[i]="FizzBuzz"
            elif (i+1)%3==0:
                array[i]="Fizz"
            elif (i+1)%5==0:
                array[i]="Buzz"
            else:
                array[i]=str(i+1) 
        return array 
        
class TestApp:
    
        def testing_case_one(self):
            assert Solution().fizzBuzz(3)==["1","2","Fizz"]
        def testing_case_two(self):
            assert Solution().fizzBuzz(5)==["1","2","Fizz","4","Buzz"]
        def testing_case_three(self):
            assert Solution().fizzBuzz(15)==["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
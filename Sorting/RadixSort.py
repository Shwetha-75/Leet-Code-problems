# Algorithm :
# Step 1: Take the maximum element from the array and calculate the number of digits and store it digits 
# Step 2: Use for loop to traverse through each digit and perform counting sort 
# Step 3: call counting sort function to sort the array at digit wise 
# Step 4: Counting Sort: args--> array, digit position  

# Counting sort: parameters ---> array, digit position 
# Step 1: Initialize the array to store the digit at each given digit position 
# Step 2: take maximum element and initialize the cumulative sum array 
# Step 3: Initialize the array of n array size to store the copy iof original array
# Step 4: point the original array reference to copy of the array 

class Solution:
    def radixSort(self,array:list):
        max_value=float('-inf')
        for i in array:
            if i>max_value:
             max_value=i
        digit=0
        while max_value:
             
              max_value//=10
              digit+=1 
        for i in range(digit):
            array=self.countingSort(array,i) 
        return array
    def countingSort(self,array:list,digit:int):
        digit_array=[]
        for i in array:
            digit_array.append((i//(10**digit))%10)
        max_value=float('-inf') 
        for i in digit_array:
            if i>max_value:
                max_value=i 
        freq=[0]*(max_value+1)
        for i in digit_array:
            freq[i]+=1 
        # cumulative sum 
        for i in range(1,max_value+1):
            freq[i]+=freq[i-1]
        
        result=[0]*len(array)
        print(freq)
        for i in range(len(result)-1,-1,-1):
            d=(array[i]//(10**digit))%10
            
          
            result[freq[d]-1]=array[i] 
            freq[d]-=1
        print(result)
        return result 



class TestApp:
    def testing_case_one(self):
        assert Solution().radixSort([11,32,111,90,556,1,2,0])==[0,1,2,11,32,90,111,556]
    def testing_case_two(self):
        assert Solution().radixSort([4,11,778,12,90,0,0,1,1])==[0,0,1,1,4,11,12,90,778] 









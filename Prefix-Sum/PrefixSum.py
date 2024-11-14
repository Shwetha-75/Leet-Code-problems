# Prefix Sum
# Creating result array of same size
class Solution:
    def calculatingPrefixSum(self,array:list):
        # create an array of same size as the given array
        n=len(array) 
        prefix_sum=[0]*n 
        prefix_sum[0]=array[0]
        
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+array[i] 
        return prefix_sum
     
# Most optimized way
class Solution_1:
      def calculatingPrefixSum(self,array:list):
          n=len(array)
          for i in range(1,n):
              array[i]+=array[i-1]
          return array
def main():
    sol=Solution()
    result=sol.calculatingPrefixSum([1,2,3,4,5,6])
    print(result)
    solution_1=Solution_1()
    result_1=solution_1.calculatingPrefixSum([1,2,3,4,5,6])
    print(result_1)
main()


# Test Case 1 
# Input : [1,2,3,4,5,6]
# Output : [1, 3, 6, 10, 15, 21]

# Test Case 2
# Input : [10, 20, 10, 5, 15]
# Output : [10, 30, 40, 45, 60]
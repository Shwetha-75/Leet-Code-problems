'''
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

1 <= n, x <= 108.   

'''
class Solution:
    def minimumArrayEnd(self,n:int,x:int):
        # def is_valid(value2:int,x:int):
        #     if x & value2==x: return True 
        #     return False 
        # array=[]
        # nums=x+1 
        # array.append(x)
        # while len(array)<n:
        #       if is_valid(nums,x):
        #           array.append(nums)
        #       nums+=1 
        # print(array)
        # return array[n-1]
        # Taking XOR on every possible values
        # Exeecding time limit
        result=x
        while n>1:
              result=(result)+1 | x
              n-=1 
        return result
def main():
    sol=Solution()
    result=sol.minimumArrayEnd(4,1)
    print(result)
main()
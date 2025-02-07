# Using hash map 
class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        hash_map:dict[int,list]=dict({})
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                temp=nums[i]*nums[j]
                if temp in hash_map:
                    hash_map[temp].append((nums[i],nums[j]))
                else: 
                    hash_map[temp]=[(nums[i],nums[j])]
        count=0 
        
        for key in hash_map:
            
            temp=hash_map[key]
            if len(temp)>=2:
                   denominator=(len(temp)-2)
                   if denominator==0:
                       count+=math.factorial(len(temp))//2
                   else:
                       count+=(math.factorial(len(temp))//math.factorial(denominator))//2
        return 8*count  



# Brute Force Approach 
# class Solution:
#     def tupleSameProduct(self, nums: list[int]) -> int:
        
#         count=0 
#         n=len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if i==j: continue 
#                 product=nums[i]*nums[j]
#                 for k in range(n):
#                     if k==i or k==j: continue 
#                     for m in range(n):
#                         if m==i or m==j or m==k: continue 
#                         product_2=nums[k]*nums[m]
#                         if product_2==product: count+=1 
#         return count 


class TestApp:
        def testing_case_one(self):
            assert Solution().tupleSameProduct([2,3,4,6])==8 
        def testing_case_two(self):
            assert Solution().tupleSameProduct([1,2,4,5,10])==16 
        def testing_case_three(self):
            assert Solution().tupleSameProduct([1,2,3,6])==8
            
        def testing_case_four(self):
            assert Solution().tupleSameProduct([535,634,280,538,517,861,363,670,817,885,89,595,813,633,674,652,117,179,133,887,430,729,818,297,47,18,889,202,329,374,328,427,694,660,943,577,253,506,385,748,616,147,162,537,304,158,168,467,453,426,645,292,822,203,296,980,316,695,323,27,480,715,268,906,361,955,966,768,441,49,588,231,988,539,376,921,890,334,597,586,384,923,942,713,858,765,129,600,145,154,798,797,902,722,693,940,331,138,727,223])==664
        
        def testing_case_five(self):
            assert Solution().tupleSameProduct([2,3,4,6,8,12])==40
import math 


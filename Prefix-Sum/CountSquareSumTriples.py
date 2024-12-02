'''

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:

1 <= n <= 250.

'''

import math
class Solution:
    def countTriples(self,n:int):
        # def odd_pythagorean_triples(x):
            
        #     return [((x**2)/2)-0.5,((x**2)/2)+0.5]
        # def even_pythagorean_triples(x):
            
        #     return [(x/2)**2-1,(x/2)**2+1]
        # count=0
        # arr=[float(i+1) for i in range(n)]
        
        # result=[]
        # final_result=[]
        # for i in range(len(arr)):
        #     if arr[i]%2!=0:
        #        result=odd_pythagorean_triples(arr[i])
        #     else:
        #         result=even_pythagorean_triples(arr[i])
            
                
        #     if result[0] in arr and result[1] in arr:
        #         if sorted([result[0],result[1],arr[i]]) not in final_result:
        #             final_result.append(sorted([result[0],result[1],arr[i]]))
        # print(final_result)
                
        # return len(final_result)*2
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
               
                   if i!=j and  math.sqrt(((i*i)+(j*j))).is_integer() and math.sqrt(((i*i)+(j*j)))<=n and math.sqrt(((i*i)+(j*j)))>=0 : count+=1 
        return count
def main():
    sol=Solution()
    result=sol.countTriples(5)
    print(result)
main()
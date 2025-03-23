class Solution:
      def findMaximumBribe(self,q:list[int]):
        #   identify the people who as taken the bribe 
        bribe_ppl={}
        n=len(q)
        for i in range(n):
            if q[i]>(i+1):
                bribe_ppl[q[i]]=i 
        # find the maximum bribe 
        max_count=0 
        print(bribe_ppl)
        
        for key,value in bribe_ppl.items():
            max_count=max(max_count,key-(value+1))
        if max_count>2:
            print("Too chaotic")
        else:
            count=0
            for i in range(n):
                for j in range(n-i-1):
                    if q[j]>q[j+1]:
                        q[j],q[j+1]=q[j+1],q[j]
                        count+=1 
            print(count)
        
        return "Too chaotic" if max_count>2 else max_count 
    
# Optimal Approach using Bubble Sort 
class Solution:
      def findMaximumBribe(self,q:list[int]):
            count,limit,currentValue=0,0,0
            n=len(q)
            for i in range(n):
                for j in range(1,n-i):
                    if q[j-1]>q[j]:
                          if currentValue!=q[j-1]:
                              limit=1 
                              currentValue=q[j-1]
                          else:
                              limit+=1 
                          if limit>2:
                              print("Too chaotic")
                              return 
                      #     swapping 
                          q[j-1],q[j]=q[j],q[j-1]
                          count+=1
            print(count)          
                         
# optimized approach 
class Solution:
      def findMaximumBribe(self,q:list[int]):
            count=0 
            for i in range(len(q)):
                if q[i]-(i+1)>2:
                    print("Too chaotic")
                    return 
                for j in range(max(0,q[i]-2),i):
                    if q[j]>q[i]:
                        count+=1 
            print(count)  

Solution().findMaximumBribe([1 ,2 ,5 ,3 ,7 ,8 ,6 ,4])

class TestApp:
      def testing_case_one(self):
          assert Solution().findMaximumBribe([1,2,3,5,4,6,7,8])==1 
      def testing_case_two(self):
          assert Solution().findMaximumBribe([4,1,2,3])=='Too chaotic'
      def testing_case_three(self):
          assert Solution().findMaximumBribe([2,1,5,3,4])==2
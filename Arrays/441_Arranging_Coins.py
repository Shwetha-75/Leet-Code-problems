class Solution:
      def arrangeCoins(self, n: int) -> int:
            coins=[1]*n
            result=[]
            for i in range(n):
                temp=[]
                for _ in range(i+1):
                    if coins:
                      temp.append(1)
                      coins.pop()
                    else:
                      temp.append(0)
                result.append(temp)
                if not coins:
                   break
            stairs=0 
            for i in result:
                if i[-1]==1:
                    stairs+=1 
                else:
                    break 
            return stairs
        
class Solution:
      def arrangeCoins(self, n: int) -> int:
          index=1
          temp=n
          result=[1]
          i=2 
          n-=1 
          while n>0:
                result.append(result[-1]+i)
                n-=i 
                i+=1 
          if temp==result[-1]:
              return result[-1]-result[-2]
          return (result[-1]-result[-2])-1
class Solution:
      def arrangeCoins(self, n: int) -> int:
          if n==1: return 1
          temp=n
          result=1 
          i=2
          n-=1
          while n>0:
                result+=i
                n-=i 
                i+=1
          print(i)
          if result==temp:
              return result-(i-1)
          else:
              return result-i-2

class TestApp:
      def testing_case_one(self):
          assert Solution().arrangeCoins(6)==3
      def testing_case_two(self):
          assert Solution().arrangeCoins(8)==3 
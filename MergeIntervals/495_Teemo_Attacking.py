class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        result=set()
        for i in timeSeries:
            temp,seconds=duration,i 
            while temp!=0:
                  result.add(seconds)
                  seconds+=1 
                  temp-=1 
        return len(result)
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        count=0 
        for i in range(len(timeSeries)-1):
            # if the time is getting overlapped 
            if timeSeries[i]+duration> timeSeries[i+1]:
                count+=timeSeries[i+1]-timeSeries[i]
            else:
                count+=duration 
        return count+duration 

class TestApp:
      def testing_case_one(self):
          assert Solution().findPoisonedDuration([1,4],2)==4 
      def testing_case_two(self):
          assert Solution().findPoisonedDuration([1,2],2)==3
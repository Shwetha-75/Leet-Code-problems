'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

* MovingAverage(int size) Initializes the object with the size of the window size.
* double next(int val) Returns the moving average of the last size values of the stream.

Example 1:

Input
[ "MovingAverage ", "next ", "next ", "next ", "next "]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:

* 1 <= size <= 1000
* -105 <= val <= 105
* At most 104 calls will be made to next.

'''

class MovingAverage:
        def __init__(self,size:int):
            self.size=size 
            self.array=[]
            self.sum=0 
        def addNext(self,next:int)->int: 
            if len(self.array)==self.size:
                number=self.array.pop(0)
                self.sum-=number 
                self.array.append(next)
                self.sum+=next 
                return self.sum/self.size 
            else:
                self.array.append(next)
                self.sum+=next 
                print(self.sum)
                return self.sum/len(self.array)

class TestApp:
      def testing_case_one(self):
          array=["MovingAverage","next","next","next","next"]
          moving=MovingAverage(3)
          result=[None,moving.addNext(1),moving.addNext(10),moving.addNext(3),moving.addNext(5)]
          print((result))
          assert result==[None, 1.0, 5.5, 4.666666666666667, 6.0]
           
        
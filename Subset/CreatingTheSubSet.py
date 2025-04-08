class Solution:
      def activity(self,arr:list[int]):
            result=[]
            def helper(arr:list[int],subset:list[int],index:int,result:list[int]):
                  if index==len(arr):
                      result.append(subset[:])
                      return 
                  subset.append(arr[index])
                  helper(arr,subset,index+1,result)
                  subset.pop()
                  helper(arr,subset,index+1,result)
            helper(arr,[],0,result)
            print(result)
            
# using iteration 
class Solution:
    def activity(self,arr:list[int]):
        result=[[]]
        for value in arr:
            result+=[i+[value] for i in result]
        print(result)
Solution().activity([1,2,3])
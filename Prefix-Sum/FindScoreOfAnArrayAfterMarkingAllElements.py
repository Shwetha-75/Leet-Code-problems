import sys
class Solution:
    def findScore(self,nums:list[int]):
        sorted_array=sorted(nums)
        score=0
        visited=set()
        print
        while sorted_array:
              temp=sorted_array.pop(0)
              index=nums.index(temp)
              print(sorted_array,temp)
              
              print("index-->",index)
              #--------------------------------------   
              if index>0 and index<len(nums)-1:
                 if nums[index-1] in sorted_array:sorted_array.remove(nums[index-1])
                 if nums[index+1] in sorted_array:sorted_array.remove(nums[index+1])
                 visited.add(index-1)
                 visited.add(index+1)
                 
              elif index==0 and index+1<=len(nums)-1:
                   if nums[index+1] in sorted_array:sorted_array.remove(nums[index+1])
                   print(sorted_array)
                   visited.add(index+1)
                  
              elif index==len(nums)-1 and index-1>=0:
                  if nums[index-1] in sorted_array:sorted_array.remove(nums[index-1])
                  visited.add(index-1)
              score+=temp
              print("temp-->",temp)
        return score
def main():
    sol=Solution()
    result=sol.findScore([2,1,3,4,5,2])
    print(result)
main()            
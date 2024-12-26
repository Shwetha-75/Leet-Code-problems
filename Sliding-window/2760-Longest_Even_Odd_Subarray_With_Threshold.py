# {Pending....}
class Solution:
      def longestAlternatingSubarray(self,nums:list[int],threshold:int):
          max_len,n=0,len(nums)
          temp=set()
          for i in range(n):
              if nums[i]%2==0:
                 
                  temp.add(nums[i])
              for j in range(i+1,n):
                  if j==n-1:
                      if nums[j]<=threshold and nums[j-1]%2!=nums[j]%2:
                       
                       temp.add(nums[j])
                       
                  elif nums[j]<=threshold and nums[j]%2!=nums[j+1]%2:
                       print(nums[j],nums[j-1])
                       temp.add(nums[j])
                  else:
                      break
              if len(temp)==1: 
                  temp.pop()%2==0
                  max_len=max(max_len,len(temp))
              else:     
                  max_len=max(max_len,len(temp))
              temp.clear()
          return max_len 
def main():
    sol=Solution()
    result=sol.longestAlternatingSubarray([2,4] ,7)
    print(result)
main()
temp=set()
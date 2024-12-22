class Solution:
      def maxFrequency(self,nums:list[int],k:int):
          if len(nums)==1: return 1
          if not nums: return 0
          nums.sort()
          left,right,max_count,temp_count=0,1,1,k
          n=len(nums)
          temp=nums[left:right+1]
          flag=True
          
          while left<n and right<n and left<=right:
                max_value=max(temp)
                for i in range(len(temp)):
                    print(temp,temp_count)
                    if max_value==temp[i]: continue
                    if max_value-temp[i]<=temp_count:
                        val=max_value-temp[i]
                        temp[i]+=val
                        temp_count-=val
                        flag=True
                    else:
                        flag=False
                        break 
                if flag:
                    if right+1<n:
                       
                        max_count=max(max_count,len(temp))
                        
                        temp.append(nums[right+1])
                        right+=1
                        
                        print(temp_count)
                    else:break
                      
                else:
                    if left+1<n:
                        temp=nums[left+1:right+1:]
                        # print(temp)
                        left+=1
                        temp_count=k
          return max_count  
def main():
    sol=Solution()
    result=sol.maxFrequency([3,9,6],2)
    print("Result:",result)
main()
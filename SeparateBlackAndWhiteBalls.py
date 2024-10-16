class Solution:
    def separateBlackAndWhiteBalls(self,string:str):
        # ans,counter_zero,counter_one=0,0,0
        # one,zero=False,False
       
        # for i in range(len(string)-1,-1,-1):
            
        #     if string[i]=='0': 
        #         counter_zero+=1
        #         zero=True 
        #     if zero and string[i]=='1':
        #         counter_one+=1
        #         one=True 
      
        # return counter_zero*counter_one if one and zero else ans 
        # Approach 2
        # Exceeds time limit
        
        # count_zero=0
        # for i in range(len(string)):
        #     if string[i]=='1':
        #        count_zero+=string[i::].count('0')
        # return count_zero
        
        count,ans=0,0
        for i in string:
             if i=='1':
                 count+=1
             else:
                 ans+=count 
        return ans
def main():
    sol=Solution()
    res=sol.separateBlackAndWhiteBalls("01010001")
    print(res)
main()
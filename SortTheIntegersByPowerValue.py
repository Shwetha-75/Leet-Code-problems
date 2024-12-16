class Solution:
    def getKth(self,lo:int,hi:int,k:int):
        def helper(number:int):
            steps=0
            while number!=1:
                  if number%2==0:
                      number//=2
                  else:
                      number=3*number+1
                  steps+=1
            return steps
        power_value=[]
        for i in range(lo,hi+1):
            power_value.append((i,helper(i)))
        power_value.sort(key=lambda x:x[1])
        print(power_value)
        return power_value[k-1][0]
def main():
    sol=Solution()
    result=sol.getKth(12,15,2)
    print(result)
main()
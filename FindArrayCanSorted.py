class Solution:
    def findArrayCanBeSorted(self,array:list):
        bitCount=bin(array[0]).count("1")
        prevMax=-1
        curMax=array[0]
        for i in range(1,len(array)):
            if bin(array[i]).count("1")!=bitCount:
                prevMax=max(prevMax,curMax)
                curMax=array[i]
                bitCount=bin(array[i]).count("1") 
            else:
                curMax=max(curMax,array[i])
            if prevMax!=-1 and array[i]<prevMax:
                return False 
        return True 
def main():
    sol=Solution() 
    result=sol.findArrayCanBeSorted([8,4,2,30,15])
    print(result)
main()
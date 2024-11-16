class Solution:
    def findLengthOfSubArray(self,arr:list):
        stack=[]
        stack.append(arr[0])
        for i in range(1,len(arr)-1):
            if arr[i-1]<=arr[i] and arr[i]<=arr[i+1]:
                if stack and stack[-1]<=arr[i]:
                    stack.append(arr[i])
            elif arr[i-1]==arr[i] and stack[-1]<=arr[i]:
                stack.append(arr[i])
        if not stack : return len(arr)-1 
        
        if stack and stack[-1]<=arr[-1]:
            stack.append(arr[-1])
        print(stack)
        return len(arr)-len(stack)
def main():
    sol=Solution()
    result=sol.findLengthOfSubArray([5,4,3,2,1])
    print(result)
main()
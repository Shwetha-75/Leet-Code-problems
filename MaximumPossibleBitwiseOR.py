class Solution:
    def maximumPossibleBitwiseOR(self,arr:list):
        maximum_possible=arr[0]
        for i in range(1,len(arr)):
            maximum_possible^=arr[i]
        print(maximum_possible)
def main():
    sol=Solution()
    sol.maximumPossibleBitwiseOR([2,1,5])
main()
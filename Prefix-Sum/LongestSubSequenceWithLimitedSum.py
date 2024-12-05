class Solution:
    def answerQueries(self,nums:list[int],queries:list[int]):
        nums.sort()
        result=[]
        print(nums)
        def helper(num:int):
            print(num)
            temp=0
            for i in range(len(nums)):
                 temp+=nums[i]
                 if not temp<=num:
                     return i
            return len(nums)
        for i in queries:
            result.append(helper(i))
        return result 
def main():
    sol=Solution()
    result=sol.answerQueries([4,5,2,1],[3,10,21])
    print(result)
main()
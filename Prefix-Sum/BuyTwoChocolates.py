class Solution:
    def buyChoco(self,prices:list,money:int):
        prices.sort()
        bill=money-(prices[0]+prices[1])
        return money if bill<0 else bill 
def main():
    sol=Solution()
    result=sol.buyChoco([3,2,3],3)
    print(result)
main()